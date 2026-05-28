import os
import json
import ollama
#from pydantic import Json

print("==================================================")
print("  Local AI Chatbot with PERMANENT Hard Drive Memory")
print("  Conversations are saved even after closing code! ")
print("       Type your prompt. Type 'exit' to quit.     ")
print("==================================================")

# Name of the local storage file on your hard drive
MEMORY_FILE = "C:/Users/ajayd/OneDrive/Desktop/Ajay/Agri App/ai-python-basics/chat_memory.json"

# 1. LOAD HISTORICAL MEMORY (If the file exists)
if os.path.exists(MEMORY_FILE):
    try:
        with open(MEMORY_FILE, "r") as file:
         chat_history = json.load(file)
        print(f" Loaded {len(chat_history)} past exchange logs from system cache.")
    except (Json.JSONDecodeError, ValueError):
        # This catches empty files or corrupt characters and resets safely
        chat_history = []
        print("Found an empty or corrupt memory file. Resetting to a clean timeline.")
else:
    chat_history = []
    print(" Created a brand new conversation session timeline.")

while True:
    user_input = input("\nYou: ").strip()
    
    if user_input.lower() == 'exit':
        # 5. SAVE HISTORICAL MEMORY TO FILE ON EXIT
        print("\nSaving conversation matrix to hard drive file...")
        with open(MEMORY_FILE, "w") as file:
            json.dump(chat_history, file, indent=4)
        print("Memory cached successfully. Goodbye!")
        break
        
    if not user_input:
        continue
        
    # 2. Append user input
    chat_history.append({'role': 'user', 'content': user_input})
    print("AI: Thinking...")
    
    try:
        # 3. Stream history log array directly to local engine
        response = ollama.chat(
            model='llama3.2',
            messages=chat_history
        )
        
        # 4. Extract and print response
        ai_response = response['message']['content']
        print(f"\nAI: {ai_response}")
        
        # Append AI response to track turns
        chat_history.append({'role': 'assistant', 'content': ai_response})
        
    except Exception as e:
        print(f"\n[Error]: Memory stream failed: {e}")
        break

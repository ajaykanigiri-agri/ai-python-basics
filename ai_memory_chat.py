import ollama

print("==================================================")
print("     Local AI Chatbot with Conversational Memory   ")
print("    The model will remember context during chat.  ")
print("        Type your prompt. Type 'exit' to quit.     ")
print("==================================================")

# 1. Initialize our chat history database list.
# This list will grow over time, storing every turn of the conversation.
chat_history = []

while True:
    user_input = input("\nYou: ").strip()
    
    if user_input.lower() == 'exit':
        print("\nClosing memory context session. Goodbye!")
        break
        
    if not user_input:
        continue
        
    # 2. Append the user's new message to our history tracking list
    chat_history.append({'role': 'user', 'content': user_input})
    
    print("AI: Thinking...")
    
    try:
        # 3. CRITICAL: We pass the ENTIRE chat_history list to Ollama,
        # not just the single new prompt sentence!
        response = ollama.chat(
            model='llama3.2',
            messages=chat_history
        )
        
        # 4. Extract the AI's response text
        ai_response = response['message']['content']
        print(f"\nAI: {ai_response}")
        
        # 5. Append the AI's response to the history list so it remembers its own words next turn
        chat_history.append({'role': 'assistant', 'content': ai_response})
        
    except Exception as e:
        print(f"\n[Error]: Memory stream failed: {e}")
        break

import ollama

print("--- Initializing Local AI Pipeline ---")

# 1. Define the topic prompt you want the AI to handle
user_prompt = "Give me a 2-sentence explanation of what a neural network is."

print(f"Sending prompt to Llama: '{user_prompt}'\n")

try:
    # 2. Call the local model using the python library layout
    response = ollama.chat(
        model='llama3.2', 
        messages=[
            {
                'role': 'user',
                'content': user_prompt,
            }
        ]
    )
    
    # 3. Extract and print the generated text response out of the return object
    ai_response = response['message']['content']
    print("--- Local AI Response ---")
    print(ai_response)
    print("-------------------------")

except Exception as e:
    print(f"An error occurred while connecting to Ollama: {e}")
    print("Make sure the Ollama desktop app icon is running in your system tray.")

import ollama

print("*************************************")
print("Welcome to your Local AI Chatbot!") 
print ("Type your prompt below. Type 'exit' to quit.")
print("**************************************")

# Start a continuous loop to keep the conversation alive
while True: 

    # 1. Capture user input from the terminal and clean up spaces
    user_input = input("\nYou: ").strip() 

    # 2. Check if the user wants to close the application
    if user_input.lower() == 'exit':
        print("Closing your AI Chatbot... , Thank you for choosing us! Goodbye!")
        break  # Exit the loop and end the program

    # 3. Skip empty inputs if the user just presses Enter
    if not user_input:
        print("Please enter a prompt to continue the conversation.")
        continue  # Skip

        print("AI is thinking...")

    try:
        # 4. Stream the dynamic input straight to your local model and get the response
        response = ollama.chat(
            model='llama3.2',
            messages=[
                {
                    'role': 'user',
                    'content': user_input,
                }
            ]
        )

        # 5. Extract and display the answer
        ai_response = response['message']['content']
        print(f"\nAI: {ai_response}")

    except Exception as e:
        print(f"\n[Error]: Connection to model failed: {e}")
        print("Please check that the Ollama app is running in the background.")


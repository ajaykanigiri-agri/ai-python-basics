print("--- Local AI Gateway ---")
print("Available commands: SUMMARIZE, TRANSLATE, CHAT, EXIT\n")

# Run a continuous loop until the user types 'exit'
while True:
    # 1. Capture input, remove extra spaces (.strip), and make it lowercase (.lower)
    user_command = input("Enter a command: ").strip().lower()

    # 2. Check the cleaned-back command against known keywords
    if user_command == "exit":
        print("Closing the AI Gateway for test. Goodbye!")
        break  # This stops the while loop immediately
        
    elif user_command == "summarize":
        text_to_process = input("Paste the text you want to summarize: ")
        print(f"\n[AI Action]: Processing text layout... (Simulated summary of: '{text_to_process[:30]}...')")
        print("-> Summary output completed successfully.\n")
        
    elif user_command == "translate":
        target_lang = input("Enter target language (e.g., Spanish, French): ")
        print(f"\n[AI Action]: Translating workspace pipelines into {target_lang}...")
        print("-> Translation engine complete.\n")
        
    elif user_command == "chat":
        print("\n[AI Action]: Open chat session initialized. Type 'back' to change commands.")
        while True:
            chat_input = input("You: ")
            if chat_input.strip().lower() == "back":
                break
            print(f"AI: This is a placeholder response to your message: '{chat_input}'")
        print("Exited chat session.\n")
        
    else:
        # Handle typos or unsupported commands gracefully
        print(f"Error: '{user_command}' is not a recognized system command. Please try again.\n")

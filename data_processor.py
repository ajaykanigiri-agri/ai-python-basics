print("--- AI Data & File Ingestion System ---")

# 1. READ AN EXTERNAL TEXT FILE
# 'with' handles opening and closing the file safely automatically
with open("document.txt", "r") as file:
    raw_document_text = file.read()

print(" Successfully loaded 'document.txt' contents into memory.\n")

# 2. INITIALIZE PYTHON DATA STRUCTURES FOR MEMORY
# A List holds ordered history logs
history_logs = []

# A Dictionary holds metadata statistics about our app run
session_stats = {
    "total_actions": 0,
    "file_read_success": True
}

# 3. INTERACTIVE PROCESSING LOOP
while True:
    print("Commands: 1: Display Text | 2: Simulate Summary | 3: View Logs | 4: Exit")
    choice = input("Select an action (1-4): ").strip()

    if choice == "4":
        print("\nSaving session status metrics...")
        print(f"Final Session Stats: {session_stats}")
        print("Goodbye!")
        break

    elif choice == "1":
        print(f"\n--- Document Content ---\n{raw_document_text}\n------------------------\n")
        # Update our dictionary tracking stats
        session_stats["total_actions"] += 1
        # Append a simple status string to our list
        history_logs.append("Action: Displayed document contents.")

    elif choice == "2":
        summary_snippet = raw_document_text[:45] + "..."
        print(f"\n[AI Summary]: {summary_snippet}\n")
        
        session_stats["total_actions"] += 1
        # Store a structured snapshot entry inside our history list
        history_logs.append(f"Action: Simulated summary creation (Chars processed: {len(raw_document_text)}).")

    elif choice == "3":
        print("\n--- Current Application History Logs ---")
        if not history_logs:
            print("[Empty: No actions taken yet this session.]")
        else:
            # Use an index count loop to neatly print the list items
            for index, log in enumerate(history_logs, 1):
                print(f" {index}. {log}")
        print(f"Total Actions Tracked in Metadata Dict: {session_stats['total_actions']}\n")

    else:
        print("\nInvalid choice selection. Try numbers 1 through 4.\n")

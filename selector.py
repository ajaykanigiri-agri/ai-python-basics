# Ask the user for their system RAM
print("---AI Model Compatibility Checker---")
print("This tool will help you determine which AI models are compatible with your system.")
user_input = input("How many GB of RAM does your computer have? ")

# Convert the text input into a whole number (integer)
ram = int(user_input)

# Decision logic based on hardware constraints
if ram >= 32:
    print("Your system can handle the most demanding AI models.")
elif ram >= 16:
    print("Your system can handle high-end AI models.")
elif ram >= 8:
    print("Your system can handle medium-end AI models.")
elif ram < 8:
    print("Your system can't handle AI models.") 
elif ram < 4:
    print("Your system can only handle basic operations.")
else:
    print("Your system is best suited for lightweight AI models.")

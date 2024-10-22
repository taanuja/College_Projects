def decision_tree(k_base):
    for question, options in k_base.items():
        answer = input(question + " (Yes/No): ").strip().lower()
        
        # Make sure the input is valid
        while answer not in ['yes', 'no']:
            print("Invalid answer. Please respond with 'Yes' or 'No'.")
            
        
        # Traverse the decision tree based on the input
        if answer == 'yes':
            if isinstance(options, dict):
                # Recursively call the decision tree if the next step is still a question
                return decision_tree(options)
            else:
                # If it's the end of the tree (a recommendation), return the answer
                print(options)
                return
        else:
            if isinstance(options, dict):
                return decision_tree(options)
            else:
                print(options)
                return

# The knowledge base (decision tree)
K_Base = {
    "Is the computer powering on?": {
        "Yes": {
            "Is there a beeping sound?": {
                "Yes": "Check the RAM and CPU",
                "No": {
                    "Is the display showing any output?": {
                        "Yes": "Check the display connections and settings",
                        "No": "Check the power supply and motherboard"
                    }
                }
            }
        },
        "No": "Check the power supply and cables"
    }
}

# Start the decision tree
print("Welcome to the Computer Troubleshooting Guide!")
decision_tree(K_Base)

def main():
    file_name = "expenses.txt"
    total_spent = 0.0

    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read each line
            for line in file:
                # Split the line into description and amount
                parts = line.strip().split(',')
                if len(parts) == 2:
                    expense_description = parts[0]
                    amount = float(parts[1])
                    total_spent += amount
                    print(f"Expense: {expense_description}, Amount: ${amount:.2f}")
    
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    
    except IOError:
        print(f"Error: Unable to read file '{file_name}'.")

    # Print the total amount spent
    print(f"\nTotal Amount Spent: ${total_spent:.2f}")

if __name__ == "__main__":
    main()

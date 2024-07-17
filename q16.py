def main():
    # Employee details
    employees = [
        {"name": "John Doe", "age": 30, "salary": 50000},
        {"name": "Jane Smith", "age": 28, "salary": 45000},
        {"name": "Michael Johnson", "age": 35, "salary": 60000},
        {"name": "Emily Davis", "age": 32, "salary": 55000},
        {"name": "James Wilson", "age": 40, "salary": 70000}
    ]

    # File path
    file_name = "employees.txt"

    try:
        # Open file in write mode
        with open(file_name, 'w') as file:
            for employee in employees:
                # Write employee details to file
                file.write(f"Name: {employee['name']}, Age: {employee['age']}, Salary: ${employee['salary']}\n")
        
        print(f"Employee details have been written to '{file_name}' successfully.")

    except IOError:
        print(f"Error: Unable to write to file '{file_name}'.")

if __name__ == "__main__":
    main()

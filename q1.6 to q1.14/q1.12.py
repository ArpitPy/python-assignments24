def calculate_grade():
    # Accept marks for five major subjects
    marks = []
    for i in range(5):
        subject_mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(subject_mark)
    
    # Display the marks entered
    print(f"Marks entered: {marks}")
    
    # Calculate sum of marks
    total_marks = sum(marks)
    
    # Calculate percentage
    percentage = total_marks / 5
    
    # Display the percentage
    print(f"Percentage: {percentage}%")
    
    # Determine grade based on percentage using if-elif ladder
    if percentage > 85:
        grade = 'A'
    elif percentage >= 75:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    elif percentage >= 30:
        grade = 'D'
    else:
        grade = 'Reappear'
    
    # Display the grade
    print(f"Grade: {grade}")

# Run the function to calculate grade based on marks
calculate_grade()

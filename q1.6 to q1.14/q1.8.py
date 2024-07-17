# Define three pre-specified numbers
num1 = 25
num2 = 40
num3 = 15

# Using ternary operator to find the largest number
largest = num1 if (num1 >= num2 and num1 >= num3) else (num2 if (num2 >= num1 and num2 >= num3) else num3)

# Display the result
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")

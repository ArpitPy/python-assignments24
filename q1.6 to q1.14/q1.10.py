def sum_positive_numbers():
    sum = 0
    while True:
        num = float(input("Enter a number (enter a negative number to stop): "))
        if num < 0:
            break
        sum += num
    return sum

# Calculate the sum of positive numbers entered by the user
total_sum = sum_positive_numbers()
print(f"The sum of all positive numbers entered is: {total_sum}")

def find_prime_numbers():
    prime_numbers = []
    for num in range(2, 101):  # Iterate through numbers from 2 to 100
        is_prime = True
        for i in range(2, num):  # Check for factors from 2 to num-1
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers

# Find and print prime numbers between 2 and 100
prime_list = find_prime_numbers()
print(f"Prime numbers between 2 and 100: {prime_list}")

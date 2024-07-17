def find_factors(n):
    # Initialize variables
    i = 1
    factors = []

    # Iterate through numbers from 1 to n
    while i <= n:
        if n % i == 0:
            factors.append(i)  # i is a factor of n
        i += 1
    
    return factors

# Example usage
number = 36
print(f"Factors of {number}: {find_factors(number)}")

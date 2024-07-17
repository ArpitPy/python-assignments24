def main():
    file_name = "inventory.txt"

    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read and print each line
            for line in file:
                print(line.strip())  # Use strip() to remove extra newline characters

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

    except IOError:
        print(f"Error: Unable to read file '{file_name}'.")

if __name__ == "__main__":
    main()

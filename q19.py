def main():
    file_name = "paragraph.txt"
    word_count = {}

    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read the entire file content
            content = file.read()

            # Split the content into words
            words = content.split()

            # Count occurrences of each word
            for word in words:
                # Remove punctuation (if any) and convert to lowercase for case insensitivity
                cleaned_word = word.strip('.,!?').lower()
                if cleaned_word:
                    if cleaned_word in word_count:
                        word_count[cleaned_word] += 1
                    else:
                        word_count[cleaned_word] = 1
            
            # Print word counts in alphabetical order
            print("Word Counts (Alphabetical Order):")
            for word in sorted(word_count.keys()):
                print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    
    except IOError:
        print(f"Error: Unable to read file '{file_name}'.")

if __name__ == "__main__":
    main()

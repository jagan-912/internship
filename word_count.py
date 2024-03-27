def count_words(text):
    """Function to count the number of words in the given text."""
    if not text:
        return 0
    words = text.split()
    return len(words)

def main():
    """Main function to handle user input and display output."""
    print("Welcome to Word Count Program!")
    while True:
        try:
            user_input = input("Please enter a sentence or paragraph (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Thank you for using the Word Count Program. Goodbye!")
                break
            word_count = count_words(user_input)
            print(f"Word count: {word_count}")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break

if __name__ == "__main__":
    main()

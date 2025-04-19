import sys
# Check if correct number of arguments was provided
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Get the book path from command line argument
book_path = sys.argv[1]# Import your functions from stats.py

from stats import num_words, character_frequency, sort_char_frequency

# Read the book
with open(book_path) as f:
    text = f.read()
# Get word count and character frequency
word_count = num_words(text)
char_freq = character_frequency(text)
sorted_chars = sort_char_frequency(char_freq)
# Print the report
print("============ BOOKBOT ============")
print("Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")

# Print only alphabetical characters
for char_dict in sorted_chars:
    char = char_dict["char"]
    count = char_dict["count"]
    if char.isalpha():
        print(f"{char}: {count}")

print("============= END ===============")


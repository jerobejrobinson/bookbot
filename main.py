from stats import get_num_of_words
from stats import get_num_of_characters
from stats import char_sort
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_of_words(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    char_sort(get_num_of_characters(get_book_text(sys.argv[1])))
    print("--------- Character Count -------")
def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()
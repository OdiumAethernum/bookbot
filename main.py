import sys
from stats import get_num_caracters, get_num_words

if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
book_path = sys.argv[1]

def main():
    get_num_words(book_path)
    get_num_caracters(book_path)
main()    
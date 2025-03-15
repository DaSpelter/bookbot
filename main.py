from stats import *
import sys


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    path = sys.argv[1]
    text = get_book_text(path)
    
    words = num_words(text)
    chars = count_characters(text)
    sorted_chars = sort_characters(chars)





    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")

    print("--------- Character Count -------")

    

    for k in sorted_chars:
        if k['name'].isalpha():
            print(f"{k['name']}: {k['num']}")

    print("============= END ===============")


main()
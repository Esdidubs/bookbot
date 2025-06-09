from stats import num_of_words
from stats import get_char_count
from stats import sort_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        # print(file_contents)
    return file_contents



def main():
  #  book_contents = get_book_text("./books/frankenstein.txt")
    import sys
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_contents = get_book_text(sys.argv[1])
    num_of_words(book_contents)
    get_char_count(book_contents)
    sort_char_count()

main()
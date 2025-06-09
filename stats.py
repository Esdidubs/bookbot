char_count = {}

def num_of_words(text):
    word_count_array = text.split()
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {len(word_count_array)} total words")

def get_char_count(text):
    char_array = list(text)
    for character in char_array:
        character = character.lower()
        if(character in char_count):
            char_count[character] += 1
        else:
            char_count[character] = 1

def sort_char_count():
    sorted_dict = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    print("----------- Character Count ----------")
    for character in sorted_dict:
        count = sorted_dict[character]
        print(f"{character}: {count}")
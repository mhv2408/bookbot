
def count_chars(f):
    char_dict = {}
    for char in f:
        char = char.lower()
        char_dict[char] = 1 + char_dict.get(char,0)
    return char_dict
    
def count_words(f):
    word_list = f.split()
    return len(word_list)
    
def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        word_cnt = count_words(file_contents)
        print(f"{word_cnt} words found in the document")
        char_dict = count_chars(file_contents)
        for char in sorted(char_dict):
            if char.isalpha():
                print(f"The {char} character was found {char_dict[char]} times")

        print("--- End report ---")
        
main()
def main():
    book_path = 'books/frankenstein.txt'
    book = read(book_path)
    word_count = count_words(book)
    character_count = count_alphabets(book)
    print_report(book_path, word_count, character_count)


def read(path):
    with open(path, 'r', encoding='utf8') as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_alphabets(string):
    character_count = {}
    for c in string.lower():
        if c.isalpha():
            character_count[c] = character_count.get(c, 0) + 1
    return character_count


def print_report(book_path, word_count, character_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for item in sorted(character_count.items(), key=lambda x: x[1], reverse=True):
        print(f"The '{item[0]}' character was found {item[1]} times")
    print(f"--- End report ---")


if __name__ == '__main__':
    main()

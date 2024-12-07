def main():
    book_path = 'books/frankenstein.txt'
    book = read(book_path)
    word_count = count_words(book)
    character_count = count_alphabets(book)
    print(character_count)


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


if __name__ == '__main__':
    main()

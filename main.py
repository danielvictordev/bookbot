def main():
    book_path = 'books/frankenstein.txt'
    book = read(book_path)
    word_count = count_words(book)
    print(word_count)


def read(path):
    with open(path, 'r', encoding='utf8') as f:
        return f.read()


def count_words(text):
    return len(text.split())


if __name__ == '__main__':
    main()

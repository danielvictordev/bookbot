def main():
    book_path = 'books/frankenstein.txt'
    book = read(book_path)
    print(book)


def read(path):
    with open(path, 'r', encoding='utf8') as f:
        return f.read()


if __name__ == '__main__':
    main()
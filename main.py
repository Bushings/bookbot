def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    chr_count = get_character_count(book_text)

    print(book_text)
    print(f"Here is the amount of words in this book: {word_count}")
    print(f"Here is a count of each character in the book: {chr_count}")

def get_character_count(book):
    lowercase = book.lower()
    chr_count = {}
    for letter in lowercase:
        if letter in chr_count:
            chr_count[letter] = chr_count[letter] + 1
        else:
            chr_count[letter] = 1
    return chr_count     

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())




main()
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    letters = count_letters(text)

    sorted_letters = []
    for key, value in letters.items():
        sorted_letters.append({"name": key, "num": value})
    sorted_letters.sort(reverse=True, key=sort_on)

    for i in sorted_letters:
        print(f"The '{i['name']}' character was found '{i['num']}' times")
    
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_letters(text):
    letter_count = {}
    lowered_text = text.lower()
    for i in lowered_text:
        if i.isalpha():
            if i in letter_count:
                letter_count[i] += 1
            else:
                letter_count[i] = 1
    return letter_count

def sort_on(dict):
    return dict["num"]


main()

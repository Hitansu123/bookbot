def book_path():
    with open("/home/hits/Workspace/github.com/Hitansu/bookbot/Books/frankenstein.txt") as f:
        file_read = f.read()
        return file_read

# print(file_read)


def count_words():
    book = book_path()
    book_str = str(book)
    words = book_str.split()

    return len(words)

# count_words()


alphabets = {}


def count_character():
    book = book_path()
    book_str = str(book)
    book_lowercase = book_str.lower()
    for i in range(ord('a'), ord('z')+1):
        val = book_lowercase.count(chr(i))
        alphabets[chr(i)] = val
    return alphabets


# count_character()


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(alphabets):
    sorted_list = []
    alphabet = count_character()
    for ch in alphabet:
        sorted_list.append({"char": ch, "num": alphabet[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


# chars_dict_to_sorted_list(alphabets)

def main():
    book = book_path()
    num_words = count_words()
    chars_sorted_list = chars_dict_to_sorted_list(alphabets)

    print(f"--- Begin report of frakenstine.txt ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


main()

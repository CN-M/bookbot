from pprint import pprint

def main():
    book_path = 'text/frankenstein.txt'

    text = get_book_text(book_path)
    total = get_num_words(text)
    str_count = get_string_count(text)

    print_report(book_path, total, str_count)
     
def print_report(path, word_count, str_count):
    print(f"Report of {path}:")
    print("")
    print(f"Total words found in the document: {word_count}")

    print(f"The most used character was '{str_count[0]['key']}' with {str_count[0]['count']} instances!")
    print(f"The least used character was '{str_count[len(str_count) - 1]['key']}' with {str_count[len(str_count) - 1]['count']} instances!")

    print("")
    for i in range(0, len(str_count)):
            print(f"The '{str_count[i]['key']}' character was found {str_count[i]['count']} times")
    print(f"--------------------------------------------------------")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(str):
    return len(str.split())

def sort_on(dict):
    return dict['count']

def get_string_count(text): 
    str_dict = {}
    str_lst = []
    for word in text.split():
        for char in word.lower():
            if char not in str_dict:
                str_dict[char] = 1
            str_dict[char] += 1

    for key in str_dict:
        str_lst.append({ 'key' : key , 'count': str_dict[key] })

    str_lst.sort(reverse=True, key=sort_on)
    return str_lst

if __name__ == "__main__":
    main()
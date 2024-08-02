from pprint import pprint

def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    total = get_num_words(text)
    str_count = get_string_count(text)
    most_used = most_used_char(str_count)
    least_used = least_used_char(str_count)
    print_report(book_path, total, most_used, least_used, str_count)
     
def print_report(path, word_count, most_used, least_used, str_count ):
    print(f"Report of {path}:")
    print("")
    print(f"Total words found in the document: {word_count}")

    for key in most_used:
        print(f"The most used character was '{key}' with {most_used[key]} instances!")

    for key in least_used:
        print(f"The least used character was '{key}' with {least_used[key]} instances!")

    print("")
    for key in str_count:
            print(f"The '{key}' character was found {str_count[key]} times")
    print(f"--------------------------------------------------------")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(str):
    return len(str.split())

def get_string_count(text): 
    str_dict = {}
    for word in text.split():
        for char in word.lower():
            if char not in str_dict:
                str_dict[char] = 1
            str_dict[char] += 1
    return str_dict
   
def least_used_char(str_dict):
    least_used_key = ''
    least_used_value = float('inf')
    for key in str_dict:
        if str_dict[key] < least_used_value:
            least_used_key = key
            least_used_value = str_dict[key]

    return {least_used_key: least_used_value}

def most_used_char(str_dict):
    most_used_key = ''
    most_used_value = float('-inf')
    for key in str_dict:
        if str_dict[key] > most_used_value:
            most_used_key = key
            most_used_value = str_dict[key]

    return {most_used_key: most_used_value}


if __name__ == "__main__":
    main()
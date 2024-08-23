path = "books/frankenstein.txt"

def count_words(phrase):
    words = phrase.split()
    return (len(words))

def get_book_text(path):
     with open(path) as f:
        return f.read()
     
def count_characters(text):
    char_dict = {}
    for character in text:
        lowered = character.lower()
        if lowered in char_dict.keys():
                char_dict[lowered] += 1
        else: 
                char_dict[lowered] = 1
    return char_dict

def sort_on(dict):
      return dict["num"]

def print_sorted_chars(char_dict):
        char_list = []
        for value in char_dict:
              char_list.append({"character":value,"num":char_dict[value]})
        char_list.sort(reverse=True,key=sort_on)
        for c in char_list:
              # ignore non alphabet characters
              if not c["character"].isalpha():
                    continue
              print(f"The '{c["character"]}' was found {c["num"]} times")

def main():
   
        #print(file_contents)
        print(count_words(get_book_text(path)))
        #print(count_characters(get_book_text(path)))
        print_sorted_chars(count_characters(get_book_text(path)))



main()

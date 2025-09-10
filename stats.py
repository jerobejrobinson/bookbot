def get_num_of_words(string):
    return len(string.split())

def get_num_of_characters(string):
    char_count = {}
    for char in list(string):
        if char_count.get(char.lower()) == None:
            char_count[char.lower()] = 1
        else:
            char_count[char.lower()] += 1
    return char_count

def char_sort(characters):
    char_list = []
    for key in characters:
        if key.isalpha() == True:
            char_list.append({'char': key, 'num': characters[key]})
    
    def sort_on(item):
        return item["num"]
    
    char_list.sort(reverse=True, key=sort_on)

    for item in char_list:
        print(f"{item["char"]}: {item["num"]}")


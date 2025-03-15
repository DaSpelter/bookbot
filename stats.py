def num_words(str):
    str_split = str.split()
    return len(str_split)

def count_characters(str):
    char_count = {}
    for k_raw in str:
        k = k_raw.lower()
        if k not in char_count:
            char_count[k] = 1
        else:
            char_count[k] += 1
    return char_count

def sort_on(dict):    
    return dict["num"]


def sort_characters(dict):
    sort_dict = []
    for key, value in dict.items():
        sort_dict.append({"name": key, "num": value})
    sort_dict.sort(reverse=True, key=sort_on)
    return sort_dict
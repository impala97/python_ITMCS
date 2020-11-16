def funWithAnagram(text_items):
    text_cp = text_items[:]
    [text_cp.remove(text_items[i]) for i in range(1, len(text_items)) if sort_string(text_items[i-1]) == sort_string(text_items[i])]
    return text_cp

def sort_string(text):
    text_list = list(text)
    text_list.sort()
    return "".join(text_list)

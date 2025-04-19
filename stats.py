def num_words(text):
    return len(text.split())

def character_frequency(text):
    frequency = {}
    for char in text.lower():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def sort_char_frequency(char_frequency):
    # Convert dictionary to list of dictionaries
    char_list = []
    for char, count in char_frequency.items():
        char_list.append({"char": char, "count": count})
    
    # Sort by count in descending order
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

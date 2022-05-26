# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word):
    string1 = "hello"
    string2 = "racecar"
    string1 = string1.casefold()
    string2 = string2.casefold()
    
    reversed_string1 = reversed(string1)
    reversed_string2 = reversed(string2)
    if list(string1) == list(reversed_string1) or list(string2) == list(reversed_string2):
        print("TRUE!")
    else:
        print("FALSE!")

    return word

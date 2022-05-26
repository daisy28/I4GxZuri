# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


string = input("Enter a word: ")
string = string.casefold()
    
reversed_string = reversed(string)
if list(string) == list(reversed_string):
    print(string)
    print("TRUE!")
else:
    print(string)
    print("FALSE!")

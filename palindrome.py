# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagram(str1, str2):
    str1 = "listen"
    str2 = "silent"
    
    str_anagram = sorted(str1)
    str2_anagram = sorted(str2)

    if(str_anagram == str2_anagram):
        return True
    else:
        return False
    print(find_anagram("listen", "silent"))

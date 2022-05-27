def read_file_content(filename):
    with open("file.txt") as file_object:
        filename = file_object.read()
        return filename


def count_words():
     text = read_file_content("file.txt")
     counts = dict()
     words = text.split
     for word in words:
         if word in counts:
             counts[word] +=1
         else:
             counts[word] = 1
             return counts
     print(count_words())

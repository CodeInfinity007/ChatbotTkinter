def find(word, file):
    for i in file:
        if i == word:
            #print("Found")
            return True
    else:
        #print("Not Found")
        return False

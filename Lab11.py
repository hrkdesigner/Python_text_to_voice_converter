from gtts import gTTS

d = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot',
     'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
     'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec',
     'r': 'romeo', 's': 'sierra', 't': 'tango', 'u': 'uniform',
     'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee', 'z': 'zulu'}


name = 'hrk designer'


# This function checks if the input name has any spaces between letters, it deletes them first and then runs the code.

def stringToICAO(data):
    listOfWords = list(data.lower())
    for eachLetter in listOfWords:
        if " " == eachLetter:
            listOfWords.remove(eachLetter) 
    listOfNewWords = []
    for item in listOfWords:
        listOfNewWords.append(d[item])
    print(listOfNewWords)
    return data + 'is like' + str(listOfNewWords)


myobj = gTTS(text=stringToICAO(name), lang='en')
myobj.save("Result.mp3")
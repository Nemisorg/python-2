naam = input("Wat is je naam? ")
print("Hallo " + naam + ", welkom bij galgje.")
count = 0
word = ("galgje")
goedeletters = ""
while True:
    streep = ("_ _ _ _ _ _")
    print (streep)
    letter = input("Geef een letter... ")
    if letter in word:
        print("Goed geraden!")
        goedeletters = (goedeletters + letter)
        print ("De letters " + goedeletters + " heb je goed.")
    elif letter == "?":
        wordguess = input("Probeer het woord maar te raden... ")
        if wordguess == word:
            print("Je hebt het woord geraden!")
            break
        else:
            print("Je hebt fout geraden!")
            print("Je hebt verloren!")
            break
    elif len(goedeletters) == 6:
        wordguess = input("Probeer het woord maar te raden... ")
        if wordguess == word:
            print("Je hebt het woord geraden!")
            break
        else:
            print("Je hebt fout geraden!")
            print("Je hebt verloren!")
            break
    else:
        print("Fout")
        count = (count +1)

    if count == 6:
        print("Je hebt verloren!")
        break

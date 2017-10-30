def een():
    print(" ___")

def twee():
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|___")

def drie():
    print("___________")
    print("|/         |")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|___")

def vier():
    print("___________")
    print("|/         |")
    print("|        (o o)")
    print("|         /|\ ")
    print("|         / \ ")
    print("|        |___|")
    print("|        |___|")
    print("|___     |   |")

def vijf():
    print("___________")
    print("|/         |")
    print("|        (x x)")
    print("|         /|\ ")
    print("|         / \ ")
    print("|")
    print("|")
    print("|___")

def toongalg():
    if count == 1:
        een()
    if count == 2:
        twee()
    if count == 3:
        drie()
    if count == 4:
        vier()
    if count == 5:
        vijf()





naam = input("Wat is je naam? ")
print("Hallo " + naam + ", welkom bij galgje.")
count = 0
word = input("Laat iemand een woord invoeren dat je moet raden: \n")
while " " in word:
    word = input("Voer één woord in!")
goedeletters = ""
streep = ["_ "] * len(word)
alleletters = ("")
while True:
    letter = input("Geef een letter. (Typ QQ om op te geven of '?' om te raden.): ")
    if letter == "QQ":
        vijf()
        print("Je hebt jezelf aangegeven en je bent opgehangen.")
        break

    for letter2 in range(len(word)):
        if letter is word[letter2]:
            streep[letter2] = letter
        print (streep[letter2], end='')
    print('')

    if "_ " not in streep:
        print('je hebt gewonnen!')
        toongalg()
        break
    if letter in word:
        if len(letter) >= 2:
            print("je hebt meer dan een letter gebruikt")
        elif letter in goedeletters:
            print ("Je hebt deze letter al genoemd. Noem een andere letter.")
        else:
            goedeletters = (goedeletters + letter)

    elif letter in alleletters:
        print ("Je hebt deze letter al genoemd. Noem een andere letter.")
    elif len(letter) >= 2:
        print("je hebt meer dan een letter gebruikt")
    elif letter == "?":
        wordguess = input("Probeer het woord maar te raden... ")
        if wordguess == word:
            print("Je hebt het woord geraden!")
            break
        else:
            print("Je hebt fout geraden!")
            print("Je hebt verloren!")
            vijf()
            break
    elif letter in goedeletters:
        print ("Je hebt deze letter al genoemd. Noem een andere letter.")
    else:
        print("Fout")
        count = (count +1)
        toongalg()

    if count == 5:
        toongalg()
        print("Je hebt verloren!")
        break

    alleletters = (alleletters + letter)

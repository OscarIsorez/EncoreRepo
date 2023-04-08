debut="dialoguetest"
from dialogue import Dialogue
from choix import Choix
from enigme import Enigme


def split_long_words(text, max_length=40):
    words = text.split()
    result = ""
    current_line = ""
    for word in words:
        if len(current_line + " " + word) <= max_length:
            current_line += " " + word
        else:
            result += current_line + "\n"
            current_line = word
    result += current_line
    return result

class Naratif:
    def __init__(self):
        self.courantName = debut
        self.courant = Dialogue(debut, "fin/fin")
        self.suivant = None;self.courant.suivant()
        self.fini = False
        self.paragraph = self.courant.getDialog()

        self.chemin = dict()
        with open("./ressources/chemin.txt", "r") as f:
            for line in f:
                splited = line.split(";")
                self.chemin[splited[0]] = splited[1].replace('\n', '')
    def allerSuivant(self):
        if(not self.suivant is None):
            split = self.suivant.split("/")
            name = split[1]
            print("Go to " + name)
            match split[0]:
                case "fin":
                    self.fini = True
                case "dialogue":
                    self.courant = Dialogue(name, self.chemin[name])
                    self.paragraph = self.courant.getDialog()
                case "choix":
                    self.courant = Choix(name)
                case "enigme":
                    self.courant = Enigme(name, self.chemin[name])
    
    def paragraphSuivant(self):
        if(isinstance(self.courant, Dialogue)):
            paraSuivant = self.courant.next()
            if(paraSuivant == None): self.suivant = self.courant.suivant()
            else: self.paragraph = paraSuivant
    
    def paragraphCourant(self): return [self.paragraph[0],split_long_words(self.paragraph[1])]
    
    def buttonClick(self, index): 
        print(index)

        if isinstance(self.courant, Choix) :
            self.suivant = self.courant.getPath(0)
    
    #Input
    def inputType(self):
        if(isinstance(self.courant, Choix)): "Button"
        elif(isinstance(self.courant, Enigme)): "Input"
        else : None
    def inputSend(self, reponse):
        if isinstance(self.courant, Enigme):
            if(self.courant.testReponse(reponse)): 
                self.suivant = self.courant.suivant()

naratif = Naratif()

fini = False
while(not naratif.fini) :
    if(naratif.inputType() == "Input"):
        naratif.inputSend("Reponse1")
    elif (naratif.inputType() == "Button"):
        naratif.buttonClick(1)
    else :
        print(naratif.paragraphCourant())
        naratif.paragraphSuivant()
    naratif.allerSuivant()

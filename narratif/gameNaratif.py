debut="dialoguetest"
from dialogue import Dialogue
from choix import Choix
from enigme import Enigme

class Naratif:
    def __init__(self):
        self.courantName = debut
        self.courant = Dialogue(debut, "dialogue/dialogue2")
        self.suivant = self.courant.suivant()
    
        self.paragraph = self.courant.getDialog()

        self.chemin = dict()
        with open("./ressources/chemin.txt", "r") as f:
            for line in f:
                splited = line.split(";")
                self.chemin[splited[0]] = splited[1].replace('\n', '')
        print(self.chemin)
    def allerSuivant(self):
        if(self.suivant != None):
            split = self.suivant.split("/")
            name = split[1]
            print("Go to " + name)
            print("Suivant " + self.chemin[name])
            match split[0]:
                case "fin":
                    ()
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
    
    def paragraphCourant(self): return self.paragraph
    
    def buttonClick(self, index): 
        if isinstance(self.courant, Choix) :
            self.suivant = self.courant.getPath(0)
    
    #Input
    def inputType(self):
        if(isinstance(self.courant, Choix)): "Button"
        elif(isinstance(self.courant, Enigme)): "Input"
        else : None
    def inputSend(self, text):
        if(isinstance(self.courant, Enigme)):
            if(self.courant.testReponse): 
                self.suivant = self.courant.suivant()
    def fini(self):
        self.suivant = None

a = Naratif()
a.paragraphSuivant()
a.allerSuivant()
a.paragraphSuivant()
a.paragraphSuivant()
a.allerSuivant()
a.inputSend("Reponse1")
a.allerSuivant()
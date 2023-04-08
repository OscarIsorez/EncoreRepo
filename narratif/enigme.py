from etape import Etape
class Enigme(Etape):
    def __init__(self, name, suite):
        Etape.__init__(self, suite)
        with open("./ressources/enigme/" + name + ".txt", "r", encoding="utf-8") as f:
            for line in f:
                splited = line.split(";")
                self.enonce = splited[0]
                self.reponse = splited[1]
        self.suite = suite
    def getEnonce(self):
        return self.enonce
    def testReponse(self, reponse):
        return self.reponse == reponse
    def suivant(self):
        return self.suite
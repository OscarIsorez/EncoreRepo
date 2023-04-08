from etape import Etape
class Enigme(Etape):
    def __init__(self, name, suite):
        Etape.__init__(self, suite)
        with open("./ressources/enigme/" + name + ".txt", "r") as f:
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

def split_long_words(text, max_length=20):
    words = text.split()
    result = []
    current_line = ""
    for word in words:
        if len(current_line + " " + word) <= max_length:
            current_line += " " + word
        else:
            result.append(current_line.strip())
            current_line = word
    result.append(current_line.strip())
    return result

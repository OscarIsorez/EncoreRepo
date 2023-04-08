from etape import Etape
class Dialogue(Etape):
    def __init__(self, name, suite):
        Etape.__init__(self, suite)
        self.paroles = []
        self.index = 0
        with open("./ressources/dialogue/" + name + ".txt", "r") as f:
            for line in f:
                splited = line.split(";")
                self.paroles.append(splited)
    def getDialog(self):
        if(self.index >= 0 and self.index < len(self.paroles)):
            return self.paroles[self.index]
        else: 
            return None
    def next(self):
        if(self.index < len(self.paroles)) :
            self.index += 1
            return self.getDialog()
        else: return None
    def previous(self):
        if(self.index > 0):
            self.index -= 1
            return self.getDialog(self)
        else: return None
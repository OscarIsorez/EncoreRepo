class Choix:
    def __init__(self, name):
        self.choix = []
        self.paths = []
        with open("./ressources/choix/" + name + ".txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            self.choix.append(lines[0].split(";"))
            self.paths.append(lines[1].split(";"))
    def choices(self): 
        return self.choix
    def getPath(self, index):
        if(index >= 0 and index < len(self.paths)): return self.path[index]
        else: return None
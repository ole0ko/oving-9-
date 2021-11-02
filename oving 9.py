
myDictIsVeryAverage = {}
c = 0


with open("sporsmaal.txt", "r") as file:
    row = file.readline
    for i in row:
        print(i)

"""
class Sporsmaal:
    def __init__(self, spørsmål, altA, altB, altC, altD, svar):
        self.spørsmål = spørsmål
        self.svar = svar
        self.altA = altA
        self.altB = altB
        self.altC = altC
        self.altD = altD
    
    def __str__(self):
        
        return ("\n",str(self.spørsmål), " \n", "1. ", str(self.altA), "2. ", str(self.altB), "3. ", str(self.altC), "4. ", str(self.altD)," \n")
    
    def sjekk_svar(self):
        userInput = int(input("Ditt svar (1..4): "))
        if userInput == self.svar:
            print("Korrekt\n")
        else:
            if rundeTo:
                if userInput == 4:
                    print("Subjektivt heilt rett, men feil i denna quizzen.. :( ")
            else:
                print("Feil\n")
"""








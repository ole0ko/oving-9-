import io

myDictIsVeryAverage = {}
c = 0

with io.open("oving_8_rein_tekst.txt", "r", encoding="utf-8") as file: 
    lines = file.readlines()
    for row in lines:
        c+=1
        for word in row.split():
            if word in myDictIsVeryAverage:
                continue
            myDictIsVeryAverage[word] = c

print(myDictIsVeryAverage)
for x, y in myDictIsVeryAverage.items():
    print(x, y)


class spørsmålSpill:
    def __init__(self, spørsmål, altA, altB, altC, altD, svar):
        self.spørsmål = spørsmål
        self.altA = altA
        self.altB = altB
        self.altC = altC
        self.altD = altD
        self.svar = svar
    
    def __str__(self):
        #tempList = (str(self.spørsmål), " \n", "1. ", str(self.altA), " \n", "2. ", str(self.altB), " \n", "3. ", str(self.altC)," \n", "4. ", str(self.altD),)
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





rundeEn = spørsmålSpill("Hva er gjennomsnittlig alder for en kvinnelig hummer", "10 år", "20 år", "50 år", "hummere dør ikke av naturlige årsaker", 3)
for i in rundeEn.__str__():
    print(i)
rundeEn.sjekk_svar()


rundeTo = spørsmålSpill("Hva står IPA for?", "Inglish Pale Ale", "Icelandic Pale Ale", "Indian Pale Ale", "Driteg i d smake drit uansett", 3) 
for i in rundeTo.__str__():
    print(i)
rundeTo.sjekk_svar()




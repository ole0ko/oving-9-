


class Sporsmaal:
    def __init__(self, quizText="", correctAnswer=None, alternatives=""):
        self.quizText = quizText
        self.correctAnswer = correctAnswer
        self.alternatives = alternatives

    def __str__(self):
        print("\n\n")
        a = self.quizText+" \n"
        for i in self.alternatives:
            a+="\n"+i
        return a
        

    def korrekt_svar_tekst(self):
        korrektSvar = int(self.correctAnswer)+1
        return korrektSvar




def getValues():
    questionList = []
    with open("sporsmaalsfil.txt", "r") as file:
        row = file.readlines()
        for i in row:
            ans = i.split(":")        
            altList = (ans[2].split(", "))
            questionList.append(Sporsmaal(ans[0], ans[1], altList))
    return questionList





try:
    if __name__ == "__main__":
        player1 = 0
        player2 = 0
        round = getValues()

        for i in round:
            print(i)
            p1Answer = int(input("Player 1 answer: "))
            p2Answer = int(input("\nPlayer 2 answer: "))
            correctAnswer = i.korrekt_svar_tekst()
            print("\n\nDet retta svaret va ", correctAnswer)
            if (p1Answer) == correctAnswer:
                player1+=1
                print("\nPlayer 1 was correct")
            else:
                print("\nPlayer 1 was incorrect")
            if p2Answer == correctAnswer:
                player2+=1
                print("\nPlayer 2 was correct")
            else:
                print("\nPlayer 2 was incorrect")
        if player1 > player2:
            print("Player 1 won, player 2 git gud")
        elif player1 < player2:
            print("Player 2 won, player 1 git gud")
        else:
            print("Draw, ggwp ")
        print("Player 1: ", player1, " pts")
        print("Player 2: ", player2, " pts")
            
except:
    print("Please enter actual numbers, you silly goose")
    
























"""
num_lines = sum(1 for line in open("sporsmaalsfil.txt"))
rounds = []
for i in range(num_lines):
    round.append([])
"""

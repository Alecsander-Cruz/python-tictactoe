import random

playableSpaces = [1,2,3,4,"X",6,7,8,9]
draw = False
win = False
loose = False
numberOfPlays = 1

def verifyIfMoveIsPossible(num, list):
    if list[num-1] == "X" or list[num-1] == "O":
        return False
    else:
        return True
    
def computerPlay():
    while True:
        computerRandom = random.randrange(1, 10, 1)
        if verifyIfMoveIsPossible(computerRandom, playableSpaces):
            playableSpaces[computerRandom-1] = "X"
            break

def winCondition():
    global win
    if (playableSpaces[0] == 'O') and (playableSpaces[1] == 'O') and (playableSpaces[2] == 'O'):
        win = True
        return True
    elif (playableSpaces[3] == 'O') and (playableSpaces[4] == 'O') and (playableSpaces[5] == 'O'):
        win = True
        return True
    elif (playableSpaces[6] == 'O') and (playableSpaces[7] == 'O') and (playableSpaces[8] == 'O'):
        win = True
        return True
    elif (playableSpaces[0] == 'O') and (playableSpaces[3] == 'O') and (playableSpaces[6] == 'O'):
        win = True
        return True
    elif (playableSpaces[1] == 'O') and (playableSpaces[4] == 'O') and (playableSpaces[7] == 'O'):
        win = True
        return True
    elif (playableSpaces[2] == 'O') and (playableSpaces[5] == 'O') and (playableSpaces[8] == 'O'):
        win = True
        return True
    elif (playableSpaces[0] == 'O') and (playableSpaces[4] == 'O') and (playableSpaces[8] == 'O'):
        win = True
        return True
    elif (playableSpaces[2] == 'O') and (playableSpaces[4] == 'O') and (playableSpaces[6] == 'O'):
        win = True
        return True
    else:
        win = False
        return False

def looseCondition():
    global loose
    if (playableSpaces[0] == 'X') and (playableSpaces[1] == 'X') and (playableSpaces[2] == 'X'):
        loose = True
        return True
    elif (playableSpaces[3] == 'X') and (playableSpaces[4] == 'X') and (playableSpaces[5] == 'X'):
        loose = True
        return True
    elif (playableSpaces[6] == 'X') and (playableSpaces[7] == 'X') and (playableSpaces[8] == 'X'):
        loose = True
        return True
    elif (playableSpaces[0] == 'X') and (playableSpaces[3] == 'X') and (playableSpaces[6] == 'X'):
        loose = True
        return True
    elif (playableSpaces[1] == 'X') and (playableSpaces[4] == 'X') and (playableSpaces[7] == 'X'):
        loose = True
        return True
    elif (playableSpaces[2] == 'X') and (playableSpaces[5] == 'X') and (playableSpaces[8] == 'X'):
        loose = True
        return True
    elif (playableSpaces[0] == 'X') and (playableSpaces[4] == 'X') and (playableSpaces[8] == 'X'):
        loose = True
        return True
    elif (playableSpaces[2] == 'X') and (playableSpaces[4] == 'X') and (playableSpaces[6] == 'X'):
        loose = True
        return True
    else:
        loose = False
        return False

def drawCondition():
    global draw
    if numberOfPlays >= 9:
        draw = True
        return True
    else:
        draw = False
        return False

    
def finalMessage():
    tablePrint()
    if win:
        print("Você ganhou!")
    if loose:
        print("Você perdeu!")
    if draw:
        print("O jogo deu empate!")



def tablePrint():
    print("+-------+-------+-------+")
    print("|       |       |       |")
    for i in range(0,3):
        print("|   ", playableSpaces[i], "   ", sep="", end="")
        if i == 2:
            print("|")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    for i in range(3,6):
        print("|   ", playableSpaces[i], "   ", sep="", end="")
        if i == 5:
            print("|")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    for i in range(6,9):
        print("|   ", playableSpaces[i], "   ", sep="", end="")
        if i == 8:
            print("|")
    print("|       |       |       |")
    print("+-------+-------+-------+")

while draw == False and win == False and loose == False:
    tablePrint()
    try:
        move = int(input("\nDigite seu movimento: "))
        if move < 0:
            print("Por favor, digite apenas NÚMEROS entre 1 e 9!")
            continue
        elif move > 9:
            print("Por favor, digite apenas NÚMEROS entre 1 e 9!")
            continue
        if verifyIfMoveIsPossible(move, playableSpaces):
            playableSpaces[move-1] = "O"
            numberOfPlays += 1
            if winCondition() or drawCondition():
                break
            computerPlay()
            numberOfPlays += 1
            if looseCondition() or drawCondition():
                break
        else:
            print("Essa casa já foi preenchida. Por favor, escolha outra")    

        print(playableSpaces)

        
    except ValueError:
        print("Por favor, digite apenas NÚMEROS entre 1 e 9!")
    except KeyboardInterrupt:
        break
    except:
        print("Alguma coisa deu errado!")

  

finalMessage()

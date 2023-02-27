
import math

# 0 | 1 | 2 
# 3 | 4 | 5
# 6 | 7 | 8 
#user is O=1
# #AI is X =0



def main():
    print("Welcome to AI-Tic-Tac-Toe")
    field = [0,0,0,0,0,0,0,0,0]
    printfield(field)
    while (not check_win(field)):
        a = int(input("Which field do you want to play?\n"))
        while field[a]!=0:
            a = int(input("Which field do you want to play?\n"))
        field[a]=2
        printfield(field)
        if check_win(field):
            break
        answerAI = get_AI_answer(field)
        field[answerAI]= 1
        printfield(field)
    print("\n\nGAME DONE!\n")
    printfield(field)



# Ausgang der Funktion:
# 3 unentschieden
# 2 User hat gewonnen
# 1 AI hat gewonnen
# 0 kein ende


def check_win(field_array):
    if (field_array[0]==field_array[1]==field_array[2]==0) or (field_array[0]==field_array[1]==field_array[2]==1):
        return	field_array[0]
    elif (field_array[3]==field_array[4]==field_array[5]==0) or (field_array[3]==field_array[4]==field_array[5]==1):
        return	field_array[3]
    elif (field_array[6]==field_array[7]==field_array[8]==0) or (field_array[6]==field_array[7]==field_array[8]==1):
        return	field_array[6]
    elif (field_array[0]==field_array[3]==field_array[6]==0) or (field_array[0]==field_array[3]==field_array[6]==1):
        return field_array[0]
    elif (field_array[1]==field_array[4]==field_array[7]==0) or (field_array[1]==field_array[4]==field_array[7]==1):
        return field_array[1]
    elif (field_array[2]==field_array[5]==field_array[8]==0) or (field_array[2]==field_array[5]==field_array[8]==1):
        return field_array[2]
    
    if (field_array[0]==field_array[4]==field_array[8]==0) or (field_array[0]==field_array[4]==field_array[8]==1):
        return	field_array[0]
    elif (field_array[2]==field_array[4]==field_array[6]==0) or (field_array[2]==field_array[4]==field_array[6]==1):
        return field_array[2]
    elif 0 not in field_array:
        return 3
    return 0

def utils(field_array, turn):
    #abbruchbedingung
    end = check_win(field_array)
    if end:
        if end==3:
            return 1.0
        elif end==2:
            return -10
        elif end==1:
            return 10
    utility=0
    #look over the field and see, what moves could be played
    possible_moves=[]
    for i in range(9):
        if field_array[i]==0:
            possible_moves.append(i)
    #probability for a move
    probability=1/len(possible_moves)
    #iterates through the tree and adds the utils
    for j in possible_moves:
        copy = list.copy(field_array)
        copy[j]=turn
        utility=utility+(utils(copy,(turn+1)%2)*probability)
    return utility






#returns the caluclated best branch
def get_AI_answer(field_array):
    possible_moves=[]
    for i in range(9):
        if field_array[i]==0:
            possible_moves.append(i)
    #probability for a move
    probability=1/len(possible_moves)
    #iterates through the tree and adds the utils
    max=-9000000000
    position=0
    for j in possible_moves:
        copy = list.copy(field_array)
        copy[j]=0
        utility=(utils(copy,1)*probability)
        if utility>max:
            max = utility
            position = j
    return position


#prints the field
def printfield(field_array):
    for i in range(3):
        c0 = ' ' 
        c1 = ' '
        c2 = ' '
        if field_array[0+(i*3)]==1:
            c0='X'
        elif field_array[0+(i*3)]==2:
            c0='O'
        if field_array[1+(i*3)]==1:
            c1='X'
        elif field_array[1+(i*3)]==2:
            c1='O'
        if field_array[2+(i*3)]==1:
            c2='X'
        elif field_array[2+(i*3)]==2:
            c2='O'
        print(" "+c0+" | "+c1+" | "+c2+" \n")
    print("\n\n")

if __name__=='__main__':
    main()
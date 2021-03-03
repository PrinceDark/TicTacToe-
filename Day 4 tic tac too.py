## TIC TAK TOO


import random
bas=True
while(bas==True):
    x=random.randint(0,2)
    if(x==0):
        print("Player I will play first")
    else:
        print("Player II will play first")
    p1i=input("Which one will player I choose('X'or'O')::")
    p1i=p1i.upper()
    if(p1i=="X"):
        p2i="O"
    else:
        p2i="x"
    a=[" "," "," "," "," "," "," "," "," "]

    print("The board format is like this")
    print(" ","0"," ","||"," ","1"," ","||"," ","2"," ")
    print("######||#######||######")
    print(" ","3"," ","||"," ","4"," ","||"," ","5"," ")
    print("######||#######||######")
    print(" ","6"," ","||"," ","7"," ","||"," ","8"," ")
    print("Lets start the game")


    def printBoard():
        print("The board format is like this")
        print(" ",a[0]," ","||"," ",a[1]," ","||"," ",a[2]," ")
        print("######||#######||######")
        print(" ",a[3]," ","||"," ",a[4]," ","||"," ",a[5]," ")
        print("######||#######||######")
        print(" ",a[6]," ","||"," ",a[7]," ","||"," ",a[8]," ")
    def printLogic(x):
        v=x
        game=True
        while(game==True):
            if(v==0):
                print("TURN :: Player I")
            else:
                print("TURN :: Player II")
            printBoard()
            sele=int(input("Select the number of box to mark::"))
            k=0
            l=0
            j=0
            while(k==0):
                if(a[sele]!=" "):
                    print("This place is aleray occpy .")
                    sele=int(input("Select the other box for mark"))
                else:
                    k=1
            if(v==0):
                a[sele]=p1i
            else:
                a[sele]=p2i


            if((p1i==a[2] and a[2]==a[4] and a[4]==a[6]) or (p1i==a[0] and a[0]==a[4] and a[4]==a[8]) or (p1i==a[1] and a[1]==a[4] and a[4]==a[7]) or (p1i==a[3] and a[3]==a[4] and a[4]==a[5])):
                printBoard()
                print("WINNER ::  Player I")
                game=False
            elif((p2i==a[0] and a[0]==a[4] and a[4]==a[8]) or (p2i==a[2] and a[2]==a[4] and a[4]==a[6]) or (p2i==a[1] and a[1]==a[4] and a[4]==a[7]) or (p2i==a[3] and a[3]==a[4] and a[4]==a[5])):
                printBoard()
                print("WINNER ::  Player II")
                game=False
            elif(a[0]!=" " and a[1]!=" " and a[2]!=" " and a[3]!=" " and a[4]!=" " and a[5]!=" " and a[6]!=" " and a[7]!=" " and a[8]!=" "):
                print("DRAW")
                printBoard()
                game=False
            else:
                print("NEXT PLAYER TURN !!!")
                v=1-v


    printLogic(x)
    y=input("Do you want to play another Game")
    if y[0].lower()=='n':
        bas=False

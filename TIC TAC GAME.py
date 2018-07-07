import random
def display_board(board):
    print (board[7]+"|"+"       "+board[8]+"|"+"       "+"|"+board[9]+"|")
    print("_______________________________________________________")
    print (board[4]+"|"+"       "+board[5]+"|"+"       "+"|"+board[6]+"|")
    print("_______________________________________________________")
    print (board[1]+"|"+"       "+board[2]+"|"+"       "+"|"+board[3]+"|")
def player_input():
    input=''
    player1=''
    player2=''
    while input!='x' and input!='o':
        input=raw_input("player 1,enter input x or o ")
        player1=input
        if player1=='x':
            player2='o'
        else:
            player2='x'
def place_marker(board, input, position):
    board[position]=input
def win_check(board, input):
    place_marker(test_board,input,position)
    flag=False
    if board[7]==board[4]==board[1]=='x' or board[7]==board[4]==board[1]=='o':
        flag= True
    elif board[8]==board[5]==board[2]=='x' or board[8]==board[5]==board[2]=='o':
        flag =True
    elif board[9]==board[6]==board[3]=='x' or board[9]==board[6]==board[3]=='o':
        flag= True
    elif board[7]==board[5]==board[3]=='x' or board[7]==board[5]==board[3]=='o':
        flag =True
    elif board[9]==board[5]==board[1]=='x' or board[9]==board[5]==board[1]=='o':
        flag =True
    elif board[3]==board[2]==board[1]=='x' or board[3]==board[2]==board[1]=='o':
        flag=True
    elif board[4]==board[5]==board[6]=='x' or board[4]==board[5]==board[6]=='o':
        flag=True
    elif board[7]==board[8]==board[9]=='x' or board[7]==board[8]==board[9]=='o':
        flag=True
    return flag
def choose_first():
    mylist=['x','o']
    k=random.choice(mylist)
    return k
def space_check(board, position):
        flag=True
        if board[position]=='x' or board[position]=='o':
            flag=False
        return flag
def player_choice(board):
    var1=True
    while(var1==True):
        position=int(raw_input("enter the  position"))
        temp1=space_check(board,position)
        if temp1==True:
            var1=False
    return position
def replay():
    flag=False
    temp2=raw_input("press yes if you want to play again no to exit")
    if temp2=="yes":
        flag= True
    else:
        flag=True
    return flag
temp3=True
while temp3:
        print("WELCOME TO TIC TAC TOE")
        test_board=['#','','','','','','','','','']

        player_input()
        input=choose_first()
        print("player with {} may enter input".format(input))
        position=player_choice(test_board)
        while win_check(test_board,input)==False:
                    place_marker(test_board,input,position)
                    display_board(test_board)
                    break
        while win_check(test_board,input)==False:
            print("next player can enter the input")
            position=player_choice(test_board)
            if input=="x":
                input="o"
            else:
                input="x"
            place_marker(test_board,input,position)
            display_board(test_board)
        print("player with {} input won".format(input))
        temp3=replay()
        print('\n'*100)

#---- GLobal variable ----#

#board
board =['-','-','-',
        '-','-','-',
        '-','-','-',]

#if gmae still running 
game_is_running = True

#who won? who lost? who tied?
winner = None

#whos turn is it 
current_player = 'X'


#have a display 

def board_display():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])  
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])  
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])  


#This will execute the entire game by putting together the functions 
def play_game():

    #Here we want to play the board when the user is playing
    board_display()

    #this will run while the game is going on
    while game_is_running:
        #this will handle the turn of the  palyer whos ever turn it is
        handle_turn(current_player)

        #This whill constantly keep checking if the game is over
        check_if_game_over()

        #this will flip to the other player
        flip_player()
    
    #tha game has ended
    if winner == "X" or winner == "O":
        print(winner + ' won.')
    elif winner == None:
        print('Tie.')


#This will handle the turns of each player
def handle_turn(player):
    print(player + "'s turn.")
    global current_player
    position = input("Choose a position between the numbers 1-9: ")
    if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid input. Please choose a number between 1-9: ")
    position = int(position) - 1

    board[position] = current_player
    board_display()


#This will identift if the game is over 
def check_if_game_over():
    check_for_winner()
    check_if_tie()


#Cheching for who wont he game
def check_for_winner():
    global winner
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check daigonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else: 
        #there was no winner
        winner = None
    return

#THis will check rows
def check_rows():
    global game_is_running

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #this now tells us who exactly won. by picking one of the letters in the winning row we know who exactly who the winner is because that winning row has the same letter in it.
    if row_1 or row_2 or row_3:
        game_is_running = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return 

#this will check colummns
def check_columns():
    global game_is_running
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_is_running = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return 

#This will check diagonals
def check_diagonals():
    global game_is_running
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2:
        game_is_running = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

#This will see if there is a tie
def check_if_tie():
    global game_still_going 
    if "-" not in board:
        game_still_going = False
    return

#This function will flip the players turn 
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = 'X'
    return 

play_game()







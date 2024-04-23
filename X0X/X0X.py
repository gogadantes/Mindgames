import random as rand

who_win = 22

player1_turn = 1
player1_row = 0
player1_column = 0

player2_turn = 1
player2_row = 0
player2_column = 0

size_cort_x = 0
size_cort_y = 0

# 0 - row position
# 1 - column position
# 2 - input status
# 3 - player symbol
map = [[1,1,0,5], [1,2,0,5], [1,3,0,5],
       [2,1,0,5], [2,2,0,5], [2,3,0,5],
       [3,1,0,5], [3,2,0,5], [3,3,0,5]]

def cort_coord():
    global size_cort_x, size_cort_y, map
    center_x = 0
    center_y = 0
    count = 0

    size_cort_x = int(input('Input width of cort for game(dots): '))
    size_cort_y = int(input('Input height of cort for game(dots): '))
    block_x = size_cort_x / 3
    block_y = size_cort_y / 3

    start_x = center_x - (block_x * 2.5)
    start_y = center_y - (block_y * 2.5)
    coordx = start_x
    coordy = start_y

    for i in range(3):
        for i in range(3):
            arcord = []
            arcord.append(coordx)
            arcord.append(coordy)
            map[count].append(arcord)
            coordx = coordx + block_x
            count += 1
        coordy = coordy + block_y
        coordx = start_x

    print(map)


def choose_symbol():    
    while (True):
        player1_symbol = input('Enter symbol for Player 1: ')

        if player1_symbol == 'x' or player1_symbol == 'X':
            player1_symbol = 1
            break
        elif player1_symbol == 'o' or player1_symbol == 'O' or player1_symbol == '0':
            player1_symbol = 0
            break
        else:
            print('Invalid symbol input')

    if player1_symbol == 0:
        player2_symbol = 1
    elif player1_symbol == 1:
        player2_symbol = 0

    return [player1_symbol, player2_symbol]

def turn(player_symbol): 
        global map, player1_turn, player2_turn

        if (player_symbol == 1):
            print("Player 1. Turn number: ", player1_turn)
            row = int(input('Input row: '))
            column = int(input('Input column: ')) 
        elif (player_symbol == 0):
            print("Player 2. Turn number: ", player2_turn)
            row = int(input('Input row: '))
            column = int(input('Input column: '))       
        

        for i in range(len(map)):
            if (map[i][0] == row and map[i][1] == column):
                if (map[i][2] == 0):
                    map[i][2] = 1
                    map[i][3] = player_symbol
                    if (player_symbol == 1):
                        player1_turn+=1
                    else:
                        player2_turn+=1
                    return
                else:
                    print('Invalid input')
                    break

        print(map)

def win_print(player_symbol):
    if (player_symbol == 1):
        print("Player 1 Win!")
    elif (player_symbol == 0):
        print("Player 2 Win")

def win_check():
    global map
    global who_win
    #horizontal win for player 1
    if (map[0][0] == 1 and map[1][3] == 1 and map[2][3] == 1):
        who_win = 1
        return 322
    if (map[3][3] == 1 and map[4][3] == 1 and map[5][3] == 1):
        who_win = 1
        return 322
    if (map[6][3] == 1 and map[7][3] == 1 and map[8][3] == 1):
        who_win = 1
        return 322
    
    #vertical win for player 1
    if (map[0][3] == 1 and map[3][3] == 1 and map[6][3] == 1):
        who_win = 1
        return 322
    if (map[1][3] == 1 and map[4][3] == 1 and map[7][3] == 1):
        who_win = 1
        return 322
    if (map[2][3] == 1 and map[5][3] == 1 and map[8][3] == 1):
        who_win = 1
        return 322
    
    #skos win for player 1
    if (map[0][3] == 1 and map[4][3] == 1 and map[8][3] == 1):
        who_win = 1
        return 322
    if (map[2][3] == 1 and map[4][3] == 1 and map[6][3] == 1):
        who_win = 1
        return 322
    

    #horizontal win for player 2
    if (map[0][3] == 0 and map[1][3] == 0 and map[2][3] == 0):
        who_win = 0
        return 322
    if (map[3][3] == 0 and map[4][3] == 0 and map[5][3] == 0):
        who_win = 0
        return 322
    if (map[6][3] == 0 and map[7][3] == 0 and map[8][3] == 0):
        who_win = 0
        return 322
    
    #vertical win for player 2
    if (map[0][3] == 0 and map[3][3] == 0 and map[6][3] == 0):
        who_win = 0
        return 322
    if (map[1][3] == 0 and map[4][3] == 0 and map[7][3] == 0):
        who_win = 0
        return 322
    if (map[2][3] == 0 and map[5][3] == 0 and map[8][3] == 0):
        who_win = 0
        return 322
    
    #skos win for player 2
    if (map[0][3] == 0 and map[4][3] == 0 and map[8][3] == 0):
        who_win = 0
        return 322
    if (map[2][3] == 0 and map[4][3] == 0 and map[6][3] == 0):
        who_win = 0
        return 322
    
    #dubt
    if (map[0][2] == 1 and map[1][2] == 1 and map[2][2] == 1 and map[3][2] == 1 and map[4][2] == 1 and map[5][2] == 1 and map[6][2] == 1 and map[7][2] == 1 and map[8][2] == 1):
        return 404
    
    return 0

def game():
    global map, who_win

    cort_coord()

    while (True):
        symbol_result = choose_symbol()
        player1_symbol = symbol_result[0]
        player2_symbol = symbol_result[1]

        while(True):
            turn(player1_symbol)
            print(map)
            if (win_check() == 322 or win_check() == 404):
                if (win_check() == 404):
                    print("It's a doubt!!!")
                    break
                else:
                    win_print(who_win)
                    break
                
            turn(player2_symbol)
            print(map)
            if (win_check() == 322 or win_check() == 404):
                if (win_check() == 404):
                    print("It's a doubt!!!")
                    break
                else:
                    win_print(who_win)
                    break
        
        print("Do you want to play again? (type 'yes' or 'no')")
        while(True):
            question = input()
            if (question == 'yes'):
                break
            elif(question == 'no'):
                return
        

game()
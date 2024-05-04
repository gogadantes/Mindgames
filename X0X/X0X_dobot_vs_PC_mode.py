import threading
import DobotDllType as dType
import random as rand
import math

""" CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

#Load Dll
api = dType.load()

#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])

print('Angle Error: ', dType.GetAngleSensorStaticError(api))
print('Base Error: ', dType.GetBaseDecoderStaticError(api))


#Magician
dType.SetEndEffectorParamsEx(api, 59.7, 0, 0, 1)
dType.SetPTPJumpParamsEx(api,50,100,1) """

who_win = 22
mode = 0

player1_turn = 1
player1_row = 0
player1_column = 0

player2_turn = 1
player2_row = 0
player2_column = 0

size_cort_x = 0
size_cort_y = 0

center_x = 211
center_y = 25
start_z = -51
block_x = 0
block_y = 0

# 0 - row position
# 1 - column position
# 2 - input status
# 3 - player symbol
#map = [[1,1,0,5], [1,2,0,5], [1,3,0,5],
 #      [2,1,0,5], [2,2,0,5], [2,3,0,5],
  #     [3,1,0,5], [3,2,0,5], [3,3,0,5]]

map = []

def win_arrays(blocks):
    hor_wins = []
    ver_wins = []
    skos_wins = []

    for i in range(blocks):
        count = []
        hor_wins.append(count)
        for j in range(blocks):
            timemap = []
            timemap.append(i + 1)
            timemap.append(j + 1)
            hor_wins[i].append(timemap)

    for i in range(blocks):
        count = []
        ver_wins.append(count)
        for j in range(blocks):
            timemap = []
            timemap.append(j + 1)
            timemap.append(i + 1)
            ver_wins[i].append(timemap)

    for i in range(1):
        count = []
        skos_wins.append(count)
        for j in range(blocks):
            timemap = []
            timemap.append(j + 1)
            timemap.append(j + 1)
            skos_wins[i].append(timemap)

    
        count = []
        skos_wins.append(count)
        sks = 1
        for j in reversed(range(blocks)):
            timemap = []
            timemap.append(j + 1)
            timemap.append(sks)
            skos_wins[i + 1].append(timemap)
            sks += 1

    print(hor_wins)
    print(ver_wins)
    print(skos_wins)

def choose_mode():
    while (True):
        mode = input('Input game mode do you choose ("player" or "comp")').lower()
        if (mode != 'player' or mode != 'comp'):
            print('Choose right game mode!')

def cort_coord():
    global size_cort_x, size_cort_y, center_x, center_y, start_z, block_x, block_y, map
    count = 0

    size_cort_x = int(input('Input width of cort for game(dots): '))
    size_cort_y = int(input('Input height of cort for game(dots): '))
    blocks = int(input('Input number of blocks for game: '))
    block_x = size_cort_x / blocks
    block_y = size_cort_y / blocks

    start_x = center_x - (block_x * (blocks / 2))
    start_y = center_y - (block_y * (blocks / 2))
    
    coordx = start_x
    coordy = start_y

    win_arrays(blocks)

    for i in range(blocks):
        for j in range(blocks):
            timemap = []
            timemap.append(i + 1)
            timemap.append(j + 1)
            timemap.append(0)
            timemap.append(5)
            map.append(timemap)

            arcord = []
            arcord.append(coordx)
            arcord.append(coordy)
            map[count].append(arcord)
            coordx = coordx + block_x
            count += 1
        coordy = coordy + block_y
        coordx = start_x

    print(count)
    print(map)

    #draw pole 
    dType.SetPTPCmdEx(api, 0, center_x,  center_y,  start_z, 0, 1)
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + size_cort_x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + size_cort_x,  start_y + size_cort_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + size_cort_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    #draw blocks
    for i in range(len(map)):
        dType.SetPTPCmdEx(api, 0, center_x,  center_y,  start_z, 0, 1)
        dType.SetPTPCmdEx(api, 0, map[i][4][0],  map[i][4][1],  start_z, 0, 1)

        current_pose = dType.GetPose(api)
        dType.SetPTPCmdEx(api, 2, map[i][4][0] + block_x,   map[i][4][1],  start_z, current_pose[3], 1)

        current_pose = dType.GetPose(api)
        dType.SetPTPCmdEx(api, 2, map[i][4][0] + block_x,  map[i][4][1] + block_y,  start_z, current_pose[3], 1)

        current_pose = dType.GetPose(api)
        dType.SetPTPCmdEx(api, 2, map[i][4][0],  map[i][4][1] + block_y,  start_z, current_pose[3], 1)

        current_pose = dType.GetPose(api)
        dType.SetPTPCmdEx(api, 2, map[i][4][0],  map[i][4][1],  start_z, current_pose[3], 1)
    
    dType.SetPTPCmdEx(api, 0, center_x,  center_y,  start_z, 0, 1)

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

def draw_symbol(player_symbol, element_number):
    global block_x, block_y

    if (player_symbol == 1):
        dType.SetPTPCmdEx(api, 0, map[element_number][4][0],  map[element_number][4][1],  start_z, 0, 1)

        current_pose = dType.GetPose(api)
        dType.SetPTPCmdEx(api, 2, map[element_number][4][0] + block_x,  map[element_number][4][1] + block_y,  start_z, current_pose[3], 1)

        dType.SetPTPCmdEx(api, 0, map[element_number][4][0],  map[element_number][4][1] + block_y,  start_z, 0, 1)

        current_pose = dType.GetPose(api)
        dType.SetPTPCmdEx(api, 2, map[element_number][4][0] + block_x,  map[element_number][4][1],  start_z, current_pose[3], 1)
    else:
        rad = 0
        steps = 10
        if (block_x > block_y):
            rad = block_y / 2
        else:
            rad = block_x / 2

        dType.SetPTPCmdEx(api, 0, (map[element_number][4][0] + (block_x / 2)) + (rad * math.cos(360 * (0 / steps))),  (map[element_number][4][1] + (block_y / 2)) + (rad * math.sin(360 * (0 / steps))),  start_z, 0, 1)

        for i in range(steps):
            x = (map[element_number][4][0] + (block_x / 2)) + (rad * math.cos(360 * (i / steps)))
            y = (map[element_number][4][1] + (block_y / 2)) + (rad * math.sin(360 * (i / steps)))
            current_pose = dType.GetPose(api)
            dType.SetPTPCmdEx(api, 2, x,  y,  start_z, current_pose[3], 1)
        

    dType.SetPTPCmdEx(api, 0, center_x,  center_y,  start_z, 0, 1)

def turn(player_symbol): 
        global map, player1_turn, player2_turn

        if (mode == 'player'):
            if (player_symbol == 1):
                print("Player 1. Turn number: ", player1_turn)
                row = int(input('Input row: '))
                column = int(input('Input column: ')) 
            elif (player_symbol == 0):
                print("Player 2. Turn number: ", player2_turn)
                row = int(input('Input row: '))
                column = int(input('Input column: '))    
        elif (mode == 'comp'):
            if (player_symbol == 1):
                print("Player. Turn number: ", player1_turn)
                row = int(input('Input row: '))
                column = int(input('Input column: ')) 
            elif (player_symbol == 0):
                print("Computer. Turn number: ", player1_turn)
                row = rand.randint(1,9)
                column = rand.randint(1,9)
        

        for i in range(len(map)):
            if (map[i][0] == row and map[i][1] == column):
                if (map[i][2] == 0):
                    map[i][2] = 1
                    map[i][3] = player_symbol
                    if (player_symbol == 1):
                        player1_turn+=1
                    else:
                        player2_turn+=1

                    draw_symbol(player_symbol, i)
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

def draw_win(aligment, start, end): #horizontal - 1, vertical - 2, skos - 3
    if (aligment == 1): #horizontal

        dType.SetPTPCmdEx(api, 0, map[start][4][0] + block_x / 2,  map[start][4][1],  start_z, 0, 1)

        current_pose = dType.GetPose(api)
        dType.SetPTPCmdEx(api, 2, map[end][4][0] + block_x / 2,  map[end][4][1] + block_y,  start_z, current_pose[3], 1) 
    elif (aligment == 2): #vertical

        dType.SetPTPCmdEx(api, 0, map[start][4][0],  map[start][4][1] + block_y / 2,  start_z, 0, 1)

        current_pose = dType.GetPose(api)
        dType.SetPTPCmdEx(api, 2, map[end][4][0] + block_x,  map[end][4][1] + block_y / 2,  start_z, current_pose[3], 1)
    elif (aligment == 3): #skos

        dType.SetPTPCmdEx(api, 0, map[start][4][0],  map[start][4][1],  start_z, 0, 1)

        current_pose = dType.GetPose(api)
        dType.SetPTPCmdEx(api, 2, map[end][4][0] + block_x,  map[end][4][1] + block_y,  start_z, current_pose[3], 1)


def win_check():
    global map, who_win

    #horizontal win for player 1
    if (map[0][0] == 1 and map[1][3] == 1 and map[2][3] == 1): #start - 0, end - 2
        who_win = 1

        draw_win(1,0,2)

        return 322
    if (map[3][3] == 1 and map[4][3] == 1 and map[5][3] == 1): #start - 3, end - 5
        who_win = 1

        draw_win(1,3,5)

        return 322
    if (map[6][3] == 1 and map[7][3] == 1 and map[8][3] == 1): #start - 6, end - 8
        who_win = 1

        draw_win(1,6,8)

        return 322
    
    #vertical win for player 1
    if (map[0][3] == 1 and map[3][3] == 1 and map[6][3] == 1): #start - 0, end - 6
        who_win = 1

        draw_win(2,0,6)

        return 322
    if (map[1][3] == 1 and map[4][3] == 1 and map[7][3] == 1): #start - 1, end - 7
        who_win = 1

        draw_win(2,1,7)

        return 322
    if (map[2][3] == 1 and map[5][3] == 1 and map[8][3] == 1): #start - 2, end - 8
        who_win = 1

        draw_win(2,2,8)

        return 322
    
    #skos win for player 1
    if (map[0][3] == 1 and map[4][3] == 1 and map[8][3] == 1): #start - 0, end - 8
        who_win = 1

        dType.SetPTPCmdEx(api, 0, map[0][4][0],  map[0][4][1],  start_z, 0, 1)

        current_pose = dType.GetPose(api)
        dType.SetPTPCmdEx(api, 2, map[8][4][0] + block_x,  map[8][4][1] + block_y,  start_z, current_pose[3], 1)

        return 322
    if (map[2][3] == 1 and map[4][3] == 1 and map[6][3] == 1): #start - 2, end - 6
        who_win = 1

        dType.SetPTPCmdEx(api, 0, map[2][4][0],  map[2][4][1] + block_y,  start_z, 0, 1)

        current_pose = dType.GetPose(api)
        dType.SetPTPCmdEx(api, 2, map[6][4][0] + block_x,  map[6][4][1],  start_z, current_pose[3], 1)

        return 322
    
    #horizontal win for player 2
    if (map[0][3] == 0 and map[1][3] == 0 and map[2][3] == 0): #start - 0, end - 2
        who_win = 0

        draw_win(1,0,2)

        return 322
    if (map[3][3] == 0 and map[4][3] == 0 and map[5][3] == 0): #start - 3, end - 5
        who_win = 0

        draw_win(1,3,5)

        return 322
    if (map[6][3] == 0 and map[7][3] == 0 and map[8][3] == 0): #start - 6, end - 8
        who_win = 0

        draw_win(1,6,8)

        return 322
    
    #vertical win for player 2
    if (map[0][3] == 0 and map[3][3] == 0 and map[6][3] == 0): #start - 0, end - 6
        who_win = 0

        draw_win(2,0,6)

        return 322
    if (map[1][3] == 0 and map[4][3] == 0 and map[7][3] == 0): #start - 1, end - 7
        who_win = 0

        draw_win(2,1,7)

        return 322
    if (map[2][3] == 0 and map[5][3] == 0 and map[8][3] == 0): #start - 2, end - 8
        who_win = 0

        draw_win(2,2,8)

        return 322
    
    #skos win for player 2
    if (map[0][3] == 0 and map[4][3] == 0 and map[8][3] == 0): #start - 0, end - 8
        who_win = 0

        dType.SetPTPCmdEx(api, 0, map[0][4][0],  map[0][4][1],  start_z, 0, 1)

        current_pose = dType.GetPose(api)
        dType.SetPTPCmdEx(api, 2, map[8][4][0] + block_x,  map[8][4][1] + block_y,  start_z, current_pose[3], 1)

        return 322
    if (map[2][3] == 0 and map[4][3] == 0 and map[6][3] == 0): #start - 2, end - 6
        who_win = 0

        dType.SetPTPCmdEx(api, 0, map[2][4][0],  map[2][4][1] + block_y,  start_z, 0, 1)

        current_pose = dType.GetPose(api)
        dType.SetPTPCmdEx(api, 2, map[6][4][0] + block_x,  map[6][4][1],  start_z, current_pose[3], 1)

        return 322
    
    #dubt
    if (map[0][2] == 1 and map[1][2] == 1 and map[2][2] == 1 and map[3][2] == 1 and map[4][2] == 1 and map[5][2] == 1 and map[6][2] == 1 and map[7][2] == 1 and map[8][2] == 1):
        return 404
    
    return 0

def game():
    global map, who_win

    cort_coord()

    while (True):
        choose_mode()

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
        
#if (state == dType.DobotConnect.DobotConnect_NoError):
game()
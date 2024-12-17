from tkinter import *
from tkinter import ttk
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

blocks = 0

map = []

hor_wins = []
ver_wins = []
skos_wins = []

#Заполнение массивов выигрышными комбинациями
def win_arrays(blocks):
    global hor_wins, ver_wins, skos_wins
    hor = ver = skos = 0

    for i in range(blocks):
        count = []
        hor_wins.append(count)
        for j in range(blocks):
            timemap = []
            timemap.append(i + 1)
            timemap.append(j + 1)
            timemap.append(hor)
            hor_wins[i].append(timemap)
            hor += 1

    for i in range(blocks):
        ver = i
        count = []
        ver_wins.append(count)
        for j in range(blocks):
            timemap = []
            timemap.append(j + 1)
            timemap.append(i + 1)
            timemap.append(ver)
            ver_wins[i].append(timemap)
            ver += blocks

    for i in range(1):
        count = []
        skos_wins.append(count)
        for j in range(blocks):
            timemap = []
            timemap.append(j + 1)
            timemap.append(j + 1)
            timemap.append(skos)
            skos_wins[i].append(timemap)
            skos += blocks + 1

    
        skos = blocks - 1
        count = []
        skos_wins.append(count)
        sks = 1
        for j in reversed(range(blocks)):
            timemap = []
            timemap.append(j + 1)
            timemap.append(sks)
            timemap.append(skos)
            skos_wins[i + 1].append(timemap)
            skos += blocks - 1

    print(hor_wins)
    print(ver_wins)
    print(skos_wins)

#Функция выбора режима игры
def choose_mode():
    while (True):
        mode = input('Input game mode do you choose ("player" or "comp")').lower()
        if (mode != 'player' or mode != 'comp'):
            print('Choose right game mode!')

#Заполнение массивов координатами блоков
def cort_coord():
    global blocks, size_cort_x, size_cort_y, center_x, center_y, start_z, block_x, block_y, map
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

    print(map)

    draw_pole(start_x, start_y)

    draw_blocks()

#Отрисовка поля на доботе
def draw_pole(start_x, start_y):
    global blocks, size_cort_x, size_cort_y, center_x, center_y, start_z, block_x, block_y, map

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

#Отрисовка блоков на доботе 
def draw_blocks():
    global blocks, size_cort_x, size_cort_y, center_x, center_y, start_z, block_x, block_y, map

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

#Выбор символа игрока
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

#Отрисовка того или иного символа на поле
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

#Функция хода
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
                row = rand.randint(1,blocks)
                column = rand.randint(1,blocks)
        

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

#Уведомление о выигравшем игроке
def win_print(player_symbol):
    if (player_symbol == 1):
        print("Player 1 Win!")
    elif (player_symbol == 0):
        print("Player 2 Win")

#Зачеркивание победной комбинации на доботе
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

#Проверка победных условий
def loop_check(arr_wins, alligment):
    global map, who_win

    for i in range(len(arr_wins)):
        start = end = check1 = check2 = 0

        for j in range(len(arr_wins[i])):
            if (map[arr_wins[i][j][2]][3] == 1):
                check1 += 1
            if (map[arr_wins[i][j][2]][3] == 0):
                check2 += 1
            if (j == 0):
                start = arr_wins[i][j][2]
            end = arr_wins[i][j][2]
        
        if (check1 == blocks):
            who_win = 1
            draw_win(alligment,start,end)
            return 322
        
        if (check1 == blocks):
            who_win = 0
            draw_win(alligment,start,end)
            return 322

#Проверка победных условий для всех масивов
def win_check():
    global map, who_win, player1_turn, player2_turn, hor_wins, ver_wins, skos_wins, blocks

    #horizontal check for player1 and player2
    loop_check(hor_wins, 1)
        
    #vertical check for player1 and player2
    loop_check(ver_wins, 2)

    #skos check for player1 and player2
    loop_check(skos_wins, 3)
    
    #dubt
    #if (map[0][2] == 1 and map[1][2] == 1 and map[2][2] == 1 and map[3][2] == 1 and map[4][2] == 1 and map[5][2] == 1 and map[6][2] == 1 and map[7][2] == 1 and map[8][2] == 1):
    #    return 404
    
    if ((blocks * blocks) == (player1_turn + player2_turn)):
        return 404
    
    return 0

#Основная функция игры
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
#game()











#Начало программы с интерфейсом
root = 0

# Запуск основной программы
def main_gui():
    global root
    root = Tk()
    root.title("X0X")
    root.geometry("250x150")

    main_buttons()

    root.mainloop()

# ручное закрытие окна и всего приложения
def exit():
    root.destroy()  
    print("Закрытие приложения")

# создание окна таблицы лидеров
def new_game():
    new_game_window = Tk()
    new_game_window.title("Настройки игры")
    new_game_window.geometry("300x150")

    new_game_buttons(new_game_window)

# Создание кнопок для выбора режима
def new_game_buttons(new_game_window):
    label_new_game = ttk.Label(master=new_game_window, text="Выберете режим игры: ")
    label_new_game.pack()

    btn_start_classic = ttk.Button(master=new_game_window, text="Игрок против игрока", command=lambda: start_game(btn_start_classic, label_new_game, btn_start_pc_mode, btn_start_pc_vs_pc_mode, btn_start_dobot_vs_dobot_mode, new_game_window, "player"))
    btn_start_classic.pack()

    btn_start_pc_mode = ttk.Button(master=new_game_window, text="Игрок против компьютера", command=lambda: start_game(btn_start_classic, label_new_game, btn_start_pc_mode, btn_start_pc_vs_pc_mode, btn_start_dobot_vs_dobot_mode, new_game_window, "comp"))
    btn_start_pc_mode.pack()

    btn_start_pc_vs_pc_mode = ttk.Button(master=new_game_window, text="Компьютер против компьютера", command=lambda: start_game(btn_start_classic, label_new_game, btn_start_pc_mode, btn_start_pc_vs_pc_mode, btn_start_dobot_vs_dobot_mode, new_game_window, "compvs"))
    btn_start_pc_vs_pc_mode.pack()

    btn_start_dobot_vs_dobot_mode = ttk.Button(master=new_game_window, text="Добот против Добота", command=lambda: start_game(btn_start_classic, label_new_game, btn_start_pc_mode, btn_start_pc_vs_pc_mode, btn_start_dobot_vs_dobot_mode, new_game_window, "dobotonly"))
    btn_start_dobot_vs_dobot_mode.pack()

# Функция выбора режима
def start_game(*args):
    args = list(args)
    mode = args[-1]
    args.remove(args[-1])
    new_game_window = args[-1]
    args.remove(args[-1])
    args = tuple(args)

    print(args)

    for element in args:
        element.destroy()

    new_game_window.geometry("400x250")
    new_game_inputs(new_game_window)

# Функция ввода размеров поля для игры
def new_game_inputs(new_game_window):
    label_new_game_input = ttk.Label(master=new_game_window, text="Введите ширину и высоту игрового поля в точках: ")
    label_new_game_input.pack()

    label_width_input = ttk.Label(master=new_game_window, text="Ширина: ")
    label_width_input.pack()
    width_input = ttk.Entry(master=new_game_window)
    width_input.pack(anchor=CENTER, padx=6, pady=6) 

    label_height_input = ttk.Label(master=new_game_window, text="Высота: ")
    label_height_input.pack()
    height_input = ttk.Entry(master=new_game_window)
    height_input.pack(anchor=CENTER, padx=6, pady=6)  

    label_blocks_input = ttk.Label(master=new_game_window, text="Введите размерность сетки (кол-во блоков): ")
    label_blocks_input.pack()
    blocks_input = ttk.Entry(master=new_game_window)
    blocks_input.pack(anchor=CENTER, padx=6, pady=6)   

    btn_new_game_inputs_apply = ttk.Button(master=new_game_window, text="Начать игру", command=lambda: new_game_apply(width_input, height_input, blocks_input, btn_new_game_inputs_apply, label_blocks_input, label_height_input, label_width_input, label_new_game_input, new_game_window))
    btn_new_game_inputs_apply.pack()

#Форма для ввода основных характеристик окна и поля
def new_game_apply(*args):
    if len(args[0].get()) == 0 or len(args[0].get()) == 0 or len(args[0].get()) == 0:
        print("Input all numbers")
    else:
        size_cort_x = int(args[0].get())
        size_cort_y = int(args[1].get())
        blocks = int(args[2].get())

        if ((size_cort_x != 0 or size_cort_x > 0) and (size_cort_y != 0 or size_cort_y > 0) and (blocks > 2)):
            args[-1].geometry("600x600")

            args = list(args)
            window = args[-1]
            args.pop()
            args = tuple(args)
            
            for element in args:
                element.destroy()

            create_game_elements(window, blocks)

        else:
            print(size_cort_x, size_cort_y, blocks)
            print("Wrong input's")

#Создание основного экрана игры
def create_game_elements(window, blocks):
    game_frame = ttk.Frame(window, borderwidth=1, relief=SOLID)
    game_frame.place(relx=0.025, rely=0.025, relheight=0.95, relwidth=0.7)

    statistic_frame = ttk.Frame(window, borderwidth=1, relief=SOLID)
    statistic_frame.place(relx=0.775, rely=0.025, relheight=0.95, relwidth=0.2)

    listbox_statistic = Listbox(master=statistic_frame, bg="white", fg="black")
    listbox_statistic.insert(1, "Python")
    listbox_statistic.place(relx=0.025, rely=0.005, relheight=0.99, relwidth=0.95)

    block_space = 0.003
    block_width = (1 -  (blocks * block_space)) / blocks
    block_height = (1 -  (blocks * block_space)) / blocks

    if mode == "player":
        win_arrays(blocks)

    print(block_height, block_width)
    
    for i in range(blocks):
        block_space_x = block_space + (block_height * i) + (block_space * i)
        for j in range(blocks):
            block_space_y = block_space + (block_width * j) + (block_space * j)
            btn_cell = ttk.Button(master=game_frame, text=f"")
            btn_cell.place(relx=block_space_x, rely=block_space_y, relheight=block_height, relwidth=block_width)
            btn_cell.update()
            print('Frame: ', game_frame.winfo_width(), game_frame.winfo_height())
            print("button created ", i, btn_cell.winfo_width(), btn_cell.winfo_height())



# создание окна таблицы лидеров
def open_bord():
    bord_window = Tk()
    bord_window.title("Таблица лидеров")
    bord_window.geometry("900x350")
    
    leaderbord(bord_window)

# Таблица лидеров
def leaderbord(bord_window):
    # определяем данные для отображения
    people = [("Tom", 38, 12, 38/100*12), ("Bob", 42, 3, 42/100*3), ("Sam", 28, 24, 28/100*24)]
    
    # определяем столбцы
    columns = ("name", "games", "wins", "percent")
    
    tree = ttk.Treeview(columns=columns, show="headings", master=bord_window)
    tree.pack(fill=BOTH, expand=1)
    
    # определяем заголовки
    tree.heading("name", text="Имя")
    tree.heading("games", text="Игры")
    tree.heading("wins", text="Победы")
    tree.heading("percent", text="Процент побед")
    
    # добавляем данные
    for person in people:
        tree.insert("", END, values=person)

# Создание кнопок для главного окна
def main_buttons():
    btn_start = ttk.Button(master=root, text="Начать игру", command=new_game)
    btn_start.pack()

    btn_bord = ttk.Button(master=root, text="Таблица лидеров", command=open_bord)
    btn_bord.pack()

    btn_callibrate = ttk.Button(master=root, text="Калибровка")
    btn_callibrate.pack()

    btn_exit = ttk.Button(master=root, text="Выход", command=exit)
    btn_exit.pack()

main_gui()
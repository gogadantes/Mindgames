from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
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

game_buttons = []

player1_name = "Игрок X"
player2_name = "Игрок O"

def save_game_result_to_file(winner):
    """Сохраняет результат игры в файл."""
    import datetime
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("leaderboard.txt", "a", encoding="utf-8") as f:
        if winner == "draw":
            f.write(f"{now},Ничья\n")
        else:
            name = player1_name if winner == "X" else player2_name
            f.write(f"{now},{name}\n")

#Заполнение массивов выигрышными комбинациями
def win_arrays(blocks):
    global hor_wins, ver_wins, skos_wins
    hor_wins.clear()
    ver_wins.clear()
    skos_wins.clear()

    # Горизонтальные линии
    for i in range(blocks):
        row = []
        for j in range(blocks):
            index = i * blocks + j
            row.append([i + 1, j + 1, index])
        hor_wins.append(row)

    # Вертикальные линии
    for j in range(blocks):
        col = []
        for i in range(blocks):
            index = i * blocks + j
            col.append([i + 1, j + 1, index])
        ver_wins.append(col)

    # Диагональ слева направо
    diag1 = []
    for i in range(blocks):
        index = i * blocks + i
        diag1.append([i + 1, i + 1, index])
    skos_wins.append(diag1)

    # Диагональ справа налево
    diag2 = []
    for i in range(blocks):
        index = i * blocks + (blocks - i - 1)
        diag2.append([i + 1, blocks - i, index])
    skos_wins.append(diag2)

#Функция выбора режима игры
def choose_mode():
    global mode
    return [1, 0]  # Игрок 1 — 'X', Игрок 2 — 'O'

#Заполнение массивов координатами блоков
def cort_coord(size_cort_x, size_cort_y, blocks):
    global center_x, center_y, start_z, block_x, block_y, map
    map.clear()
    count = 0

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

    #draw_pole(start_x, start_y)

    #draw_blocks()

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
        

        row = rand.randint(1, blocks)
        column = rand.randint(1, blocks)

        for i in range(len(map)):
            if map[i][0] == row and map[i][1] == column and map[i][2] == 0:
                map[i][2] = 1
                map[i][3] = player_symbol
                if player_symbol == 1:
                    player1_turn += 1
                else:
                    player2_turn += 1
                #draw_symbol(player_symbol, i)
                return
        # Если выбранный ход занят, рекурсивно попробуем ещё раз
        turn(player_symbol)

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
def loop_check(arr_wins, alignment):
    global map, who_win, blocks
    print("[DEBUG] loop_check: blocks =", blocks)

    for i in range(len(arr_wins)):
        start = end = check1 = check2 = 0

        for j in range(len(arr_wins[i])):
            cell_index = arr_wins[i][j][2]
            if map[cell_index][2] == 1:  # только если клетка занята
                if map[cell_index][3] == 1:
                    check1 += 1
                elif map[cell_index][3] == 0:
                    check2 += 1
            if j == 0:
                start = cell_index
            end = cell_index

        if check1 == blocks:
            who_win = 1
            #draw_win(alignment, start, end)
            return 322

        if check2 == blocks:
            who_win = 0
            #draw_win(alignment, start, end)
            return 322

    return 0

#Проверка победных условий для всех масивов
def win_check():
    global map, who_win, player1_turn, player2_turn, hor_wins, ver_wins, skos_wins, blocks

    print("map:")
    for i, cell in enumerate(map):
        print(i, cell)

    #horizontal check for player1 and player2
    result = loop_check(hor_wins, 1)
    print("horizontal check result:", result)
    if result:
        return result
        
    #vertical check for player1 and player2
    result = loop_check(ver_wins, 2)
    print("vertical check result:", result)
    if result:
        return result

    #skos check for player1 and player2
    result = loop_check(skos_wins, 3)
    print("skos check result:", result)
    if result:
        return result
    
    #dubt
    if (player1_turn + player2_turn) >= (blocks * blocks):
        return 404
    
    if ((blocks * blocks) == (player1_turn + player2_turn)):
        return 404
    
    return 0

#Основная функция игры
def game():
    global map, who_win

    cort_coord()

    while (True):
        #choose_mode() # отключено, чтобы не запрашивать режим через консоль

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

    # Скрытые поля ввода ширины и высоты
    width_label = ttk.Label(master=new_game_window, text="Ширина: ")
    width_input = ttk.Entry(master=new_game_window)
    height_label = ttk.Label(master=new_game_window, text="Высота: ")
    height_input = ttk.Entry(master=new_game_window)

    blocks_label = ttk.Label(master=new_game_window, text="Введите размерность сетки (кол-во блоков): ")
    blocks_input = ttk.Entry(master=new_game_window)

    def start_game_mode(mode, with_dobot):
        for widget in new_game_window.winfo_children():
            widget.destroy()

        width_label = ttk.Label(master=new_game_window, text="Ширина: ")
        width_input = ttk.Entry(master=new_game_window)
        height_label = ttk.Label(master=new_game_window, text="Высота: ")
        height_input = ttk.Entry(master=new_game_window)
        blocks_label = ttk.Label(master=new_game_window, text="Введите размерность сетки (кол-во блоков): ")
        blocks_input = ttk.Entry(master=new_game_window)

        # Показывать поля ширины и высоты только если с доботом
        if with_dobot:
            width_label.pack()
            width_input.pack(anchor="center", padx=6, pady=6)
            height_label.pack()
            height_input.pack(anchor="center", padx=6, pady=6)

        blocks_label.pack()
        blocks_input.pack(anchor="center", padx=6, pady=6)

        btn_start = ttk.Button(master=new_game_window, text="Начать игру",
                               command=lambda: new_game_apply(
                                   width_input, height_input, blocks_input, btn_start,
                                   blocks_label, height_label, width_label, label_new_game, new_game_window,
                                   mode, with_dobot))
        btn_start.pack(pady=10)

    btn_player_only = ttk.Button(master=new_game_window, text="Игрок против игрока (только компьютер)",
                                 command=lambda: start_game_mode("player", False))
    btn_player_only.pack(fill='x', padx=10, pady=3)

    btn_player_dobot = ttk.Button(master=new_game_window, text="Игрок против игрока (компьютер + добот)",
                                 command=lambda: start_game_mode("player", True))
    btn_player_dobot.pack(fill='x', padx=10, pady=3)

    btn_comp_only = ttk.Button(master=new_game_window, text="Игрок против компьютера (только компьютер)",
                               command=lambda: start_game_mode("comp", False))
    btn_comp_only.pack(fill='x', padx=10, pady=3)

    btn_comp_dobot = ttk.Button(master=new_game_window, text="Игрок против компьютера (компьютер + добот)",
                               command=lambda: start_game_mode("comp", True))
    btn_comp_dobot.pack(fill='x', padx=10, pady=3)

    btn_comp_vs_comp = ttk.Button(master=new_game_window, text="Компьютер против компьютера (только компьютер)",
                                 command=lambda: start_game_mode("compvs", False))
    btn_comp_vs_comp.pack(fill='x', padx=10, pady=3)

    btn_comp_vs_comp_dobot = ttk.Button(master=new_game_window, text="Компьютер против компьютера (компьютер + добот)",
                                       command=lambda: start_game_mode("compvs", True))
    btn_comp_vs_comp_dobot.pack(fill='x', padx=10, pady=3)

    btn_dobot_vs_dobot = ttk.Button(master=new_game_window, text="Добот против Добота",
                                   command=lambda: start_game_mode("dobotonly", True))
    btn_dobot_vs_dobot.pack(fill='x', padx=10, pady=3)

    adjust_window_size(new_game_window)

# Функция выбора режима
def start_game(*args):
    global mode
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
def new_game_apply(width_input, height_input, blocks_input, btn_apply,
                   label_blocks, label_height, label_width, label_new_game_input,
                   new_game_window, mode, with_dobot):
    global blocks, size_cort_x, size_cort_y, map, hor_wins, ver_wins, skos_wins, player1_turn, player2_turn, mode_global, with_dobot_global

    try:
        blocks = int(blocks_input.get())
        print("[DEBUG] blocks set to", blocks)
        if with_dobot:
            size_cort_x = int(width_input.get())
            size_cort_y = int(height_input.get())
        else:
            size_cort_x = 0
            size_cort_y = 0
    except ValueError:
        print("Введите корректные числа")
        return

    if blocks > 2 and (not with_dobot or (size_cort_x > 0 and size_cort_y > 0)):
        global map, hor_wins, ver_wins, skos_wins, player1_turn, player2_turn, mode_global, with_dobot_global, player1_name, player2_name

        map.clear()
        hor_wins.clear()
        ver_wins.clear()
        skos_wins.clear()

        player1_turn = 0
        player2_turn = 0

        if mode == "player":
            player1_name = simpledialog.askstring("Имя игрока 1", "Введите имя игрока X:", parent=new_game_window) or "Игрок X"
            player2_name = simpledialog.askstring("Имя игрока 2", "Введите имя игрока O:", parent=new_game_window) or "Игрок O"
        elif mode == "comp":
            player1_name = simpledialog.askstring("Имя игрока", "Введите имя игрока:", parent=new_game_window) or "Игрок"
            player2_name = "ComputerAI_1"
        elif mode == "compvs":
            player1_name = "ComputerAI_1"
            player2_name = "ComputerAI_2"
        elif mode == "dobotonly":
            player1_name = "ComputerAI_1"
            player2_name = "ComputerAI_2"
        else:
            player1_name = "Игрок X"
            player2_name = "Игрок O"

        mode_global = mode
        with_dobot_global = with_dobot

        win_arrays(blocks)

        if with_dobot:
            cort_coord(size_cort_x, size_cort_y, blocks)
        else:
            # Инициализируем map без координат для добота
            # Можно сделать пустые координаты или нули
            block_x = 0
            block_y = 0
            map.clear()
            for i in range(blocks):
                for j in range(blocks):
                    map.append([i + 1, j + 1, 0, 5, [0,0]])

        new_game_window.geometry("600x600")

        for w in [btn_apply, label_blocks, label_height, label_width,
          label_new_game_input, width_input, height_input, blocks_input]:
            if w.winfo_exists():
                w.destroy()

        create_game_elements(new_game_window, blocks)
    else:
        print("Неверные параметры")

#Создание основного экрана игры
def create_game_elements(window, blocks):
    global listbox_statistic
    game_frame = ttk.Frame(window, borderwidth=1, relief=SOLID)
    game_frame.place(relx=0.025, rely=0.025, relheight=0.95, relwidth=0.7)

    statistic_frame = ttk.Frame(window, borderwidth=1, relief=SOLID)
    statistic_frame.place(relx=0.775, rely=0.025, relheight=0.95, relwidth=0.2)

    listbox_statistic = Listbox(master=statistic_frame, bg="white", fg="black")
    listbox_statistic.place(relx=0.025, rely=0.005, relheight=0.99, relwidth=0.95)

    block_space = 0.003
    block_width = (1 -  (blocks * block_space)) / blocks
    block_height = (1 -  (blocks * block_space)) / blocks

    if mode == "player":
        win_arrays(blocks)

    print(block_height, block_width)
    
    local_style = ttk.Style(game_frame)
    local_style.configure("X.TButton",
                      foreground="#00BFFF",
                      font=("Helvetica", 20, "bold"))
    local_style.configure("O.TButton",
                        foreground="#FF6347",
                        font=("Helvetica", 20, "bold"))
    local_style.theme_use('clam')
    local_style.configure("Tile.TButton",
                font=("Helvetica", 20, "bold"),
                padding=10,
                background="#5C5C6A",
                foreground="white",
                relief="flat")
    local_style.map("Tile.TButton",
                background=[("active", "#6E6E80"), ("disabled", "#3A3A48")],
                foreground=[("disabled", "#AAAAAA")])
    local_style.configure("Win.TButton",
                      background="#FFD700",
                      font=("Helvetica", 20, "bold"))
    
    def update_game_state(i, j, btn_ref):
        #"""Обновляет состояние игры в зависимости от выбранного режима.

        #Поддерживаемые режимы (mode_global задаётся в new_game_apply):
        #- 'player'      : игрок против игрока
        #- 'comp'        : игрок против компьютера (рандомный ход)
        #- 'compvs'      : компьютер против компьютера
        #- 'dobotonly'   : добот против добота (пока логика та же, что и compvs)
        #"""
        if mode_global == "player":
            _handle_player_vs_player(i, j, btn_ref)

        elif mode_global == "comp":
            _handle_player_vs_computer(i, j, btn_ref)

        elif mode_global in ("compvs", "dobotonly"):
            # автоматическая партия (запускается один-раз при первом клике)
            if not hasattr(update_game_state, "_auto_started"):
                update_game_state._auto_started = True
                _run_auto_game()
        else:
            print("[ERROR] Unknown mode:", mode_global)

    # ------------------------------------------------------------------ #
    # ----------  ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ДЛЯ РАЗНЫХ РЕЖИМОВ  ----------- #
    # ------------------------------------------------------------------ #

    def _apply_move(i, j, btn_ref, force_symbol=None):
        """Выполняет ход, обновляет UI и проверяет победу.
        Возвращает True, если партия завершилась (победа/ничья)."""
        global map, player1_turn, player2_turn

        # если координаты неверные – игнорируем вызов
        index = next((idx for idx, cell in enumerate(map)
                      if cell[0] == i + 1 and cell[1] == j + 1), None)
        if index is None or map[index][2] == 1:
            return False  # клетка занята или не найдена

        # определяем, чей сейчас символ
        if force_symbol is None:
            symbol = "X" if (player1_turn + player2_turn) % 2 == 0 else "O"
        else:
            symbol = force_symbol
        player_symbol = 1 if symbol == "X" else 0

        # фиксируем ход в модели
        map[index][2] = 1
        map[index][3] = player_symbol

        if player_symbol == 1:
            player1_turn += 1
            btn_ref.configure(style="X.TButton")
        else:
            player2_turn += 1
            btn_ref.configure(style="O.TButton")

        # обновляем GUI
        btn_ref["text"] = symbol
        btn_ref["state"] = "disabled"
        listbox_statistic.insert(
            END, f"Ход {player1_turn + player2_turn}: {symbol} → ({i + 1}, {j + 1})")
        listbox_statistic.yview(END)

        # проверяем результат игры
        result = win_check()
        if result == 322:
            win_print(player_symbol)
            animate_win()
            disable_all_buttons()
            show_game_result(symbol, btn_ref.winfo_toplevel())
            return True
        elif result == 404:
            print("Ничья!")
            disable_all_buttons()
            show_game_result("draw", btn_ref.winfo_toplevel())
            return True
        return False

    # ---------- режим «игрок vs игрок» ----------
    def _handle_player_vs_player(i, j, btn_ref):
        _apply_move(i, j, btn_ref)

    # ---------- режим «игрок vs компьютер» ----------
    def _computer_smart_move():
        """Улучшенный ИИ: пытается выиграть или блокировать игрока."""
        # 1. Попробовать выиграть самому
        for idx, cell in enumerate(map):
            if cell[2] == 0:
                cell[2] = 1
                cell[3] = 0  # Компьютер — 'O'
                if win_check() == 322:
                    i, j = cell[0] - 1, cell[1] - 1
                    btn_ref = next(btn for bi, bj, btn in game_buttons if bi == i and bj == j)
                    _apply_move(i, j, btn_ref, force_symbol="O")
                    return
                cell[2] = 0
                cell[3] = 5

        # 2. Попробовать заблокировать игрока
        for idx, cell in enumerate(map):
            if cell[2] == 0:
                cell[2] = 1
                cell[3] = 1  # Игрок — 'X'
                if win_check() == 322:
                    cell[2] = 0
                    cell[3] = 5
                    i, j = cell[0] - 1, cell[1] - 1
                    btn_ref = next(btn for bi, bj, btn in game_buttons if bi == i and bj == j)
                    _apply_move(i, j, btn_ref, force_symbol="O")
                    return
                cell[2] = 0
                cell[3] = 5

        # 3. Центр, если свободен
        center = blocks // 2
        for i in range(blocks):
            for j in range(blocks):
                if i == center and j == center:
                    index = next((idx for idx, cell in enumerate(map)
                                if cell[0] == i + 1 and cell[1] == j + 1), None)
                    if index is not None and map[index][2] == 0:
                        btn_ref = next(btn for bi, bj, btn in game_buttons if bi == i and bj == j)
                        _apply_move(i, j, btn_ref, force_symbol="O")
                        return

        # 4. Иначе — случайный ход
        free_cells = [(idx, cell) for idx, cell in enumerate(map) if cell[2] == 0]
        if not free_cells:
            return
        idx, cell = rand.choice(free_cells)
        i, j = cell[0] - 1, cell[1] - 1
        btn_ref = next(btn for bi, bj, btn in game_buttons if bi == i and bj == j)
        _apply_move(i, j, btn_ref, force_symbol="O")

    def _handle_player_vs_computer(i, j, btn_ref):
        game_ended = _apply_move(i, j, btn_ref)  # ход игрока
        if not game_ended:
            _computer_smart_move()              # ход компьютера

    # ---------- режимы «компьютер vs компьютер» и «добот vs добот» ----------
    def _run_auto_game():
        """Запускает автоматическую партию до завершения."""
        while True:
            _computer_smart_move()
            window.update()  # обновляем интерфейс
            if win_check() in (322, 404):
                break

    for i in range(blocks):
        block_space_x = block_space + (block_height * i) + (block_space * i)
        for j in range(blocks):
            block_space_y = block_space + (block_width * j) + (block_space * j)
            # btn_cell = ttk.Button(master=game_frame, text=f"")
            # btn_cell.place(relx=block_space_x, rely=block_space_y, relheight=block_height, relwidth=block_width)
            # btn_cell.update()
            # print('Frame: ', game_frame.winfo_width(), game_frame.winfo_height())
            # print("button created ", i, btn_cell.winfo_width(), btn_cell.winfo_height())

            def make_button_command(x, y, btn_ref):
                def on_click():
                    update_game_state(x, y, btn_ref)
                return on_click

            btn_cell = ttk.Button(master=game_frame, text="", style="Tile.TButton")
            btn_cell.place(relx=block_space_y, rely=block_space_x, relheight=block_height, relwidth=block_width)
            btn_cell["command"] = make_button_command(i, j, btn_cell)
            game_buttons.append((i, j, btn_cell))

    def disable_all_buttons():
        for _, _, btn in game_buttons:
            btn["state"] = "disabled"

    def animate_win():
        for _ in range(6):
            for i, j, btn in game_buttons:
                btn.after(100)
                btn.configure(style="Win.TButton")
            window.update()
            for i, j, btn in game_buttons:
                btn.after(100)
                btn.configure(style="Tile.TButton")
            window.update()



# создание окна таблицы лидеров
def open_bord():
    bord_window = Tk()
    bord_window.title("Таблица лидеров")
    bord_window.geometry("900x350")
    
    leaderbord(bord_window)

# Таблица лидеров
def leaderbord(bord_window):
    # определяем данные для отображения
    import collections

    people = []
    win_counter = collections.Counter()
    total_counter = collections.Counter()

    try:
        with open("leaderboard.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    _, result = parts
                    if result not in ("Ничья", "draw"):
                        win_counter[result] += 1
                    total_counter[result] += 1
    except FileNotFoundError:
        pass

    for name in total_counter:
        total = total_counter[name]
        wins = win_counter.get(name, 0)
        percent = (wins / total) * 100 if total else 0
        people.append((name, total, wins, round(percent, 2)))
    
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

#Окно после победы
def show_game_result(winner, game_window):
    save_game_result_to_file(winner)

    result_window = Toplevel()
    result_window.title("Результат игры")
    result_window.geometry("300x150")
    result_window.grab_set()

    if winner == "draw":
        message = "Ничья!"
    elif winner == "X":
        message = "Победил игрок X!"
    elif winner == "O":
        message = "Победил игрок O!"
    else:
        message = "Игра завершена"

    label = ttk.Label(result_window, text=message, font=("Helvetica", 14))
    label.pack(pady=20)

    btn_menu = ttk.Button(result_window, text="В меню", command=lambda: (game_window.destroy(), result_window.destroy(), root.deiconify()))
    btn_menu.pack(pady=5)

    btn_exit = ttk.Button(result_window, text="Выход", command=root.quit)
    btn_exit.pack(pady=5)

def adjust_window_size(window):
    window.update_idletasks()
    width = window.winfo_reqwidth() + 20
    height = window.winfo_reqheight() + 20
    window.geometry(f"{width}x{height}")

main_gui()
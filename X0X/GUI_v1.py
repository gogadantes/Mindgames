from tkinter import *
from tkinter import ttk

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

    btn_start_classic = ttk.Button(master=new_game_window, text="Игрок против игрока", command=lambda: start_game(btn_start_classic, label_new_game, btn_start_pc_mode, new_game_window, "player"))
    btn_start_classic.pack()

    btn_start_pc_mode = ttk.Button(master=new_game_window, text="Игрок против компьютера", command=lambda: start_game(btn_start_classic, label_new_game, btn_start_pc_mode, new_game_window, "comp"))
    btn_start_pc_mode.pack()

# Функция выбора режима
def start_game(*args):
    args = list(args)
    mode = args[-1]
    args.remove(args[-1])
    new_game_window = args[-1]
    args.remove(args[-1])
    args = tuple(args)

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
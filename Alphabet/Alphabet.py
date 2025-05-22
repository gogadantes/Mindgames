import threading
import DobotDllType as dType
import random as rand
import math

def get_rotation():
    return dType.GetPose(api)[3]

def dobot_connect():
    CON_STR = {
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
    dType.SetPTPJumpParamsEx(api,50,100,1)

    return api

api = dobot_connect()

#English

def us_symbol_A(start_x, start_y, start_z, x, y):
    print(x, y)
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x * 0.75),  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.25),  start_y + (y / 2),  start_z, current_pose[3], 1)

def us_symbol_B(x, y, z, width, height, segments=15):
    r = get_rotation()
    h_half = height / 2

    # Вертикальная линия
    dType.SetPTPCmdEx(api, 0, x, y, z, r, 1)
    dType.SetPTPCmdEx(api, 2, x, y + height, z, r, 1)

    # Верхняя дуга
    for i in range(segments + 1):
        angle = math.pi * i / segments
        xi = x + width * math.cos(angle)
        yi = y + h_half + width * math.sin(angle)
        dType.SetPTPCmdEx(api, 2, xi, yi, z, r, 1)

    # Нижняя дуга
    for i in range(segments + 1):
        angle = math.pi * i / segments
        xi = x + width * math.cos(angle)
        yi = y + width * math.sin(angle)
        dType.SetPTPCmdEx(api, 2, xi, yi, z, r, 1)

def us_symbol_C(x, y, z, radius, segments=30):
    r = get_rotation()
    for i in range(segments + 1):
        angle = math.pi + (math.pi * i / segments)
        xi = x + radius * math.cos(angle)
        yi = y + radius * math.sin(angle)
        if i == 0:
            dType.SetPTPCmdEx(api, 0, xi, yi, z, r, 1)
        else:
            dType.SetPTPCmdEx(api, 2, xi, yi, z, r, 1)

def us_symbol_D(x, y, z, radius, height, segments=30):
    r = get_rotation()
    dType.SetPTPCmdEx(api, 0, x, y, z, r, 1)
    dType.SetPTPCmdEx(api, 2, x, y + height, z, r, 1)

    for i in range(segments + 1):
        angle = math.pi * i / segments
        xi = x + radius * math.cos(angle)
        yi = y + height / 2 + radius * math.sin(angle)
        dType.SetPTPCmdEx(api, 2, xi, yi, z, r, 1)

    dType.SetPTPCmdEx(api, 2, x, y, z, r, 1)

def us_symbol_E(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def us_symbol_F(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def us_symbol_G(x, y, z, radius, segments=30):
    r = get_rotation()
    for i in range(int(segments * 0.75) + 1):
        angle = math.pi + (1.5 * math.pi * i / segments)
        xi = x + radius * math.cos(angle)
        yi = y + radius * math.sin(angle)
        if i == 0:
            dType.SetPTPCmdEx(api, 0, xi, yi, z, r, 1)
        else:
            dType.SetPTPCmdEx(api, 2, xi, yi, z, r, 1)
    # "Зубчик"
    dType.SetPTPCmdEx(api, 2, x + radius / 2, y, z, r, 1)

def us_symbol_H(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def us_symbol_I(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x / 2),  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + y,  start_z, current_pose[3], 1)

def us_symbol_J(x, y, z, height, radius, segments=15):
    r = get_rotation()
    for i in range(segments + 1):
        angle = math.pi / 2 + math.pi * i / segments
        xi = x + radius * math.cos(angle)
        yi = y + radius * math.sin(angle)
        if i == 0:
            dType.SetPTPCmdEx(api, 0, xi, yi, z, r, 1)
        else:
            dType.SetPTPCmdEx(api, 2, xi, yi, z, r, 1)
    dType.SetPTPCmdEx(api, 2, x + radius, y + height, z, r, 1)

def us_symbol_K(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def us_symbol_L(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def us_symbol_M(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def us_symbol_N(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

def us_symbol_O(x, y, z, radius, segments=36):
    r = get_rotation()
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        xi = x + radius * math.cos(angle)
        yi = y + radius * math.sin(angle)
        if i == 0:
            dType.SetPTPCmdEx(api, 0, xi, yi, z, r, 1)
        else:
            dType.SetPTPCmdEx(api, 2, xi, yi, z, r, 1)

def us_symbol_P(x, y, z, height, radius, segments=15):
    r = get_rotation()
    dType.SetPTPCmdEx(api, 0, x, y, z, r, 1)
    dType.SetPTPCmdEx(api, 2, x, y + height, z, r, 1)
    for i in range(segments + 1):
        angle = math.pi * i / segments
        xi = x + radius * math.cos(angle)
        yi = y + height - radius + radius * math.sin(angle)
        dType.SetPTPCmdEx(api, 2, xi, yi, z, r, 1)

def us_symbol_Q(x, y, z, radius, segments=36):
    r = get_rotation()
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        xi = x + radius * math.cos(angle)
        yi = y + radius * math.sin(angle)
        if i == 0:
            dType.SetPTPCmdEx(api, 0, xi, yi, z, r, 1)
        else:
            dType.SetPTPCmdEx(api, 2, xi, yi, z, r, 1)
    # Хвост
    dType.SetPTPCmdEx(api, 2, x + radius / 2, y + radius / 2, z, r, 1)

def us_symbol_R(x, y, z, height, radius, segments=15):
    r = get_rotation()
    dType.SetPTPCmdEx(api, 0, x, y, z, r, 1)
    dType.SetPTPCmdEx(api, 2, x, y + height, z, r, 1)
    for i in range(segments + 1):
        angle = math.pi * i / segments
        xi = x + radius * math.cos(angle)
        yi = y + height - radius + radius * math.sin(angle)
        dType.SetPTPCmdEx(api, 2, xi, yi, z, r, 1)
    dType.SetPTPCmdEx(api, 2, x + radius, y, z, r, 1)

def us_symbol_S(x, y, z, radius, segments=20):
    r = get_rotation()

    # Верхняя дуга
    for i in range(segments + 1):
        angle = math.pi + (math.pi * i / segments)
        xi = x + radius * math.cos(angle)
        yi = y + 2 * radius + radius * math.sin(angle)
        if i == 0:
            dType.SetPTPCmdEx(api, 0, xi, yi, z, r, 1)
        else:
            dType.SetPTPCmdEx(api, 2, xi, yi, z, r, 1)

    # Нижняя дуга
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        xi = x + radius * math.cos(angle)
        yi = y + radius * math.sin(angle)
        dType.SetPTPCmdEx(api, 2, xi, yi, z, r, 1)

def us_symbol_T(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x / 2),  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y,  start_z, current_pose[3], 1)

def us_symbol_U(x, y, z, height, radius, segments=15):
    r = get_rotation()
    dType.SetPTPCmdEx(api, 0, x, y + height, z, r, 1)
    dType.SetPTPCmdEx(api, 2, x, y + radius, z, r, 1)

    for i in range(segments + 1):
        angle = math.pi + math.pi * i / segments
        xi = x + radius + radius * math.cos(angle)
        yi = y + radius * math.sin(angle)
        dType.SetPTPCmdEx(api, 2, xi, yi, z, r, 1)

    dType.SetPTPCmdEx(api, 2, x + 2 * radius, y + height, z, r, 1)

def us_symbol_V(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)
  
def us_symbol_W(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.25),  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.75),  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

def us_symbol_X(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

def us_symbol_Y(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x / 2),  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + (y / 2),  start_z, current_pose[3], 1)

def us_symbol_Z(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

#Russian

def ru_symbol_A(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x * 0.75),  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.25),  start_y + (y / 2),  start_z, current_pose[3], 1)

def ru_symbol_Be(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def ru_symbol_Ve(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y * 0.75),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y+ (y * 0.5),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y * 0.25),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

def ru_symbol_G(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

def ur_symbol_D(x, y, z, width, height):
    r = get_rotation()

    base_height = height * 0.2  # основание у «Д»
    top_x = x + width / 2
    top_y = y + height

    # 1. Поднимаемся к нижней точке левой вертикали
    dType.SetPTPCmdEx(api, 0, x, y, z, r, 1)

    # 2. Линия к вершине
    dType.SetPTPCmdEx(api, 2, top_x, top_y, z, r, 1)

    # 3. Линия к правой нижней части
    dType.SetPTPCmdEx(api, 2, x + width, y, z, r, 1)

    # 4. Горизонтальная линия основания
    dType.SetPTPCmdEx(api, 2, x + width, y - base_height, z, r, 1)
    dType.SetPTPCmdEx(api, 2, x, y - base_height, z, r, 1)

    # 5. Замыкаем в исходную точку
    dType.SetPTPCmdEx(api, 2, x, y, z, r, 1)

def ru_symbol_D(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y * 0.15,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y * 0.15,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x * 0.15,  start_y + y * 0.15,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x / 2,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x * 0.85,  start_y + y * 0.15,  start_z, current_pose[3], 1)

def ru_symbol_E(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def ru_symbol_Yo(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y * 0.75,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y * 0.75,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y * 0.33),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y * 0.33),  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x * 0.25,  start_y + (y * 0.85),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x * 0.35,  start_y + (y * 0.85),  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x * 0.65,  start_y + (y * 0.85),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x * 0.75,  start_y + (y * 0.85),  start_z, current_pose[3], 1)

def ru_symbol_J(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y / 2,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y / 2,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x / 2,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x / 2,  start_y,  start_z, current_pose[3], 1)

def ru_symbol_Ze(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y * 0.75),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y * 0.5),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y * 0.25),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

def ru_symbol_And(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def ru_symbol_Yi(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y * 0.75,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y * 0.75,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x * 0.25,  start_y + y * 0.85,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x * 0.35,  start_y + y * 0.85,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x * 0.65,  start_y + y * 0.85,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x * 0.75,  start_y + y * 0.85,  start_z, current_pose[3], 1)

def ru_symbol_K(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def ru_symbol_L(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def ru_symbol_M(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def ru_symbol_H(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def ru_symbol_O(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)   
    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

def ru_symbol_P(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def ru_symbol_R(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + (y * 0.75),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y * 0.5),  start_z, current_pose[3], 1)

def ru_symbol_C(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y * 0.75),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y * 0.5),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def ru_symbol_T(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x / 2),  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y,  start_z, current_pose[3], 1)

def ru_symbol_U(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def ru_symbol_F(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x + (x / 2),  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

def ru_symbol_X(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

def ru_symbol_Ce(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y * 0.2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.8),  start_y + (y * 0.2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.8),  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x * 0.8),  start_y + (y * 0.2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y * 0.2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def ru_symbol_Che(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def ru_symbol_Sha(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x / 2),  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x (x / 2),  start_y,  start_z, current_pose[3], 1)

def ru_symbol_Shca(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y * 0.2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.8),  start_y + (y * 0.2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.8),  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x * 0.4),  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.4),  start_y + (y * 0.2),  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x * 0.8),  start_y + (y * 0.2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y * 0.2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def ru_symbol_Tverd(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y * 0.8),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.2),  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.2),  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.2),  start_y + (y / 2),  start_z, current_pose[3], 1)

def ru_symbol_Yii(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.8),  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.8),  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def ru_symbol_Magki(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def ru_symbol_Eee(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x * 0.5),  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def ru_symbol_Yu(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.2),  start_y + (y /2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.2),  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.2),  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.2),  start_y + (y / 2),  start_z, current_pose[3], 1)

def ru_symbol_Ya(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

#Graphic

#Numeric
def nubmer_1(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x + (x / 2),  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + y,  start_z, current_pose[3], 1)

def number_2(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def number_3(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def number_4(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def number_5(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

def number_6(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def number_7(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x * 0.25),  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.75),  start_y (y / 2),  start_z, current_pose[3], 1)

def number_8(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def number_9(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def number_0(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

ru = {"A":ru_symbol_A,  
      "Б":ru_symbol_Be, 
      "В":ru_symbol_Ve, 
      "Г":ru_symbol_G,  
      "Д":ru_symbol_D,           
      "Е":ru_symbol_E,  
      "Ё":ru_symbol_Yo, 
      "Ж":ru_symbol_Ze, 
      "З":ru_symbol_Ze, 
      "И":ru_symbol_And,
      "Й":ru_symbol_Yo, 
      "К":ru_symbol_K,  
      "Л":ru_symbol_L,  
      "М":ru_symbol_M,  
      "Н":ru_symbol_H,  
      "О":ru_symbol_O,  
      "П":ru_symbol_P,  
      "Р":ru_symbol_R,  
      "С":ru_symbol_C,  
      "Т":ru_symbol_T,  
      "У":ru_symbol_U,  
      "Ф":ru_symbol_F,  
      "Х":ru_symbol_X,  
      "Ц":ru_symbol_Ce, 
      "Ч":ru_symbol_Che,
      "Ш":ru_symbol_Sha, 
      "Щ":ru_symbol_Shca, 
      "Ъ":ru_symbol_Tverd, 
      "Ы":ru_symbol_Yi, 
      "Ь":ru_symbol_Magki, 
      "Э":ru_symbol_Eee,
      "Ю":ru_symbol_U,  
      "Я":ru_symbol_Ya 
}

en = {"A": us_symbol_A,
      "B": us_symbol_B,
      "C": us_symbol_C,
      "D": us_symbol_D,
      "E": us_symbol_E,
      "F": us_symbol_F,
      "G": us_symbol_G,
      "H": us_symbol_H,
      "I": us_symbol_I,
      "J": us_symbol_J,
      "K": us_symbol_K,
      "L": us_symbol_L,
      "M": us_symbol_M,
      "N": us_symbol_N,
      "O": us_symbol_O,
      "P": us_symbol_P,
      "Q": us_symbol_Q,
      "R": us_symbol_R,
      "S": us_symbol_S,
      "T": us_symbol_T,
      "U": us_symbol_U,
      "V": us_symbol_V,
      "W": us_symbol_W,
      "X": us_symbol_X,
      "Y": us_symbol_Y,
      "Z": us_symbol_Z 
}

numbers = {
    "0": number_0,  
    "1": nubmer_1,  
    "2": number_2,  
    "3": number_3,  
    "4": number_4,  
    "5": number_5,  
    "6": number_6,  
    "7": number_7,  
    "8": number_8,  
    "9": number_9,  

}

en["A"](25,25,55,20,20)
import threading
import DobotDllType as dType
import random as rand
import math

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

def us_symbol_T(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x / 2),  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y,  start_z, current_pose[3], 1)

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

ru = {"A":ru_symbol_A,  # type: ignore
      "Б":ru_symbol_Be, # type: ignore
      "В":ru_symbol_Ve, # type: ignore
      "Г":ru_symbol_G,  # type: ignore
      "Д":"",           # type: ignore
      "Е":ru_symbol_E,  # type: ignore
      "Ё":ru_symbol_Yo, # type: ignore
      "Ж":ru_symbol_Ze, # type: ignore
      "З":ru_symbol_Ze, # type: ignore
      "И":ru_symbol_And,# type: ignore 
      "Й":ru_symbol_Yo, # type: ignore
      "К":ru_symbol_K,  # type: ignore
      "Л":ru_symbol_L,  # type: ignore
      "М":ru_symbol_M,  # type: ignore
      "Н":ru_symbol_H,  # type: ignore
      "О":ru_symbol_O,  # type: ignore
      "П":ru_symbol_P,  # type: ignore
      "Р":ru_symbol_R,  # type: ignore
      "С":ru_symbol_C,  # type: ignore
      "Т":ru_symbol_T,  # type: ignore
      "У":ru_symbol_U,  # type: ignore
      "Ф":ru_symbol_F,  # type: ignore
      "Х":ru_symbol_X,  # type: ignore
      "Ц":ru_symbol_Ce, # type: ignore
      "Ч":ru_symbol_Che,# type: ignore
      "Ш":ru_symbol_Sha,# type: ignore 
      "Щ":ru_symbol_Shca,# type: ignore 
      "Ъ":ru_symbol_Tverd,# type: ignore 
      "Ы":ru_symbol_Yi, # type: ignore
      "Ь":ru_symbol_Magki,# type: ignore 
      "Э":ru_symbol_Eee,# type: ignore 
      "Ю":ru_symbol_U,  # type: ignore
      "Я":ru_symbol_Ya  # type: ignore
}

en = {"A": us_symbol_A,
      "B": "",
      "C": "",
      "D": "",
      "E": us_symbol_E,
      "F": us_symbol_F,
      "G": "",
      "H": us_symbol_H,
      "I": us_symbol_I,
      "J": "",
      "K": us_symbol_K,
      "L": us_symbol_L,
      "M": us_symbol_M,
      "N": us_symbol_N,
      "O": "",
      "P": "",
      "Q": "",
      "R": "",
      "S": "",
      "T": us_symbol_T,
      "U": "",
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
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
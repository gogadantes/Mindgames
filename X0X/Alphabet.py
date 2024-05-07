import threading
import DobotDllType as dType
import random as rand
import math

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

def symbol_A(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x * 0.75),  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.25),  start_y + (y / 2),  start_z, current_pose[3], 1)

def symbol_E(start_x, start_y, start_z, x, y):
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

def symbol_F(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def symbol_H(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + (y / 2),  start_z, current_pose[3], 1)

def symbol_I(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x / 2),  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + y,  start_z, current_pose[3], 1)

def symbol_K(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y + (y / 2),  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def symbol_L(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def symbol_M(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

def symbol_N(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

def symbol_T(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x / 2),  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y,  start_z, current_pose[3], 1)

def symbol_V(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)
  
def symbol_W(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.25),  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x * 0.75),  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

def symbol_X(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

def symbol_Y(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + (y / 2),  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    dType.SetPTPCmdEx(api, 0, start_x + (x / 2),  start_y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + (x / 2),  start_y + (y / 2),  start_z, current_pose[3], 1)

def symbol_Z(start_x, start_y, start_z, x, y):
    dType.SetPTPCmdEx(api, 0, start_x,  start_y + y,  start_z, 0, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y + y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x,  start_y,  start_z, current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, start_x + x,  start_y,  start_z, current_pose[3], 1)




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
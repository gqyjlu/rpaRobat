import math
import random
import time
import pyautogui
import pyperclip
import win32api


#----这里以后重新下写，可以都用win32来实现键盘和鼠标操作----
#----这里键盘操作和鼠标点击是用pyautogui，win32api仅仅用来移动鼠标指针

def trackComput(curPosNow,target):
    
    step = 0
    flag = True
    curPos = curPosNow
    sumDis = target - curPos
    resultList = []
    speed = 0.0
    while (flag):
        #----计算步长变化----
        dis = int(target - curPos)
        if abs(dis) > abs(sumDis)/2.0 and abs(dis) <= abs(sumDis):
            #----加速阶段---
            speed  = min((pow(2,min(step,10))) * (1 + random.random()) ,60)
        elif abs(dis) <= abs(sumDis)/2.0 and abs(dis) > 0:
            #----减速阶段
            speed =  (speed * 0.7) + random.randint(0,3)
        elif abs(dis) == 0:
            speed = 0.0
        #----修改pos，取决于移动方向，接近目标点正负2误差就行
        if dis > 0 and dis > 2:
            curPos = int(curPos + speed )
        elif dis < 0 and dis < -2:
            curPos = int(curPos - speed )
        elif dis <= 2 or dis >= -2 :
            flag = False
           
        resultList.append(curPos)
        step += 1
    return resultList

def humanMoveAndClick(targetPosList):
    humanMove(targetPosList)
    time.sleep(random.random())
    pyautogui.click(targetPosList[0],targetPosList[1])
    time.sleep(1.0+random.random())
    return


def humanMoveAndRandomClick(startPos,endPos):
    #----随机在范围内点击-----
    #----在范围内选择一个点---
    #----这里加一个需求，就是，点击更加靠近中心，有内收，防止点击不上
    xs = startPos[0]
    xe = endPos[0]
    if abs(xe - xs) >= 20:
        xs = xs + 10
        xe = xe - 10
    
    ys = startPos[1]
    ye = endPos[1]
    if abs(ys - ye) >= 20:
        ys = ys + 10
        ye = ye - 10

    x = random.randint(int(xs),int(xe))
    y = random.randint(int(ys),int(ye))
    humanMoveAndClick([x,y])
    return

def randomMove():
    #---随便滑一下
    x = random.randint(300,2500)
    y = random.randint(200,1600)
    humanMove([x,y])
    return

def humanInputByClip(content):
    time.sleep(0.1)
    pyperclip.copy(content)
    pyautogui.keyDown('ctrlleft')
    time.sleep(0.3 + 0.1*random.randint(0,2))
    pyautogui.keyDown('v')
    time.sleep(0.3 + 0.1*random.randint(0,2))
    pyautogui.keyUp('ctrlleft')
    time.sleep(0.3 + 0.1*random.randint(0,2))
    pyautogui.keyUp('v')
    time.sleep(0.1)
    return
    
def allSelect():
    #---写个全选的---ctrl s的---
    time.sleep(0.1)
    pyautogui.keyDown('ctrlleft')
    time.sleep(0.1 + 0.1*random.randint(0,2))
    pyautogui.keyDown('a')
    time.sleep(0.1 + 0.1*random.randint(0,2))
    pyautogui.keyUp('ctrlleft')
    time.sleep(0.1 + 0.1*random.randint(0,2))
    pyautogui.keyUp('a')
    time.sleep(0.1)

def specialKey(keyName):
    #---输入一些特殊字符，回车，删除啥的
    #---就是简单随机一下按键时间
    pyautogui.keyDown(keyName)
    time.sleep(0.1 + 0.1*random.randint(0,2))
    pyautogui.keyUp(keyName)
    time.sleep(0.1)
    return



def humanMove(targetPosList):
    targetPos = targetPosList
    trackResult = []
    nowPos = list(pyautogui.position())
    xTrack = trackComput(nowPos[0],targetPos[0])
    yTrack = trackComput(nowPos[1],targetPos[1])
    for i in range(0,max(len(xTrack),len(yTrack))):
        x = targetPos[0]
        y = targetPos[1]
        try:
            x = xTrack[i] 
        except(IndexError):
            pass

        try:
            y = yTrack[i]
        except(IndexError):
            pass

        trackResult.append([x,y])

    
    for item in trackResult:
        x = item[0]
        y = item[1]
        win32api.SetCursorPos((x,y))
        time.sleep(0.005)


def humanScrollIndexY(length):
    #----做一个竖向滚屏的函数----
    #----最好也是慢慢的滚动的----
    #----正数是向上滚动----
    #----差不多就得了----给点误差更真实
    time.sleep(1)
    flag = True
    realLength = 0
    while (flag):
        time.sleep(0.01)
        if length < 0:
            step = random.randint(-80,-50)
        elif length > 0:
            step = random.randint(50,80)
        elif length == 0:
            pass
        
        pyautogui.scroll(step)
        realLength += step
        if abs(length - realLength) <= 80:
            flag = False
    print ('实际滚屏了多少？',realLength)
    time.sleep(1)
    return


if __name__ == "__main__":
    humanScrollIndexY(-100)
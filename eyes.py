#encoding=utf8
import PIL
from PIL import ImageGrab
from PIL import Image
from cv2 import cv2 
import numpy as np
import time
import sycmException

def getImgSize(img):
    a = cv2.imread(img)
    return list((a.shape))[0:2]



def findVariousElements(targetImgList,value=0.9):
    #----在一次截屏中找多种模板元素并返回位置-----
    try:
        im = np.array(ImageGrab.grab())
        imgGray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        resultDic = {}
        for targetImg in targetImgList:
            template = cv2.imread(targetImg, 0)
            res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= value)
            resultList = []
            yList = loc[0]
            xList = loc[1]
            xTmp = -20
            yTmp = -20
            #----在这里一样要过滤掉近似结果-----
            for i in range(0,len(xList)):
                if abs(xList[i] - xTmp) >= 10 and abs(yList[i] - yTmp) >= 10:
                    resultList.append([xList[i],yList[i]])
                    xTmp = xList[i]
                    yTmp = yList[i]
            #----有结果就装在字典里，没结果就算    
            if len(resultList) != 0:
                resultDic[targetImg] = resultList
        return resultDic
    except(cv2.error):
        pass

def findElements(targetImg, value = 0.9):
    #----截屏一次去找一种模板元素的位置信息------
    #----这里容易出现一个bug，就是一个元素接近纯色时候，会左右偏差几个像素的位置都会识别出来
    #----容易把一个结果返回成多个结果------x,y相差10个px以上才算是俩结果-----
    try:
        im = np.array(ImageGrab.grab())
        imgGray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(targetImg, 0)
        res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= value)
        resultList = []
        yList = loc[0]
        xList = loc[1]
        xTmp = -20
        yTmp = -20
        for i in range(0,len(xList)):
            #----在这里把可能重复的结果过滤一下------
            #----两个坐标很接近的，去掉重复的-----
            if abs(xList[i] - xTmp) >= 10 and abs(yList[i] - yTmp) >= 10:
                resultList.append([xList[i],yList[i]])
                xTmp = xList[i]
                yTmp = yList[i]

        return resultList
    except(cv2.error):
        print ('cv2出现错误')
        pass
    


def findElementsByPos(img,leftTopPos,rightBottomPos):
    #-----在页面范围内，找到元素，可以找到多个-------
    tmpList = findElements(img)
    resultList = []
    if len(tmpList) >= 1:
        for pos in tmpList:
            x = pos[0]
            y = pos[1]
            if x in range(leftTopPos[0],rightBottomPos[0]) and y in range(leftTopPos[1],rightBottomPos[1]):
                resultList.append(pos)
        if len(resultList) >= 1:
            return resultList
        else:
            raise sycmException.SycmCrawlerExceptin('区域范围内没有出现这个元素:'+img)       
    else:
        raise sycmException.SycmCrawlerExceptin('整个屏幕中就没有这个元素:'+img)



def checkIfMask():
    #---检测是否有遮罩-----
    im = np.array(ImageGrab.grab())
    #---从[20,230]采样到[120,400]，去看颜色
    colorACount = 0
    colorBCount = 0
    for x in range(20,120):
        for y in range(230,400):
            color = list(im[y][x])
            if color == [33,98,229]:
                colorACount += 1
            elif color == [17,50,115]:
                colorBCount += 1
    if colorACount > colorBCount:
        print ('无遮罩状态',colorACount,colorBCount)
        return False
    elif colorACount < colorBCount:
        print ('有遮罩状态',colorACount,colorBCount)
        #----检测是否有广告关闭按钮-----
        if findElements('targetImg/guanggaoguanbi.png') != None:
            return True
        else:
            print ('只检测到遮罩，没有检测到广告关闭按钮')
    
    return

'''

def checkIfChange():
    #----检测是否画面有变化----
    #----一定要注意，调用PIL截屏的时候，是不会把鼠标指针截屏进去的----
    
    while (True):
        img1 = np.array(ImageGrab.grab((0,0,1700,500)))
        time.sleep(0.5)
        img2 = np.array(ImageGrab.grab((0,0,1700,500)))
        difference = cv2.subtract(img1, img2)
        result = np.any(difference)
        if result == True:
            print ('变化了')
        else:
            print ('没变化')

    return
'''

if __name__ == "__main__":
    
    while(True):
        time.sleep(0.5)
        #print (findElements('targetImg/ceshi.png'))
        #print (getImgSize('targetImg/ceshi.png'))
        print (findVariousElements(['targetImg/ceshi1.png','targetImg/ceshi2.png','targetImg/ceshi3.png']))
        #checkIfAd()
        #checkIfChange()
    

    

        
        









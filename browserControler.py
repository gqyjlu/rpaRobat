#encoding=utf8
import eyes
import humanAction
import sycmException
import time
import random


def init():
    #----检查浏览器是否启动，并处于最大化位置----
    tmp = eyes.findElementsByPos('targetImg/browserClose.png',[2400,0],[2700,200])
    if len(tmp) == 1:
        print ('浏览器已经摆放好')
        return True
    else:
        raise sycmException.SycmCrawlerExceptin('浏览器没有摆放好')

def loadUrl(url):

    if waitForImgListDisplay(['targetImg/browserButton.png']) == True:
        #----计算地址栏位置----
        tmpPosList = eyes.findElements('targetImg/browserButton.png')
        tmpPos = tmpPosList[0]
        urlPosA = [tmpPos[0] + 500,tmpPos[1]+10]
        urlPosB = [tmpPos[0] + 800,tmpPos[1]+20]
        #----点击地址栏--------
        humanAction.humanMoveAndRandomClick(urlPosA,urlPosB)
        #----全选删除输入url回车
        humanAction.allSelect()
        humanAction.specialKey('delete')
        humanAction.humanInputByClip(url)
        humanAction.specialKey('return')
        #----等待载入页面成功--------
        if waitForImgListDisplay(['targetImg/shuaxin.png']) == True:
            return True
        else:
            raise sycmException.SycmCrawlerExceptin('载入时间超时:'+url)

    else:
        raise sycmException.SycmCrawlerExceptin('没有找到浏览器')
        


def clickElement(img):
    #-----点击前检测是页面是否有且只有一个这个元素----
    if waitForImgListDisplay([img]) == True :
        posList = eyes.findElements(img)
        if len(posList) == 1:
            #----看图片size----
            size = eyes.getImgSize(img)
            
            posA = posList[0]
            posB = [posA[0] + size[1] , posA[1] + size[0]]
            humanAction.humanMoveAndRandomClick(posA,posB)
            
            '''
            #----这里加一个彩蛋，每次点击成功，都有1/3瞎划拉一下鼠标----
            if random.randint(0,2) == 0:
                humanAction.randomMove()
            '''

            #---等待浏览器响应----
            waitForImgListDisplay(['targetImg/shuaxin.png'])
            return True
        else:
            print ('posList',posList)
            raise sycmException.SycmCrawlerExceptin('页面有不止这一个元素:'+img)
    else:
        raise sycmException.SycmCrawlerExceptin('页面不存在这个元素:'+img)
        
    
   

def clickElementByPos(img,leftTopPos,rightBottomPos):
    #---等待下加载----
    waitForImgListDisplay([img])
    #----------------
    resultList = eyes.findElementsByPos(img,leftTopPos,rightBottomPos)
    if len(resultList) == 1:
        size = eyes.getImgSize(img)
        posA = resultList[0]
        posB = [posA[0] + size[1] , posA[1] + size[0]]
        humanAction.humanMoveAndRandomClick(posA,posB)
        #---一定概率瞎划拉鼠标----
        if random.randint(0,2) == 0:
                humanAction.randomMove()
        waitForImgListDisplay(['targetImg/shuaxin.png'])
        return True
    else:
        raise sycmException.SycmCrawlerExceptin('范围内不存在或者存在多个要点击的元素:'+img)


def checkElementsAllExist(imgList):
    resultDic = eyes.findVariousElements(imgList)
    if len(resultDic) == len(imgList):
        #----每一个元素都检测出来了一个或者以上的坐标----
        return True
    else:
        return False

def waitForImgListDisplay(imgList):
    #----等待屏幕上出现某些特定的元素----
    startTime = time.time()
    flag = True
    while(flag):
        resultDic = eyes.findVariousElements(imgList)
        if len(resultDic) == len(imgList):
            #----这些页面元素都存在----
            flag = False
        time.sleep(0.5)
        now = time.time()
        if now - startTime > 100:
            #----100s都没有响应就超时退出----
            raise sycmException.SycmCrawlerExceptin('超时还没有出现特征元素：'+str(imgList))
            
    return True
    
        
    



    




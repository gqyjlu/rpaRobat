#encoding=utf8

import browserControler
import humanAction

def start():
    browserControler.init()
    browserControler.loadUrl('http://sycm.taobao.com')
    #----在这里判断下是否登录状态----
    if browserControler.checkElementsAllExist(['targetImg/denglu.png']) == True:
        print ('还没登录呢，准备登录')
        browserControler.clickElement('targetImg/denglu.png')

    if browserControler.checkElementsAllExist(['targetImg/dingbudaohang.png','targetImg/shengyicanmou.png']) == True:
        print ('首页成功加载出来')
    
    

def task0():
    browserControler.clickElement('targetImg/liuliang.png')
    print ('点击流量')
    browserControler.waitForImgListDisplay(['targetImg/liuliangzonglan.png'])
    #----长得像周的比较多，拿位置过滤一下----
    browserControler.clickElementByPos('targetImg/zhou.png',[2100,500],[2500,600])
    #----点击完周只有容易被hover出来的界面阻挡----
    humanAction.randomMove()
    browserControler.waitForImgListDisplay(['targetImg/yijianzhuanhua.png'])

    #----逐一点击完哪些按钮-----
    browserControler.clickElement('targetImg/yijianzhuanhua.png')
    browserControler.clickElement('targetImg/liulanliang.png')
    browserControler.clickElement('targetImg/tiaoshilv.png')
    browserControler.clickElement('targetImg/pingjuntingliushichang.png')
    browserControler.clickElement('targetImg/renjunliulanliang.png')
    browserControler.clickElement('targetImg/laofangkeshu.png')
    browserControler.clickElement('targetImg/xinfangkeshu.png')
    browserControler.clickElement('targetImg/guanzhudianpurenshu.png')

    #----复制表格-----
    browserControler.clickElement('targetImg/fuzhibiaoge.png')
    browserControler.clickElementByPos('targetImg/guanbiaming.png',[2500,200],[2700,500])
    #----表格复制完了，第一个任务算是完成了，在这里做一些剪切板操作来提交内容-----

    #----todo-----剪切板里的解析的部分-------
    task1()


def task1():
    if browserControler.checkElementsAllExist(['targetImg/cebianguanggao.png']) == True:
        #----有广告就给这个广告给关了-----
        browserControler.clickElement('targetImg/cebianguanggao.png')

    browserControler.clickElement('targetImg/dianpulaiyuan.png')
    #---等一下周，点一下周
    browserControler.waitForImgListDisplay(['targetImg/zhou.png'])
    browserControler.clickElementByPos('targetImg/zhou.png',[2100,500],[2500,600])
    humanAction.randomMove()
    humanAction.humanScrollIndexY(-800)
    browserControler.clickElementByPos('targetImg/xiazai.png',[2300,0],[2700,1500])

    #----在这里处理下载下来的文件-----录入数据库----
    #-----todo-------
    task2()


def task2():
    browserControler.clickElement('targetImg/pinlei.png')
    if browserControler.checkElementsAllExist(['targetImg/cebianguanggao.png']) == True:
        #----有广告就给这个广告给关了-----
        browserControler.clickElement('targetImg/cebianguanggao.png')
    browserControler.clickElement('targetImg/hongguanjiankong.png')
    humanAction.randomMove()
    browserControler.clickElementByPos('targetImg/zhou.png',[2100,500],[2500,900])
    #----滚屏----
    humanAction.humanScrollIndexY(-800)
    #----注意这行下载，UI坏了，折行了的，这块可能会以后容易出错，他们要是修了bug就重新截图就行
    browserControler.clickElement('targetImg/zhehangxiazai.png')
    task3()

def task3():
    browserControler.clickElement('targetImg/jiaoyi.png')
    browserControler.clickElement('targetImg/jiaoyigoucheng.png')
    humanAction.humanScrollIndexY(-400)
    browserControler.clickElement('targetImg/anniuxiazai.png')
    browserControler.clickElement('targetImg/xiazaiqueding.png')
    task4()

def task4():
    browserControler.clickElement('targetImg/jingzheng.png')
    browserControler.clickElementByPos('targetImg/zhou.png',[2100,300],[2500,600])
    browserControler.clickElement('targetImg/yijianzhuanhua.png')
    browserControler.clickElement('targetImg/fuzhibiaoge.png')
    #---在这里读取剪切板并做上传操作-----
    #----todo-----
    browserControler.clickElementByPos('targetImg/guanbiaming.png',[2500,200],[2700,500])
    browserControler.clickElement('targetImg/shengyicanmou.png')
    task5()


def task5():
    browserControler.clickElement('targetImg/jingzheng.png')
    browserControler.clickElement('targetImg/jingdianfenxi.png')
    browserControler.clickElementByPos('targetImg/zhou.png',[2100,300],[2500,600])

    #---接下来这块比较复杂，要轮着选择竞品店铺，尝试用非url变换的方式来搞一下----
    #---这里面还差一部分没有做完，切换店铺之后，要点好几个一键转化的部分，目前还没有做---
    for item in ['雀巢','野兽生活','理想燃料','smeal','wonderlab','非糖轻盈','非糖减脂餐','乐纯食品','蕴巢','丢糖',
    '薄荷健康','咚吃','keep食品','王饱饱','kck食品','绿瘦','ffit8','正大玉膳','姿美堂','田园主义','云耕','若饭']:
        browserControler.clickElementByPos('targetImg/jingdiantianjia.png',[1000,600],[1600,1000])
        browserControler.clickElement('targetImg/shurujiankongdianpu.png')
        humanAction.humanInputByClip(item)
        #----点击首位suggestion
        if item == '野兽生活':
            browserControler.clickElementByPos('targetImg/yeshoushenghuo.png',[1000,800],[2100,1200])
        elif item == '非糖减脂餐':
            browserControler.clickElementByPos('targetImg/feitangjianzhican.png',[1000,800],[2100,1200])
        else:
            browserControler.clickElementByPos('targetImg/qijiandian.png',[1000,800],[2100,1200])
        browserControler.clickElement('targetImg/yijianzhuanhua.png')
        browserControler.clickElement('targetImg/fuzhibiaoge.png')
        #----在这里读取剪切板，上传数据----
        browserControler.clickElementByPos('targetImg/guanbiaming.png',[2500,200],[2700,500])
        browserControler.clickElementByPos('targetImg/jingdianguanbi.png',[1600,700],[1900,800])
        
    task7()

def task7():
    browserControler.clickElement('targetImg/shengyicanmou.png')
    #browserControler.clickElement('targetImg/')
    pass

if __name__ == "__main__":
    start()
    task4()






    




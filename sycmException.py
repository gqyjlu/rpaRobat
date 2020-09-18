#encoding=utf8


class SycmCrawlerExceptin(Exception):
    def __init__(self,info):
        self.info = info
    def __str__(self):
        print(self.info)
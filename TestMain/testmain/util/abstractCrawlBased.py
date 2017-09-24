#encoding:utf8

import abc

class abstractCrawlBased(object):
    def __init__(self):
        self.response = None
    def run(self):
        print("父类")
    def getContent(self):
        html = self.response.read().decode("utf")
        return  html

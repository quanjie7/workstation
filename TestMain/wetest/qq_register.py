#encoding:utf-8
import re
import time
import json
import requests
import traceback
from selenium import webdriver

class Register():
    def __init__(self):
        self.token = None
        self.proxies = []
        self.phones = []
        self.getToken
    def run(self):
        # self.getReceivedPhoneList()
        # self.getVerification("13726637165")
        while True:
            self.register_qq(self.getPhoneNo)
            time.sleep(10)
            print(len(self.phones)," ip：",len(self.proxies))
            print("\n---------------------------------------------\n")

    def register_qq(self,phone):
        try:
            chrome_options = webdriver.ChromeOptions()
            # ip = str(self.getProxyIp)
            # print("ip:",ip)
            # chrome_options.add_argument('--proxy-server=http://%s'% ip)
            chrome_options.add_argument(
                'user-agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"')
            driver = webdriver.Chrome(chrome_options=chrome_options)
            driver.get('http://httpbin.org/ip')
            time.sleep(1)
            driver.get("https://ssl.zc.qq.com/v3/index-chs.html?type=3")
            print("手机号：",phone)
            time.sleep(10)

            driver.find_element_by_xpath("//input[@id='phone']").send_keys(phone)
            driver.find_element_by_xpath("//a[@id='send-sms']").click()
            time.sleep(7)

            error = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/form/div[6]/div")
            content_error = error.text
            if "该手机号码今天接收验证码数目已达上限" in content_error:
                print("error:",content_error)
                self.addIgnorePhone(phone)
                # self.proxies.append(ip)
            else:
                driver.find_element_by_xpath("//input[@id='nickname']").send_keys("shu%s"%phone)
                driver.find_element_by_xpath("//input[@id='password']").send_keys("wwshushu@7")
                driver.find_element_by_xpath("//input[@id='code']").send_keys(self.getVerification(phone))
                # print("请输入验证码：",self.getVerification(phone=phone))
                time.sleep(30)
                driver.find_element_by_xpath("//input[@id='get_acc']").click()
                time.sleep(60)
        except Exception as e:
            traceback.print_exc()#3410473007
            # self.phones.append(phone)


        #，建议尝试其他手机号码
        driver.close()

    @property
    def getProxyIp(self):
        if self.proxies == [] or self.proxies == None:
            url = "http://dps.kuaidaili.com/api/getdps/?orderid=939421529410437&num=50&ut=1&format=json&sep=1"
            response = requests.get(url)
            content = response.text
            msg = json.loads(content)
            data = msg['data']
            proxy_lists = data['proxy_list']
            for item in proxy_lists:
                self.proxies.append(item)
            self.proxies.pop()
        else:
            return self.proxies.pop()
    @property
    def getToken(self):
        time.sleep(3)
        url_login = "http://api.eobzz.com/httpApi.do?action=loginIn&uid=shushu&pwd=wwshushu@7"
        print("登录速运：",url_login)
        response = requests.get(url=url_login)
        token = response.text[7:]
        self.token = token
    @property
    def getPhoneNo(self):
        if self.phones ==[]:
            #获取手机号
            try:
                url_phones = "http://api.eobzz.com/httpApi.do?action=getMobilenum&pid=10658&uid=shushu&token=%s&mobile=&size=10" % self.token
                print("获取手机号：",url_phones)
                response = requests.get(url=url_phones)
                phones = response.text
                response.close()
                print('获取的手机号1：')
                phones =  phones[:phones.index("|")].split(";")
                print("获取的手机号：",phones)
                for phone in phones:
                    self.phones.append(phone)
                return self.getPhoneNo
            except Exception as e:
                traceback.print_exc()
                self.getPhoneNo
        else:
            return self.phones.pop(0)
    def getVerification(self,phone):
        for i in range(4):
            time.sleep(10)
            url = "http://api.eobzz.com/httpApi.do?action=getVcodeAndHoldMobilenum&uid=shushu&token=%s&mobile=%s&next_pid=10658" %(self.token,phone)
            print("第",i,"次获取验证码：",url)
            response = requests.get(url)
            phone_verifiaction = response.text
            if "not_receive" in phone_verifiaction :
                continue
            print("获取验证码结果：",phone_verifiaction)
            com = re.compile("【腾讯科技】(\d{6})\\（", re.DOTALL)
            try:
                return com.findall(phone_verifiaction)[0]
            except Exception as e:
                print("请手动输入验证码。")
        raise Exception("没有获取验证码。")
    def addIgnorePhone(self,phone):
        url = "http://api.eobzz.com/httpApi.do?action=addIgnoreList&uid=shushu&token=%s&mobiles=%s&pid=10658"% (self.token,phone)
        requests.get(url)
    def getReceivedPhoneList(self):
        url = "http://api.eobzz.com/httpApi.do?action=getRecvingInfo&uid=shushu&pid=10658&token=%s" % self.token
        print(url)
        response = requests.get(url)
        print(response.text)


if __name__ == "__main__":
    print("start......")
    register = Register()
    register.run()

#迭代器
#def myGen():
    #print("yield running!")
    #yield 1
    #yield 2

#myG = myGen()
#next(myG)
#next(myG)

#获取页面html,保存为文件
#import urllib.request
#response = urllib.request.urlopen("https://www.kishere.gq")
#html = response.read()
#html = html.decode("utf-8")
#print(html)
#f = open('html_of_kishere\'s_web.txt','a',encoding='utf-8')
#f.write(html)
#f.close()

#获取一张图片,保存到本地
#import urllib.request
#response = urllib.request.urlopen("https://kishere.gq/wp-content/uploads/2019/12/QQ%E6%88%AA%E5%9B%BE20191122201535-300x249.jpg")
#ima = response.read()
#with open('image_1.jpg','wb')as f:
#    f.write(ima)

#有道翻译调用
import urllib.request
import urllib.parse
import json

content = input('input what you want to translate:')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
data['i']= content
data['from']= 'AUTO'
data['to']= 'AUTO'
data['smartresult']= 'dict'
data['client']= 'fanyideskweb'
data['salt']= '15792275563114'
data['sign']= '7f10eba2a842e99b92aa180f80e1ef6a'
data['ts']= '1579227556311'
data['bv']= '470df6afd582fe67e18c2221dab59fb3'
data['doctype']= 'json'
data['version']= '2.1'
data['keyfrom']= 'fanyi.web'
data['action']= 'FY_BY_REALTlME'

data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data)
html = response.read().decode("utf-8")

target = json.loads(html)
print('result = %s' %(target['translateResult'][0][0]['tgt']))

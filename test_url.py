#def myGen():
    #print("yield running!")
    #yield 1
    #yield 2

#myG = myGen()
#next(myG)
#next(myG)
import urllib.request
response = urllib.request.urlopen("https://www.kishere.gq")
html = response.read()
html = html.decode("utf-8")
print(html)
f = open('html_of_kishere\'s_web.txt','a',encoding='utf-8')
f.write(html)
f.close()
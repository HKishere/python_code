import urllib.request
import os

def urlopen(url):
    req = urllib.request.Request(url)
    req.add_header("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")
    response = urllib.request.urlopen(url)
    html = response.read()

    return html


def get_an(url):
    html = urlopen(url).decode('utf-8')

    a = html.find('selectarcpost') - 64 # a是最新文章的url的起始位置
    b = html.find('"', a)
    print(html[a:b])
    return html[a:b]

def get_pn(url):
    html = urlopen(url).decode('utf-8')
    a = html.find('var Cdetail_total') + 20
    b = html.find(';', a)
    print(html[a:b])
    return html[a:b]

def find_ima(page_url):
    html = urlopen(page_url).decode('utf-8')
    ima_addr = []

    start_p = html.find('news_warp_center')
    end_p = html.find('/div',start_p)

    a = html.find('img src=', start_p,end_p)

    #print(html[start_p:end_p])
    
    if start_p != -1:
        while a != -1:
            b = html.find('.jpg',a, a+100)
            if b != -1:
                ima_addr.append(html[a+9:b+4])
            else:
                b = a + 9
            a = html.find('img src=', b,end_p)
        for i in ima_addr:
            print(i)


    return ima_addr

def save_ima(folder, ima_addr):
    for each in ima_addr:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = urlopen(each)
            f.write(img)

def download_sombar(folder='ima_sombar'):
    #os.mkdir(folder)
    os.chdir(folder)
    
    url = "https://www.3dmgame.com/bagua_65_1/"
    #page_url = "https://www.3dmgame.com/bagua/"
    root_article_addr = get_an(url)
    page_num = int(get_pn(root_article_addr))
    end_of_article_addr = root_article_addr.find('.html')
    root_article_addr = root_article_addr[0: end_of_article_addr]

    for i in range(page_num):
        #page_num -= i
        article_addr = root_article_addr
        if i > 0:
            article_addr += "_"
            article_addr += str(i+1)
        article_addr += ".html"
        ima_addr = find_ima(article_addr)
        save_ima(folder, ima_addr)

if __name__ == "__main__":
    download_sombar()

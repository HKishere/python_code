map=[]

def Init():
    for each in range(1,4):
        buf = input('请输入第%d行数字,"_"表示空格:'%each)
        map.append(buf)

def Check(map):
    for j in range(0,3):
        for i in range(0,3):
            if map[j][i] == "_":
                


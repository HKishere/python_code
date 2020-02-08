#!/usr/bin/python
import os
map = ['002070340','000009001','009802070','600080007','000950003','830000010','400200060','020003000','900400700']

#初始化数独
def Init():
    choose = input("是否要自己输入数独地图? 如果不输入将使用示例\n1.是\n2.否\n")
    while ((choose != '1') and (choose != '2')):
        print("请选择1或2!\n")
        choose = input("是否要自己输入数独地图? 如果不输入将使用示例\n1.是\n2.否\n")
    
    if choose == 1:
        for each in range(1,10):
            print('input the sudu value of %dth row, use 0 to replace the blank:' %each)
            buf = input()
            while len(buf) != 9:
                print('input the sudu value of %dth row, use 0 to replace the blank:' %each)
                buf = input()
            else:
                map.append(buf)
    if choose == 2:
        pass
    
    print("here is your map:\n==========")
    for each in map:
        print(each)

#判断是否满足九宫格条件
def blockcheck(row, col, value):
    row = (row//3)*3
    col = (col//3)*3
    map_block = map[row][col]
    map_block = map_block + (map[row][col+1])
    map_block = map_block + (map[row][col+2])
    map_block = map_block + (map[row+1][col])
    map_block = map_block + (map[row+1][col+1])
    map_block = map_block + (map[row+1][col+2])
    map_block = map_block + (map[row+2][col])
    map_block = map_block + (map[row+2][col+1])
    map_block = map_block + (map[row+2][col+2])
    return map_block.find(str(value))

#解数独开始
def Solve(row, col):
    if (row < 9) & (col < 9):
        if map[row][col] == '0':
            for each in range(1,10):
                map_row = map[row]
                map_col = ''
                for i in range(0,9):
                    map_col += map[i][col]
                if (map_row.find(str(each)) == -1) and (map_col.find(str(each)) == -1) and (blockcheck(row,col,each) == -1):
                    backup = map[row]
                    buf = list(map[row])
                    buf[col] = str(each)
                    map[row] = "".join(buf)
                    #PrintMap(map)
                    if Solve(row, col + 1) == 1:
                        return 1
                    else:
                        map[row] = backup
        else:
            return Solve(row, col + 1)
    else:
        if row < 8:
            return Solve(row + 1, 0)
        else:
            return 1

#将地图输出到文件中
def PrintMap(map):
    with open('record.txt', 'a')as f:
        f.write('===========\n')
        for each in range(0,9):
            f.write(map[each])
            f.write("\n")
        f.close()

#主函数流程
def Run():
    Init()
    Solve(0,0)
    print('\n解数独完成!\n==========')
    for each in map:
        print(each)

if __name__ == "__main__":
    Run()

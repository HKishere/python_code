import os
map = ['002070340','000009001','009802070','600080007','000950003','830000010','400200060','020003000','900400700']
def Init():
    pass
#    for each in range(1,10):
#        print('input the sudu value of %dth row, use 0 to replace the blank:' %each)
#        buf = input()
#        while len(buf) != 9:
#            print('input the sudu value of %dth row, use 0 to replace the blank:' %each)
#            buf = input()
#        else:
#            map.append(buf)
#    
#    print("here is your map:\n==========")
#    
#    for each in map:
#        print(each)

def blockcheck(row, col, value):
    map_block = map[row//3][col//3]
    map_block = map_block + (map[row//3][col//3+1])
    map_block = map_block + (map[row//3][col//3+2])
    map_block = map_block + (map[row//3+1][col//3])
    map_block = map_block + (map[row//3+1][col//3+1])
    map_block = map_block + (map[row//3+1][col//3+2])
    map_block = map_block + (map[row//3+2][col//3])
    map_block = map_block + (map[row//3+2][col//3+1])
    map_block = map_block + (map[row//3+2][col//3+2])
    return map_block.find(str(value))


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
                    PrintMap(map)
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
            
def PrintMap(map):
    with open('record.txt', 'a')as f:
        f.write('===========\n')
        for each in range(0,9):
            f.write(map[each])
            f.write("\n")
        f.close()


def Run():
    Init()
    Solve(0,0)
    for each in map:
        print(each)

if __name__ == "__main__":
    Run()
map = []
def Init():
    for each in range(1,10):
        print('input the sudu value of %dth row, use 0 to replace the blank:' %each)
        buf = input()
        while len(buf) != 9:
            print('input the sudu value of %dth row, use 0 to replace the blank:' %each)
            buf = input()
        else:
            map.append(buf)
    
    print("here is your map:\n==========")
    
    for each in map:
        print(each)

def blockcheck(row, col):
    start_point = map[row//3][col//3]
    for each in (0,3):


def Solve(row, col):
    if (row < 9) & (col < 9):
        if map[row][col] == '0':
            for each in range(0,9):
                map_row = map[row]
                map_col = ''
                for each in range(0,9):
                    map_col.join(map[each][col])
                if (map_row.find(str(each)) == -1) and (map_col.find(str(each)) == -1):
                    map[row][col] = str(each)
                    if Solve(row, col + 1) == 1:
                        return 1
                else:
                    return 0
    else:
        if row < 8:
            Solve(row + 1, 0)
        else:
            return 1
            



def Run():
    Init()
    Solve(0,0)

if __name__ == "__main__":
    Run()
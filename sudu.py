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
def FindMaxNum():
    pass


def Solve(row, col):
    if (col < 9):
        if (row < 9):
            if(map[row][col] == '0'):




def Run():
    Init()
    Solve(1,2)

if __name__ == "__main__":
    Run()
import random

def checkColumn(m, x):
    for y in range(0,6):
        if m[x][y] == False:
            return False
    return True
 
def checkRow(m, y):
    for x in range(0,6):
        if m[x][y] == False:
            return False
    return True
 
def checkLCross(m):
    for i in range(0,6):
        if m[i][i] == False:
            return False
    return True
    
def checkRCross(m):
    for i in range(0,6):
        if m[5 - i][i] == False:
            return False
    return True
 
def checkBoard():
    w, h = 6, 6;
    m = [[False for x in range(w)] for y in range(h)]
    for i in range(0,15):
        x = random.randrange(0,6)
        y = random.randrange(0,6)
        while m[x][y] == True:
            x = random.randrange(0,6)
            y = random.randrange(0,6)
        m[x][y]=True
    for x in range(0,6):
        if checkColumn(m, x) == True:
            return True
    for y in range(0,6):
        if checkRow(m, y) == True:
            return True
    if (checkLCross(m) == True) or (checkRCross(m) == True):
        return True
    return False
win = 0
total = 0
for i in range(0,10000):
    if checkBoard() == True:
        win += 1
    total += 1
print ("out of ", total, " trials...")
print (win, " are winners")
print ("Win percentage = ", win / total * 100, "%")

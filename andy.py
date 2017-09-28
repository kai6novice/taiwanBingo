import random

def checkColumn(m, x):
 maxMatch = 0
 for y in range(0,6):
  if m[x][y] == False:
   return maxMatch
  maxMatch+=1
 return maxMatch
 
def checkRow(m, y):
 maxMatch = 0
 for x in range(0,6):
        if m[x][y] == False:
            return maxMatch
		maxMatch += 1
    return maxMatch
 
def checkLCross(m):
	maxMatch = 0
    for i in range(0,6):
        if m[i][i] == False:
            return maxMatch
		maxMatch +=1
    return maxMatch
    
def checkRCross(m):
	maxMatch = 0
    for i in range(0,6):
        if m[5 - i][i] == False:
            return maxMatch
		maxMatch +=1
    return maxMatch
 
def checkBoard(m):
	maxMatch = 0
    for x in range(0,6):
		tempMatch = checkColumn(m, x)
        if tempMatch > maxMatch:
            maxMatch = tempMatch
    for y in range(0,6):
		tempMatch = checkRow(m, y)
        if tempMatch > maxMatch:
            maxMatch = tempMatch
	tempMatch = checkLCross(m)
	if tempMatch > maxMatch:
		maxMatch = tempMatch
	tempMatch = checkRCross(m)
	if tempMatch > maxMatch:
		maxMatch = tempMatch	
    return maxMatch

def initBoard():
    w, h = 6, 6;
    m = [[False for x in range(w)] for y in range(h)]
    for i in range(0,15):
        x = random.randrange(0,6)
        y = random.randrange(0,6)
        while m[x][y] == True:
            x = random.randrange(0,6)
            y = random.randrange(0,6)
        m[x][y]=True
    return m
win = 0
win4 = 0
win3 = 0
win2 = 0
win1 = 0
win0 = 0
total = 0
for i in range(0,10000):
    m = initBoard()
	match = checkBoard(m)
    if match == 5:
        win += 1
	elif match == 4:
		win4 +=1
	elif match == 3:
		win3 +=1
	elif match == 2:
		win2 +=1
	elif match == 1:
		win1 +=1
	elif match == 0:
		win0 +=1
    total += 1
print ("out of ", total, " trials...")
print (win, " are winners")
print (win4, " are match 4")
print (win3, " are match 3")
print (win2, " are match 2")
print (win1, " are match 1")
print (win0, " are match 0")
print ("Win percentage = ", win / total * 100, "%")
print ("Win4 percentage = ", win4 / total * 100, "%")
print ("Win3 percentage = ", win3 / total * 100, "%")
print ("Win2 percentage = ", win2 / total * 100, "%")
print ("Win1 percentage = ", win1 / total * 100, "%")
print ("Win0 percentage = ", win0 / total * 100, "%")

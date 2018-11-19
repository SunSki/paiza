#A009:ビームの反射
#https://paiza.jp/challenges/50/ready

RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"

posX = 0
posY = 1

#準備
H,W = input().rstrip().split(' ')
H = int(H)
W = int(W)

box = []
for i in range(H):
    box.append(input())

#初期状態
count = 0
status = [0,0]
direction = RIGHT


#衝突
while True:
    count+=1
    pos = box[status[posY]][status[posX]]
    
    if direction == RIGHT:
        if pos == "/":
            status[posY] -= 1
            direction = UP
        elif pos == "\\":
            status[posY] += 1
            direction = DOWN
        else:
            status[posX] += 1
        
    elif direction == LEFT:
        if pos == "/":
            status[posY] += 1
            direction = DOWN
        elif pos == "\\":
            status[posY] -= 1
            direction = UP
        else:
            status[posX] -= 1
            
    elif direction == UP:
        if pos == "/":
            status[posX] += 1
            direction = RIGHT
        elif pos == "\\":
            status[posX] -= 1
            direction = LEFT
        else:
            status[posY] -= 1
            
    else:
        if pos == "/":
            status[posX] -= 1
            direction = LEFT
        elif pos == "\\":
            status[posX] += 1
            direction = RIGHT
        else:
            status[posY] += 1
            
    
    if status[posX]<0 or status[posX]==W or status[posY]<0 or status[posY]==H:
        break

print(count)
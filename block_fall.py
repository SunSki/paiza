#A017:落ちものシュミレーション
#https://paiza.jp/challenges/123/ready

H,W,N = input().rstrip().split(' ')
W = int(W)
H = int(H)

#ステージを生成
stage = [[0 for i in range(W)] for j in range(H)]
stage.append([1 for i in range(W)])


#ブロックを生成
block = []
for i in range(int(N)):
    h,w,x = input().rstrip().split(' ')
    block.append([int(h),int(w),int(x)])


#ブロックを描写
def draw_block(x,y,h,w,stage):
    for i in range(h):
        for k in range(w):
            stage[y-1-i][x+k] = 1
            

#ブロックを落とす
for i in range(int(N)):
    h = block[i][0]
    w = block[i][1]
    x = block[i][2]
    
    #縦方向
    for y in range(H+1):
        #横方向
        for l in range(w):
            if stage[y][x+l] == 1:
                draw_block(x,y,h,w,stage)
                break
        else:
            continue
        break

        
for i in range(H):
    for k in range(W):
        if stage[i][k] == 0:
            print('.', end='')
        else:
            print('#', end='')
    print('')


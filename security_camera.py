#A018:美術館のセキュリティ
#https://paiza.jp/challenges/137/ready

import math

W,H,M,N = input().rstrip().split(' ')
W=int(W)
H=int(H)
M=int(M)
N=int(N)

cameras = []
arts = []
area = []

for i in range(M):
    camera = input().split()
    cameras.append([int(s) for s in camera])
    
for j in range(N):
    art = input().split()
    arts.append([int(s) for s in art])


for c in cameras:
    x = c[0]
    y = c[1]
    t = c[2]
    d = c[3]
    r = c[4]
    
    theta1 = t-d/2
    theta2 = t+d/2
    tilt_1 = math.tan(math.radians(theta1))
    tilt_2 = math.tan(math.radians(theta2))
    
    for a in arts:
        i = a[0]
        k = a[1]
        point = [i,k]
        if ((x-i)**2 + (y-k)**2) <= r**2:
            
            if theta1 >= 0 and theta1 < 90:
                if theta2 < 90:
                    if k >= tilt_1*(i-x)+y and k <= tilt_2*(i-x)+y:
                        area.append(point)
                else:
                    if k >= tilt_1*(i-x)+y and k >= tilt_2*(i-x)+y:
                        area.append(point)
                    
            elif theta1 >= 90 and theta1 <= 270:
                if theta2 < 270:
                    if k <= tilt_1*(i-x)+y and k >= tilt_2*(i-x)+y:
                        area.append(point)
                else:
                    if k <= tilt_1*(i-x)+y and k <= tilt_2*(i-x)+y:
                        area.append(point)
            else:
                if k >= tilt_1*(i-x)+y and k <= tilt_2*(i-x)+y:
                    area.append(point)
                        
for i in range(N):
    if arts[i] in area:
        print("yes")
    else:
        print("no")
        
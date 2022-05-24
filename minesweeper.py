import random as rn
import numpy as np

print("Choose field size and the amount of mines.")
field_size=int(input("1 - 8x8, 10; 2 - 20x20, 40; 3 - 30x16, 99; 4-Custom."))

field_raw=[]
gamefield_raw=[]
repeat=1
x=0
y=0
win=False
xy=[]

bombs=0
sqfl=0

def gen_field(sizew,sizel,bomb):
    global field
    global gamefield
    for i in range(sizel*sizew):
        field_raw.append('0')
        gamefield_raw.append('■')
    gamefield=np.array_split(gamefield_raw,sizel)
    field=np.array_split(field_raw,sizel)
    for i in range(bomb):
        x=rn.randint(0,sizel-1)
        y=rn.randint(0,sizew-1)
        while field[x][y]=='b':
            x=rn.randint(0,sizel-1)
            y=rn.randint(0,sizew-1)
        field[x][y]='b'
        if x-1>=0:
            if field[x-1][y]!='b':
                field[x-1][y]=int(field[x-1][y])+1
        if x+1<sizel:
            if field[x+1][y]!='b':
                field[x+1][y]=int(field[x+1][y])+1
        if y+1<len(field[0]):
            if field[x][y+1]!='b':
                field[x][y+1]=int(field[x][y+1])+1
        if y-1>=0:
            if field[x][y-1]!='b':
                field[x][y-1]=int(field[x][y-1])+1
        if x-1>=0 and y-1>=0:
            if field[x-1][y-1]!='b':
                field[x-1][y-1]=int(field[x-1][y-1])+1
        if x-1>=0 and y+1<len(field[0]):
            if field[x-1][y+1]!='b':
                field[x-1][y+1]=int(field[x-1][y+1])+1
        if x+1<sizel and y-1>=0:
            if field[x+1][y-1]!='b':
                field[x+1][y-1]=int(field[x+1][y-1])+1
        if x+1<sizel and y+1<len(field[0]):
            if field[x+1][y+1]!='b':
                field[x+1][y+1]=int(field[x+1][y+1])+1

def show(showfield):
    print(' ___'*sizel)
    for i in range(len(showfield)):
        for j in range(len(showfield[i])):
            if j==0: print('|_',end='')
            else:print('_|_',end='')
            print(showfield[i][j],end='')
        print('_|')

def choose():
    y=int(input('Input column number: '))-1
    x=int(input('Input row number: '))-1
    xy.append(y)
    xy.append(x)
    if gamefield[x][y]=='■':
        choose=int(input('1-Set f, 2-Set ?, 3-Open: '))
    elif gamefield[x][y]=='f'or gamefield[x][y]=='?':
        choose=int(input('1-Remove f/?, 2-Skip: '))
    elif gamefield[x][y]=='0'or gamefield[x][y]=='1'or gamefield[x][y]=='2'or gamefield[x][y]=='3'or gamefield[x][y]=='4'or gamefield[x][y]=='5'or gamefield[x][y]=='6'or gamefield[x][y]=='7'or gamefield[x][y]=='8':
        print('This field is already opened')
        choose=3
    if choose==1:
        if gamefield[x][y]=='■':
            gamefield[x][y]='f'
        else:
            gamefield[x][y]='■'
    elif choose==2:
        if gamefield[x][y]=='■':
            gamefield[x][y]='?'
    elif choose==3:
        if field[x][y]=='b':
            print('You lost')
            show(field)
            raise SystemExit
        else:
            gamefield[x][y]=field[x][y]
            if field[x][y]=='0':
                repeat=1
                while repeat!=0:
                    print(xy)
                    y=xy[0]
                    x=xy[1]
                    if x-1>=0:
                        if field[x-1][y]=='0' and gamefield[x-1][y]=='■':
                            gamefield[x-1][y]=field[x-1][y]
                            xy.append(y)
                            xy.append(x-1)
                        elif field[x-1][y]=='1'or field[x-1][y]=='2'or field[x-1][y]=='3'or field[x-1][y]=='4'or field[x-1][y]=='5'or field[x-1][y]=='6'or field[x-1][y]=='7'or field[x-1][y]=='8' and not field[x-1][y]== 'b':
                            gamefield[x-1][y]=field[x-1][y]
                    if x+1<sizel:
                        if field[x+1][y]=='0' and gamefield[x+1][y]=='■':
                            gamefield[x+1][y]=field[x+1][y]
                            xy.append(y)
                            xy.append(x+1)
                        elif field[x+1][y]=='1'or field[x+1][y]=='2'or field[x+1][y]=='3'or field[x+1][y]=='4'or field[x+1][y]=='5'or field[x+1][y]=='6'or field[x+1][y]=='7'or field[x+1][y]=='8' and not field[x+1][y]== 'b':
                            gamefield[x+1][y]=field[x+1][y]
                    if y+1<len(field[0]):
                        if field[x][y+1]=='0' and gamefield[x][y+1]=='■':
                            gamefield[x][y+1]=field[x][y+1]
                            xy.append(y+1)
                            xy.append(x)
                        elif field[x][y+1]=='1'or field[x][y+1]=='2'or field[x][y+1]=='3'or field[x][y+1]=='4'or field[x][y+1]=='5'or field[x][y+1]=='6'or field[x][y+1]=='7'or field[x][y+1]=='8' and not field[x][y+1]== 'b':
                            gamefield[x][y+1]=field[x][y+1]
                    if y-1>=0:
                        if field[x][y-1]=='0' and gamefield[x][y-1]=='■':
                            gamefield[x][y-1]=field[x][y-1]
                            xy.append(y-1)
                            xy.append(x)
                        elif field[x][y-1]=='1'or field[x][y-1]=='2'or field[x][y-1]=='3'or field[x][y-1]=='4'or field[x][y-1]=='5'or field[x][y-1]=='6'or field[x][y-1]=='7'or field[x][y-1]=='8' and not field[x][y-1]== 'b':
                            gamefield[x][y-1]=field[x][y-1]
                    if x-1>=0 and y-1>=0:
                        if field[x-1][y-1]=='0' and gamefield[x-1][y-1]=='■':
                            gamefield[x-1][y-1]=field[x-1][y-1]
                            xy.append(y-1)
                            xy.append(x-1)
                        elif field[x-1][y-1]=='1'or field[x-1][y-1]=='2'or field[x-1][y-1]=='3'or field[x-1][y-1]=='4'or field[x-1][y-1]=='5'or field[x-1][y-1]=='6'or field[x-1][y-1]=='7'or field[x-1][y-1]=='8' and not field[x-1][y-1]== 'b':
                            gamefield[x-1][y-1]=field[x-1][y-1]
                    if x-1>=0 and y+1<len(field[0]):
                        if field[x-1][y+1]=='0' and gamefield[x-1][y+1]=='■':
                            gamefield[x-1][y+1]=field[x-1][y+1]
                            xy.append(y+1)
                            xy.append(x-1)
                        elif field[x-1][y+1]=='1'or field[x-1][y+1]=='2'or field[x-1][y+1]=='3'or field[x-1][y+1]=='4'or field[x-1][y+1]=='5'or field[x-1][y+1]=='6'or field[x-1][y+1]=='7'or field[x-1][y+1]=='8' and not field[x-1][y+1]== 'b':
                            gamefield[x-1][y+1]=field[x-1][y+1]
                    if x+1<sizel and y-1>=0:
                        if field[x+1][y-1]=='0' and gamefield[x+1][y-1]=='■':
                            gamefield[x+1][y-1]=field[x+1][y-1]
                            xy.append(y-1)
                            xy.append(x+1)
                        elif field[x+1][y-1]=='1'or field[x+1][y-1]=='2'or field[x+1][y-1]=='3'or field[x+1][y-1]=='4'or field[x+1][y-1]=='5'or field[x+1][y-1]=='6'or field[x+1][y-1]=='7'or field[x+1][y-1]=='8' and not field[x+1][y-1]== 'b':
                            gamefield[x+1][y-1]=field[x+1][y-1]
                    if x+1<sizel and y+1<len(field[0]):
                        if field[x+1][y+1]=='0' and gamefield[x+1][y+1]=='■':
                            gamefield[x+1][y+1]=field[x+1][y+1]
                            xy.append(y+1)
                            xy.append(x+1)
                        elif field[x+1][y+1]=='1'or field[x+1][y+1]=='2'or field[x+1][y+1]=='3'or field[x+1][y+1]=='4'or field[x+1][y+1]=='5'or field[x+1][y+1]=='6'or field[x+1][y+1]=='7'or field[x+1][y+1]=='8' and not field[x+1][y+1]== 'b':
                            gamefield[x+1][y+1]=field[x+1][y+1]
                    xy.remove(y)
                    xy.remove(x)
                    repeat=len(xy)/2
    xy.clear()

def checkwin():
    sqfl=0
    bombs=0
    for i in range(len(gamefield)):
        for j in range(len(gamefield[i])):
            if gamefield[i][j]=='■':
                sqfl+=1
            if 'f' in gamefield[i]:
                if gamefield[i][j]=='f':
                    sqfl+=1
            if field[i][j]=='b':
                bombs+=1
    if sqfl==bombs:
        print('You won!')
        return True
    else:
        return False

if field_size==1:
    sizel=8
    gen_field(8,8,10)
elif field_size==2:
    sizel=20
    gen_field(20,20,40)
elif field_size==3:
    sizel=30
    gen_field(30,16,99)
else:
    length=int(input('Input field width: '))
    width=int(input('Input field length: '))
    mines=int(input('Input amount of mines on field: '))
    while mines>=length*width:
        print('You entered the wrong amount of bombs on the field.')
        mines=int(input('Input amount of mines on field: '))
    sizel=length
    gen_field(length,width,mines)

while win==False:
    show(gamefield)
    choose()
    win=checkwin()
raise SystemExit

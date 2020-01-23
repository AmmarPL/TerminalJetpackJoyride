import numpy as np
import random
import signal
import time
import os
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from colorama import Fore, Back, Style
from coins import coins
from variables import *
from obstacles import *
from bullet import *
from dragon import dragon
from mandalorian import Mandy


board=[]
objboard=[]
ogoglist=[]
magboard=[]
length=150
height=43
bh=[]
bv=[]
bd=[]
bc=[]
bm=[]
bb=[]
bdb=[]




space=emptyspace()

for i in range(height):
    board.append([])
    objboard.append([])
    magboard.append([])
    for j in range(length):
        board[i].append(' ')
        objboard[i].append(space)
        magboard[i].append([0,0])

board=np.array(board)
# objboard=np.array(board)




# bh.append(beamhorizontal(200,20,6))
# bv.append(beamvertical(180,30,4))
bossarea=450

def createbeams():
    for i in range(5):
        bh.append(beamhorizontal(random.randint(60,bossarea),random.randint(1,height-5),random.randint(5,10),bh))
        bv.append(beamvertical(random.randint(60,bossarea),random.randint(1,height-7),random.randint(4,6),bv))
        bd.append(beamdiagonal(random.randint(60,bossarea),random.randint(1,height-7),random.randint(4,6),bd))

def createcoins():
    for i in range(20):
        bc.append(coins(random.randint(60,bossarea),random.randint(1,height-5),bc))  

def createmagnets():
    for i in range(5):
        bm.append(magnet(random.randint(60,bossarea),random.randint(1,height-5),bm)) 
        x=bm[i].x
        y=bm[i].y
        for i in range(max(1,x-10),min(length,x+10)):
            for j in range(max(3,y-10),min(height-3,y+10)):
                magboard[j][i][0]=y
                magboard[j][i][1]=x




createbeams()
createcoins()
createmagnets()
boss=dragon()

boi=Mandy()
# tcheck=0



def move(shieldt,framedelay,boostsleft):
    def alarmhandler(signum, frame):
        ''' input method '''
        raise AlarmException
    def user_input(timeout=framedelay):
        # tcheck+=0.05
        # if(tcheck==0.1):
            # tcheck=0
            # return ''
        ''' input method '''
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''

    char = user_input()
    if char=='d':
        if boi.getx()<length-3:
            boi.moveh(boi.getx()+2)
    if char=='a':
        if boi.getx()>3:
            boi.moveh(boi.getx()-2)
 
    if char=='w':
        if boi.gety()>1:
            boi.changespeed(boi.getyv()-1)
    
    if char =='k':
        if(time.time()-shieldt>=60):
            shieldt=time.time()
            boi.setshield(1)
    if char =='p' and boostsleft>0:
        boostsleft-=1
        if(framedelay==0.15):
            framedelay=0.075
        else:
            framedelay=0.15
    if char ==' ':
        bb.append(bullet(boi.getx(),boi.gety(),bb))
        
    if(magboard[boi.gety()][boi.getx()][0]!=0):
        if(magboard[boi.gety()][boi.getx()][0]>boi.gety()):
            boi.changespeed(boi.getyv()+1)
        elif(magboard[boi.gety()][boi.getx()][0]<boi.gety()):
            boi.changespeed(boi.getyv()-1)
        if(magboard[boi.gety()][boi.getx()][1]>boi.getx()):
            boi.moveh(boi.getx()+1)
        elif(magboard[boi.gety()][boi.getx()][1]<boi.getx()):
            boi.moveh(boi.getx()-1)


    boi.movey(boi.gety()+min(boi.getyv(),4))
    boi.movey(min(40,boi.gety()))
    boi.movey(max(3,boi.gety()))
    boi.moveh(min(length-1,boi.getx()))
    if(boi.gety()==3):
        boi.changespeed(0)
    boi.checkcollisions(board,objboard,ogoglist)

    if char == 'q':
        quit()
    return shieldt,framedelay,boostsleft
    


os.system('clear')
board[1][1]='['
board[height-1][length-1]=']'
for i in range(length):
    board[height-1][i]= '^'
    board[0][i]='~'
ogoglist=board.copy()
# boi.putonmap()



# bh[0].putonmap()
# bv[0].putonmap()
print(Fore.MAGENTA,end="")
for i in range(2,height):
    for j in range(1,length+1):
        # print(board[i][j],end="")
        # if board[i-1][j-1]!=oglist[i-1][j-1]:
            # if(i!=0):
                print("\033["+str(i)+";"+str(j)+"H"+board[i-1][j-1],end="")
print(Style.RESET_ALL,end="")
print(Fore.WHITE+Back.BLUE,end="")
for i in range(1,2):
    for j in range(1,length+1):
        # print(board[i][j],end="")
        # if board[i-1][j-1]!=oglist[i-1][j-1]:
            # if(i!=0):
                print("\033["+str(i)+";"+str(j)+"H"+board[i-1][j-1],end="")
print(Style.RESET_ALL,end="")
print(Fore.RED+Back.GREEN,end="")
for i in range(height,height+1):
    for j in range(1,length+1):
        # print(board[i][j],end="")
        # if board[i-1][j-1]!=oglist[i-1][j-1]:
            # if(i!=0):
                print("\033["+str(i)+";"+str(j)+"H"+board[i-1][j-1],end="")
print(Style.RESET_ALL,end="")

x=time.time()
boostsleft=6
timeremaining=150
timeelapsed=time.time()
shieldt=time.time()-60
framedelay=0.15
prevshot=time.time()
while True:
    if(time.time()-x>=framedelay):
        if time.time()-timeelapsed>=1:
            timeelapsed=time.time()
            timeremaining-=1    
            print('\033[2;30HTime remaining:'+str(timeremaining)+' ',end='')
            if timeremaining<0:
                quit()

        oglist=board.copy()
        print('\033[2;15HScore:'+str(boi.score)+' ',end='')
        print('\033[2;50HLives:'+str(boi.lives)+' ',end='')
        print('\033[2;65HShield:'+str(int(time.time()-shieldt))+' ',end='')
        print('\033[2;85HBosslives:'+str(boss.lives)+' ',end='')
        # print('\033[2;100HBosslives:'+str(len(bb))+' ',end='')
        # print(bb)
        boi.removefrommap(board,objboard,ogoglist)
        if(boi.getshield()==1 and time.time()-shieldt>=10):
            boi.setshield(0)
        if(boi.gety()<height-3):
            boi.changespeed(boi.getyv()+0.5)
        else:
            boi.changespeed(0)
        shieldt,framedelay,boostsleft = move(shieldt,framedelay,boostsleft)
        # os.system('clear')
        boi.putonmap(board,objboard)


        for i in bh:
            i.removefrommap(board,objboard,ogoglist)
            i.x-=1
            i.putonmap(board,objboard)
        
        for i in bv:
            i.removefrommap(board,objboard,ogoglist)
            i.x-=1
            i.putonmap(board,objboard)

        for i in bd:
            i.removefrommap(board,objboard,ogoglist)
            i.x-=1
            i.putonmap(board,objboard)

        for i in bc:
            i.removefrommap(board,objboard,ogoglist)
            i.x-=1
            i.putonmap(board,objboard)    
        for i in bm:
            i.removefrommap(board,magboard,ogoglist)
            i.x-=1
            i.putonmap(board,magboard)
        for i in bb:
            i.removefrommap(board,objboard,ogoglist)
            i.x+=6
            i.checkcollisions(board,objboard,ogoglist)
        for i in bdb:
            i.removefrommap(board,objboard,ogoglist)
            i.x-=3
            i.putonmap(board,objboard)

        boss.removefrommap(board,objboard,ogoglist)
        if(boi.gety()>boss.y):
            boss.y+=1
        else:
            boss.y-=1
        if(boss.x>110):
            boss.x-=1
        else:
            # print (prevshot,time.time(),end="")
            if time.time()-prevshot>=1:
                prevshot=time.time()
                bdb.append(dragonball(boss.x,boss.y+7,bdb))
                
        boss.y=max(3,boss.y)
        boss.y=min(29,boss.y)
        boss.putonmap(board,objboard)

        


        print(Fore.YELLOW,end="")
        for i in range(2,height):
            for j in range(1,length+1):
                # print(board[i][j],end="")
                if board[i-1][j-1]!=oglist[i-1][j-1]:
                    if(i!=0):
                        print("\033["+str(i)+";"+str(j)+"H"+board[i-1][j-1],end="")
        print(Style.RESET_ALL,end="")
        print(Fore.WHITE+Back.BLUE,end="")
        for i in range(1,2):
            for j in range(1,length+1):
                # print(board[i][j],end="")
                if board[i-1][j-1]!=oglist[i-1][j-1]:
                    if(i!=0):
                        print("\033["+str(i)+";"+str(j)+"H"+board[i-1][j-1],end="")
        print(Style.RESET_ALL,end="")
        print(Fore.RED+Back.GREEN,end="")
        for i in range(height,height+1):
            for j in range(1,length+1):
                # print(board[i][j],end="")
                if board[i-1][j-1]!=oglist[i-1][j-1]:
                    if(i!=0):
                        print("\033["+str(i)+";"+str(j)+"H"+board[i-1][j-1],end="")
        print(Style.RESET_ALL,end="")

        x=time.time()
        print("\033[40;1H",end="")

        print("")



# for i in range(100):
#     for j in range(100):
#         print("\033["+str(i)+";"+str(j)+"Hc",end='')
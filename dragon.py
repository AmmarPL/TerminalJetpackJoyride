from variables import *
class dragon:
    def __init__(self):
        self.name="dragon"
        self.x=500
        self.y=height-20
        self.lives=50
        self.boss=[]
        with open("./dragon.txt") as obj:
            for line in obj:
                self.boss.append(line.strip('\n'))
        print(self.boss)
        print(len(self.boss[0]),len(self.boss[1]))
        for i in range(13):
            for j in range(38):
                print(self.boss[i][j],end="")
            print()

    def putonmap(self,board,objboard):
        self.y=int(self.y)
        for i in range(self.y,self.y+13):
                for j in range(self.x,self.x+38):
                    if(j<150):
                        board[i][j]=self.boss[i-self.y][j-self.x]
                        objboard[i][j]=self
    def removefrommap(self,board,objboard,ogoglist):
        self.y=int(self.y)
        for i in range(self.y,self.y+13):
                for j in range(self.x,self.x+38):
                    if(j<150):
                        board[i][j]=ogoglist[i][j]
                        objboard[i][j]=space


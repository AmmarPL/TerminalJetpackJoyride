from variables import *
class beam:
    def __init__(self,x,y,length,group):
        self.group=group
        self.name="beam"
        self.x=x
        self.y=y
        self.length=length

class beamhorizontal(beam):
    def putonmap(self,board,objboard):
        for i in range(self.x,self.x+self.length):
            if i<length and i>0:
                board[self.y][i]='='
                objboard[self.y][i]=self
    def removefrommap(self,board,objboard,ogoglist):
        for i in range(self.x,self.x+self.length):
            if i<length and i>0:
                board[self.y][i]=ogoglist[self.y][i]
                objboard[self.y][i]=space

class beamvertical(beam):
    def putonmap(self,board,objboard):
        for i in range(self.y,self.y+self.length):
            if self.x <length and self.x > 0:
                board[i][self.x]='I'
                objboard[i][self.x]=self
    def removefrommap(self,board,objboard,ogoglist):
        for i in range(self.y,self.y+self.length):
            if self.x <length and self.x > 0:
                board[i][self.x]=ogoglist[i][self.x]
                objboard[i][self.x]=space

class beamdiagonal(beam):
    def putonmap(self,board,objboard):
        j=self.y
        for i in range(self.x,self.x+self.length):
            if i <length and i > 0:
                board[j][i]='\\'
                objboard[j][i]=self
                j+=1
    def removefrommap(self,board,objboard,ogoglist):
        j=self.y
        for i in range(self.x,self.x+self.length):
            if i <length and i > 0:
                board[j][i]=ogoglist[j][i]
                objboard[j][i]=space
                j+=1
class magnet:
    def __init__(self,x,y,group):
        self.name="magnet"
        self.group=group
        self.x=x
        self.y=y
    def putonmap(self,board,magboard):
        if self.x < length and self.x> 0:
            board[self.y][self.x]='M'
            for i in range(max(1,self.x-10),min(length,self.x+10)):
                for j in range(max(3,self.y-10),min(height-3,self.y+10)):
                    magboard[j][i][0]=self.y
                    magboard[j][i][1]=self.x
    def removefrommap(self,board,magboard,ogoglist):
        if self.x < length and self.x> 0:
            board[self.y][self.x]=ogoglist[self.y][self.x]
            for i in range(max(1,self.x-10),min(length,self.x+10)):
                for j in range(max(3,self.y-10),min(height-3,self.y+10)):
                    magboard[j][i][0]=0
                    magboard[j][i][1]=0
from variables import *
class coins:
    def __init__(self,x,y,group):
        self.name="coin"
        self.group=group
        self.x=x
        self.y=y
    def putonmap(self,board,objboard):
        if self.x < length and self.x> 0:
            board[self.y][self.x]='O'
            objboard[self.y][self.x]=self
    def removefrommap(self,board,objboard,ogoglist):
        if self.x < length and self.x> 0:
            board[self.y][self.x]=ogoglist[self.y][self.x]
            objboard[self.y][self.x]=space
from variables import *
class bullet:
    def __init__(self,x,y,group):
        self.name="bullet"
        self.group=group
        self.x=x
        self.y=y
        self.exists=1
    def putonmap(self,board,objboard):
        if self.x < length and self.x> 0:
            board[self.y][self.x]='>'
            objboard[self.y][self.x]=self
    def removefrommap(self,board,objboard,ogoglist):
        if self.x < length and self.x> 0:
            # print('\033['+str(self.y)+';'+str(self.x)+'H:'+str(self.x)+' ',end='')

            # time.   sleep(0.5)
            board[self.y][self.x]=ogoglist[self.y][self.x]
            objboard[self.y][self.x]=space

    def checkcollisions(self,board,objboard,ogoglist):
        self.y=int(self.y)
        if(self.x<150):
            pass
            f=0
            for j in range(self.x-6,self.x+1):
                if objboard[self.y][j].name=="beam" or j>800:
                    objboard[self.y][j].group.remove(objboard[self.y][j])
                    objboard[self.y][j].removefrommap(board,objboard,ogoglist)
                    if self in self.group:
                        self.group.remove(self)
                    f=1
            #         # self.exists=0
                elif objboard[self.y][j].name=="dragon":
                    objboard[self.y][j].lives-=1
                    f=1
                    if self in self.group:
                        self.group.remove(self)
            #         # self.exists=0
                    if objboard[self.y][j].lives<0:
                        quit()
            if f==0:
                self.putonmap(board,objboard)

                    # self.removefrommap()

class dragonball(bullet):
    def __init__(self,x,y,group):
        self.name="bullet"
        self.group=group
        self.x=x
        self.y=y
    def putonmap(self,board,objboard):
        if self.x < length and self.x> 0:
            board[self.y][self.x]='<'
            objboard[self.y][self.x]=self
    def checkcollisions(self):
        pass


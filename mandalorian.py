from variables import *
import numpy as np
class Mandy:
    def __init__(self):
        self.__x=2
        self.name="mandalorian"
        self.lives=5
        self.__group=[]
        self.__y=height-5
        self.__yv=0
        self.score=0 
        self.__shield=0
        self.__shape=np.array([[' ','o',' '],['[','|','\\'],[' ','/',')']])
    def putonmap(self,board,objboard):
        self.__y=int(self.__y)
        for i in range(self.__y,self.__y+3):
            for j in range(self.__x,self.__x+3):
                board[i][j]=self.__shape[i-self.__y][j-self.__x]
                objboard[i][j]=self
                # print("\033["+str(i)+";"+str(j)+"f",end="")
                # print(board[i][j],end="")
    def removefrommap(self,board,objboard,ogoglist):
        self.__y=int(self.__y)
        for i in range(self.__y,self.__y+3):
            for j in range(self.__x,self.__x+3):
                board[i][j]=ogoglist[i][j]
                objboard[i][j]=space
                # print("el1"+ogoglist[i][j],end="")
                # print("\033["+str(i)+";"+str(j)+"f",end="")
                # print(board[i][j],end="")
    
    def checkcollisions(self,board,objboard,ogoglist):
        self.__y=int(self.__y)
        for i in range(self.__y,self.__y+3):
            for j in range(self.__x,self.__x+4):
                if len(objboard[i][j].group)>0:
                    if(objboard[i][j].name=="coin"):
                        self.score+=1
                    elif((objboard[i][j].name=="beam" or objboard[i][j].name=="bullet") and self.__shield==0):
                        self.lives-=1
                        if(self.lives<0):
                            quit()
                    objboard[i][j].group.remove(objboard[i][j])
                    objboard[i][j].removefrommap(board,objboard,ogoglist)
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def moveh(self,x):
        self.__x=x
    def movey(self,y):
        self.__y=y
    def getyv(self):
        return self.__yv
    def changespeed(self,yv):
        self.__yv=yv
    def getshield(self):
        return self.__shield
    def setshield(self,shield):
        self.__shield=shield
        if shield==1:
            self.__shape=np.array([[' ','o','|'],['[','|','|'],[' ','/',')']])
        else:
            self.__shape=np.array([[' ','o',' '],['[','|','\\'],[' ','/',')']])
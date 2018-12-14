
import numpy as np
from colors import Colors
class ImageProcessing:
    def __init__(self,params):
        self.width=params['width']
        self.height=params['height']
        self.playerPos=(0,0)
        self.colors=Colors(params['colors'])
        self.npc=[]#not player unit
        self.cars=[]
        print(type(self.width))
    def checkCarType(self,x,y):
        i_U=3
        i_D=6
        j_L=3
        j_R=3
        color = list(self.imgArr[y][x])
        print(color)
        print(color==self.colors.yellow)
        print(self.colors.yellow[0]==191)
        print(self.colors.yellow)
        print(type(self.colors.yellow)==type(color))
        #print("start color %s" % str(color))
        i,j=y,x
        vert_count_r=0
        horz_count_r=0
        vert_count_b=0
        horz_count_b=0
        vert_count_y=0
        horz_count_y=0
        vert_count_w=0
        horz_count_w=0
        vert_count_bl=0
        horz_count_bl=0
        while(i<i_U):
            if color == self.colors.yellow:
                vert_count_y+=1
            elif color == self.colors.blue:
                 vert_count_b+=1
            elif color == self.colors.red:
                 vert_count_r+=1
            elif color == self.colors.white:
                 vert_count_w+=1
            elif color == self.colors.black:
                 vert_count_bl+=1
            else :break
            i+=1
            color = list(self.imgArr[i][j])
        i=1
        

        while(i<i_D):
            if color == self.colors.yellow:
                vert_count_y+=1
            elif color == self.colors.blue:
                 vert_count_b+=1
            elif color == self.colors.red:
                 vert_count_r+=1
            elif color == self.colors.white:
                 vert_count_w+=1
            elif color == self.colors.black:
                 vert_count_bl+=1
            else :break
            color=list(self.imgArr[y-i][j])
            i+=1
        color =list(self.imgArr[y][x])   
        while(j<j_R):
            if color == self.colors.yellow:
                horz_count_y+=1
            elif color == self.colors.blue:
                 horz_count_b+=1
            elif color == self.colors.red:
                 horz_count_r+=1
            elif color == self.colors.white:
                 horz_count_w+=1
            elif color == self.colors.black:
                 horz_count_bl+=1
            else :break
            color =list(self.imgArr[y][j])
            j+=1
        j=1
        color = list(self.imgArr[y][x])
      
        while(j<j_L):
            if color == self.colors.yellow:
                horz_count_y+=1
            elif color == self.colors.blue:
                 horz_count_b+=1
            elif color == self.colors.red:
                 horz_count_r+=1
            elif color == self.colors.white:
                 horz_count_w+=1
            elif color == self.colors.black:
                 horz_count_bl+=1
            else :break
            color =list(self.imgArr[y][x-j])
            j+=1      
       
        if horz_count_y>2 and vert_count_y>2 and horz_count_w<3 and vert_count_w<3:
            return 'y'#сообщаем что это машина желтого цвета
        if horz_count_b>2 and vert_count_b>2 and horz_count_w<3 and vert_count_w<3:
            return 'b'#сообщаем что это машина cинего цвета
        if horz_count_r>2 and vert_count_r>2 and horz_count_w<3 and vert_count_w<3:
            return 'r'#сообщаем что это машина красного цвета
        if vert_count_w>2 and horz_count_w>2 and vert_count_w<8 and (horz_count_r>0 or vert_count_r
        or horz_count_b>0 or vert_count_b>0 ):
            return 'f'#сообщаем что это машина заправка
        if vert_count_b>2 and horz_count_b>2:
            return 'o'#сообщаем что это пятно масла
        print (horz_count_y ,vert_count_y)
        return None 
        
    def checkCars(self):
        i=5
        route=0#используем контрольную точку для определения условных границ 
        xStart,xEnd = self.roadStart[0][0],self.roadEnd[0][0]
        dutyRoute=self.roadStart[route][1]
        isFoundCar=False
        while(i<175):
            j=xStart
            while(j<xEnd):
                lst =list(self.imgArr[i][j])
                if lst!=self.colors.grey and lst!=self.colors.green:
                    print(lst)
                    carType =self.checkCarType(j,i)
                    if(carType!=None):
                        j+=6
                        self.cars.append({'x':j,'y':i,'t':carType})
                        isFoundCar=True
                j+=2
            if(isFoundCar):
                i+=5
                isFoundCar=False
            i+=2
            if(i>dutyRoute and route+1<len(self.roadStart)):
                route+=1
                dutyRoute=self.roadStart[route][1]
                xStart = self.roadStart[route][0]
                xEnd= self.roadEnd[route][0]
                print("cur i:%d" % i)
              



    def checkProgress(self):        
        progress=0
        for i in range(self.height):
            if(self.imgArr[i][9][0]==228):
                progress=i
                break
        return (self.height-progress)/self.height
    def findMyPos(self):
        i=self.roadStart[4][0]
        lim=self.roadEnd[4][0]
        while(i<lim):
            if(self.imgArr[170][i][0]==228):
               self.playerPos =(i,170)
               break
            i+=2 
        
    def checkRoute(self):
        i=0
        j=65 #j=65 т.к трасса не генерируеться левее этого диапазона
        z=180
        iter =int( self.height/5)
        self.roadStart=[]
        self.roadEnd=[]
        while i<self.height:
            while j<175:
                if (self.imgArr[i][j][0]==128):
                    self.roadStart.append((j,i))
                    break
                j+=2#погрешность в 1 пиксель ничего не даст но ускорит время обработки
            while z>65:     
                if(self.imgArr[i][z][0]==128):
                    self.roadEnd.append((z,i))
                    break
                z-=2
            i+=iter   
    def process(self,imgArr):
        self.imgArr = np.reshape(imgArr,(self.height,self.width,3))
        print(str(self.imgArr[0][1]))
        self.checkRoute()
        self.findMyPos()
        self.checkCars()
        print(self.roadStart)
        print(self.roadEnd)
        print(self.playerPos)
        print(self.cars)
        
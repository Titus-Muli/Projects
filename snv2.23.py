import pygame as pg
import keyboard as kb
import time
import math
import random as rd

pi= math.pi
x= 290; x2= 291; x3= 292; x4= 293; x5= 294; x6= 295; x7= 296; x8= 297; x9= 299; x10= 300
x11= 301; x12= 302; x13= 303; x14= 304; x15= 305; x16= 306; x17= 307; x18= 308; x19= 309; x20= 310
x21= 311; x22= 312; x23= 313; x24= 314; x25= 315; x26= 316; x27= 317; x28= 318; x29= 319; x30= 320
x31= 321; x32= 322; x33= 323; x34= 324; x35= 325; x36= 326; x37= 327; x38= 328; x39= 329; x40= 330
x41= 331; x42= 332; x43= 333; x44= 334; x45= 335; x46= 336; x47= 337; x48= 338; x49= 339; x50= 340
x51= 341; x52= 342; x53= 343; x54= 344; x55= 345; x56= 346; x57= 347; x58= 348; x59= 349; x60= 350
x61= 351; x62= 352; x63= 353; x64= 354; x65= 355; x66= 356; x67= 357; x68= 358; x69= 359; x70= 360
x71= 361; x72= 362; x73= 363; x74= 364; x75= 365; x76= 366; x77= 367; x78= 368; x79= 369; x80= 370


y= 290; y2= 291; y3= 292; y4= 293; y5= 294; y6= 295; y7= 296; y8= 297; y9= 299; y10= 300
y11= 301; y12= 302; y13= 303; y14= 304; y15= 305; y16= 306; y17= 307; y18= 308; y19= 309; y20= 310
y21= 311; y22= 312; y23= 313; y24= 314; y25= 315; y26= 316; y27= 317; y28= 318; y29= 319; y30= 320
y31= 321; y32= 322; y33= 323; y34= 324; y35= 325; y36= 326; y37= 327; y38= 328; y39= 329; y40= 330
y41= 331; y42= 332; y43= 333; y44= 334; y45= 335; y46= 336; y47= 337; y48= 338; y49= 339; y50= 340
y51= 341; y52= 342; y53= 343; y54= 344; y55= 345; y56= 346; y57= 347; y58= 348; y59= 349; y60= 350
y61= 351; y62= 352; y63= 353; y64= 354; y65= 355; y66= 356; y67= 357; y68= 358; y69= 359; y70= 360
y71= 361; y72= 362; y73= 363; y74= 364; y75= 365; y76= 366; y77= 367; y78= 368; y79= 369; y80= 370

AG= 0
CG= pi/14
HD= 0
dca= 0
up= False
speed= 10
stops= [5]
val= 0

ex= rd.randint(30,570)
ey= rd.randint(30,570)
pts= 0
rect= pg.Rect(ex,ex,20,20)     

xyr= [(x, y, x2, y2), (x2, y2, x3, y3), (x3, y3, x4, y4), (x4, y4, x5, y5), (x5, y5, x6, y6), (x6, y6, x7, y7), (x7, y7, x8, y8), (x8, y8, x9, y9), (x9, y9, x10, y10),
      (x10, y10, x11, y11), (x11, y11, x12, y12), (x12, y12, x13, y13), (x13, y13, x14, y14), (x14, y14, x15, y15), (x15, y15, x16, y16), (x16, y16, x17, y17), (x17, y17, x18, y18), (x18, y18, x19, y19), (x19, y19, x20, y20),
      (x20, y20, x21, y21), (x21, y21, x22, y22), (x22, y22, x23, y23), (x23, y23, x24, y24), (x24, y24, x25, y25), (x25, y25, x26, y26), (x26, y26, x27, y27), (x27, y27, x28, y28), (x28, y28, x29, y29), (x29, y29, x30, y30),
      (x30, y30, x31, y31), (x31, y31, x32, y32), (x32, y32, x33, y33), (x33, y33, x34, y34), (x34, y34, x35, y35), (x35, y35, x36, y36), (x36, y36, x37, y37), (x37, y37, x38, y38), (x38, y38, x39, y39), (x39, y39, x40, y40),
      (x40, y40, x41, y41), (x41, y41, x42, y42), (x42, y42, x43, y43), (x43, y43, x44, y44), (x44, y44, x45, y45), (x45, y45, x46, y46),(x46, y46, x47, y47), (x47, y47, x48, y48), (x48, y48, x49, y49), (x49, y49, x50, y50),
      (x50, y50, x51, y51), (x51, y51, x52, y52), (x52, y52, x53, y53), (x53, y53, x54, y54), (x54, y54, x55, y55), (x55, y55, x56, y56), (x56, y56, x57, y57), (x57, y57, x58, y58), (x58, y58, x59, y59), (x59, y59, x60, y60),
      (x60, y60, x61, y61), (x61, y61, x62, y62), (x62, y62, x63, y63), (x63, y63, x64, y64), (x64, y64, x65, y65), (x65, y65, x66, y66), (x66, y66, x67, y67), (x67, y67, x68, y68), (x68, y68, x69, y69), (x69, y69, x70, y70),
      (x70, y70, x71, y71), (x71, y71, x72, y72), (x72, y72, x73, y73), (x73, y73, x74, y74), (x74, y74, x75, y75), (x75, y75, x76, y76), (x76, y76, x77, y77), (x77, y77, x78, y78), (x78, y78, x79, y79), (x79, y79, x80, y80)]

g=0; size=10
xys= []
for g in range(size):
    xys.append(xyr[g])

pg.init()
screen= pg.display.set_mode(size=(600,600))
rect= pg.Rect(x,y,20,20)
pg.draw.arc(screen, (255,0,0),rect,AG,(AG+pi))
pg.display.update()

running= True
while running:
#                  _______________________________________________________
#INPUT MANIPULATION_______________________________________________________|

    def movment(x,y):
        global rect, pts
        screen.fill((50,80,150))
        Rect= pg.Rect(x,y,15,15)
        pg.draw.arc(screen, (255,0,0),Rect,AG,(AG+(2*pi)),7)
        pg.draw.rect(screen,(100,0,100),rect)
        font = pg.font.Font(None, 18)        
        text = font.render(f'Score: {pts}', True, (255, 255, 255))
        text_rect = text.get_rect(center=(560,20))
        screen.blit(text, text_rect)
        pg.display.update()
        parts(x,y)

    def heading(AG):
        global HD        
        if (2.001*pi)>AG>=((3/2)*pi):            
            HD= AG+(pi/2)-2*pi
        else:            
            HD= AG+(pi/2)        
        delta(HD)

    def delta(HD):        
        dx= 10*math.cos(HD)
        dy= 10*math.sin(HD)
        angle(dx,dy)

    def angle(dx,dy):
        global x,y
        x+= dx
        y-= dy        
        movment(x,y)
    
    def main(A):
        global AG, dca, speed      
        r= kb.is_pressed('right')
        l= kb.is_pressed('left')
        u= kb.is_pressed('up')
        d= kb.is_pressed('down')
        if r:            
            if AG>=0:
                AG-=CG                
            elif AG<0:
                AG=2*pi
            if dca<(pi/20):
                dca+= pi/128
            else:
                dca= pi/20
        elif l:
            if AG<=(2*pi):
                AG+=CG                
            elif AG>(2*pi):
                AG=0
            if dca>(-(pi/20)):
                dca-= pi/128
            else:
                dca= -(pi/20)
        else:
            if dca>0:
                dca-= pi/128
            else:
                dca+= pi/128
        heading(AG)            
        time.sleep(1/speed)
        
#                    _____________________________________________________
#REPEATED SNAKE PARTS_____________________________________________________|

    def parts(x,y):
        global xys, dca, colours, running
        con= True
        i=0
        dct= 9
        for (xa,ya,xb,yb) in xys:
            if i==0:
                xa= x
                ya= y
            if xa>=xb and ya>=yb:
                AGb= -1*(math.atan((abs(ya-yb)/abs(xa-xb))))
            elif xa<=xb and ya>=yb:
                AGb= -1*(pi- math.atan((abs(ya-yb)/abs(xa-xb))))
            elif xa<=xb and ya<=yb:
                AGb= -1*(math.atan(((ya-yb)/(xa-xb))) + pi)
            elif xa>=xb and ya<=yb:
                AGb= -1*((2*pi)- math.atan((abs(ya-yb)/abs(xa-xb))))
            leng= math.sqrt(((ya-yb)*(ya-yb))+((xa-xb)*(xa-xb)))                            

            AGb+= dca
            if leng>25:                
                dxb= 11*math.cos(AGb)
                dyb= 11*math.sin(AGb)                
            else:                
                dxb= dct*math.cos(AGb)
                dyb= dct*math.sin(AGb)
                dct-= 0.08*dct
            xb+= dxb
            yb-= dyb                    
            
            rect= pg.Rect(xb,yb,15,15)     
            pg.draw.arc(screen, (255,255,255),rect,(AGb-(pi/2)),(AGb+(pi*1.5)),7)

            xys[i]= (xa,ya,xb,yb)
            if (i+1)<len(xys):
                xysl= list(xys[i+1])
                xys[i+1]= (xb,yb,xysl[2],xysl[3])
                
            if abs(xb-x)<7 and abs(yb-y)<7 and len(xys)>13:
                running= False
                print('FAILURE')
                
            i+=1        
        pg.display.update()        
        eat(x,y)
  
#     ___________________________________________
#SCORE___________________________________________|

    def eat(x,y):
        global pts, ex, ey, rect
        if abs(x-ex)< 24 and abs(y-ey)< 24:
            pts+=1
            ex= rd.randint(30,570)
            ey= rd.randint(30,570)
            up= True
        else:
            up= False
        rect= pg.Rect(ex,ey,20,20)     
        pg.draw.rect(screen,(100,0,100),rect)
        Speed(pts)
#     ___________________________________________
#SPEED___________________________________________|
        
    def Speed(pts):
        global speed, stops, xys, xyr, val
        if pts%5==0 and pts in stops:
            speed+=1.2
            stops[0]= stops[0]+5                    
        elif val<pts:
            speed+=0.4
            xys.append(xyr[len(xys)])
            val= pts
            
#             ____________________________________________________________    
#EXIT SEQUENCE____________________________________________________________|
        
    esc= kb.is_pressed('esc')
    if esc:
        running= False

    if not 10<x<590:
        running= False
    if not 10<y<590:
        running= False
        
    main(1)
    
time.sleep(3)
pg.quit()

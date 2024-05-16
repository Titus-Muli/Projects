import customtkinter as ctk 
import datetime as dt
import time


ctk.set_default_color_theme("blue")


GUI = ctk.CTk()
GUI.geometry("480x360")
GUI.title('KATTiVAH Smart Home GUI')


lights= [('ON',6,30),('OFF',22,30)]
aircon= [(30,5,10),(20,19,45)]
doors= [('OPEN',7,30),('CLOSED',20,30)]
times= [aircon,lights,doors]


deg= 25
lt_buttons = [('All On',50,30,145,280,0),('All Off',50,30,360,280,1),('OFF', 60, 60, 150, 75,2),('OFF', 60, 60, 150, 180,3),
              ('OFF', 60, 60, 370, 75,4),('OFF', 60, 60, 370, 180,5),('BACK', 50, 30, 0, 0,6)]
dr_buttons = [('CLOSED', 120, 60, 180, 150, 0),('BACK', 50, 30, 0, 0,1)]
labstp= [('Adjust The Temperature',140,30),('Increase', 280, 100),('Decrease', 270, 220),(deg, 220, 150),('Temp: ', 150, 150)] 


mod= 'Dark'
lig_dar= '🔆'



#_____________________________________________________________________________________________________________________________________________
#TEMPERATURE WINDOW___________________________________________________________________________________________________________________________

def temp():    
    global deg, labstp, aircon  
    def labelcr(ltp,lx,ly): 
        label = ctk.CTkLabel(GUI, text=ltp, font=('Consolas',20)) 
        label.place(x=lx, y=ly)
        return label


    labelstp= []
    for (ltp,lx,ly) in labstp:
        label= labelcr(ltp,lx,ly)
        labelstp.append(label)    


    label= ctk.CTkLabel(GUI, text=f'Air conditioning will change to:\n{aircon[0][0]}° at {aircon[0][1]}:{aircon[0][2]}\n{aircon[1][0]}° at {aircon[1][1]}:{aircon[1][2]}',font=('Consolas',12)) 
    label.place(x=120, y=290) 
    labelstp.append(label)


    def change(i):
        global deg, labstp
        if i== 2 and deg<40:
            deg+=1
        elif i== 3 and deg>10:
            deg-=1
        elif i== 0:
            deg= 40
        elif i== 1:
            deg= 10

        lab= list(labstp[3])
        lab[0]= deg
        labstp[3]= lab
        new_t(lab)


    def back_t():
        for but in buttonstp:
            but.destroy()
        for lab in labelstp:
            lab.destroy()
        login()


    def new_t(nw):
        label= labelcr(nw[0],nw[1],nw[2])
        labelstp.append(label)


    def create_temp(text, w, h, bx, by, e):
        if e== 4:
            button = ctk.CTkButton(GUI, text=text, width=w, height=h, font=('Consolas',20), command=lambda: back_t())
            button.place(x=bx, y=by)
        else:
            button = ctk.CTkButton(GUI, text=text, width=w, height=h, font=('Consolas',20), command=lambda: change(e))
            button.place(x=bx, y=by)
        return button


    tp_buttons = [('High', 70, 30, 60, 100,0),('Low', 70, 30, 60, 220,1),('Ʌ', 60, 60, 370, 85,2),('V', 60, 60, 370, 205,3),('BACK', 50, 30, 0, 0,4)]
    buttonstp = []
    for (text, w, h, bx, by, e) in tp_buttons:
        button = create_temp(text, w, h, bx, by, e)
        buttonstp.append(button)




#_____________________________________________________________________________________________________________________________________________
#LIGHTS WINDOW________________________________________________________________________________________________________________________________

def light():
    global lt_buttons

    labslt= [('Which lights do you want to switch?',90,30),('Living\nroom',50,80),('Kitchen',50,190),('Bedroom',270,80),('Toilet /\nBathroom',270,190)]
    labelslt= []
    for (llt,lx,ly) in labslt:
        label = ctk.CTkLabel(GUI, text=llt, font=('Consolas',20))
        label.place(x=lx, y=ly)
        labelslt.append(label)


    nt_label= ctk.CTkLabel(GUI, text=f'Lights will turn:\nON at {lights[0][1]}:{lights[0][2]}\nOFF at {lights[1][1]}:{lights[1][2]}',font=('Consolas',12)) 
    nt_label.place(x=20, y=300)
    labelslt.append(nt_label)


    def switch_l(e):
        global lt_buttons
        states= ['ON','OFF']
        lights= [2,3,4,5]

        
        if e in lights:
            butt= list(lt_buttons[e])
            if butt[0]== states[0]:
                butt[0]= states[1]
            else:
                butt[0]= states[0]
            lt_buttons[e]= butt
            new_l(butt)


        else:
            for i in lights:
                butt= list(lt_buttons[i])
                butt[0]= states[e]
                lt_buttons[i]= butt
                new_l(butt)


    def back_l():
        for but in buttonslt:
            but.destroy()
        for lab in labelslt:
            lab.destroy()
        login()


    def new_l(nw):
        button= create_light(nw[0],nw[1],nw[2],nw[3],nw[4],nw[5])
        buttonslt.append(button)


    def create_light(text, w, h, bx, by, e):        
        if e== 6:
            button = ctk.CTkButton(GUI, text=text, width=w, height=h, font=('Consolas',20), command=lambda: back_l())
            button.place(x=bx, y=by)
        else:
            button = ctk.CTkButton(GUI, text=text, width=w, height=h, font=('Consolas',20), command=lambda: switch_l(e))
            button.place(x=bx, y=by)
        return button    


    buttonslt = []
    for (text, w, h, bx, by, e) in lt_buttons:
        button = create_light(text, w, h, bx, by, e)
        buttonslt.append(button)



#_____________________________________________________________________________________________________________________________________________
#FRONT DOOR WINDOW____________________________________________________________________________________________________________________________

def door():
    global dr_buttons,doors

    dr_label = ctk.CTkLabel(GUI, text="Lock or Unlock the main door?", font=('Consolas',20))
    dr_label.place(x=100, y=50)


    nt_label= ctk.CTkLabel(GUI, text=f'The door will:\nUNLOCK at {doors[0][1]}:{doors[0][2]}\nLOCK at {doors[1][1]}:{doors[1][2]}',font=('Consolas',12)) 
    nt_label.place(x=195, y=270)     


    def back_d():
        for but in buttonsdr:
            but.destroy()
        dr_label.destroy()
        nt_label.destroy()
        login()


    def switch_d(e):
        global dr_buttons
        states= ['OPEN','CLOSED']
        butt= list(dr_buttons[e])


        if butt[0]== states[0]:
            butt[0]= states[1]
        else:
            butt[0]= states[0]

            
        dr_buttons[e]= butt
        new_d(butt)


    def new_d(nw):
        button= create_door(nw[0],nw[1],nw[2],nw[3],nw[4],nw[5])
        buttonsdr.append(button)
    
        
    def create_door(text, w, h, bx, by, e):
        if e== 1:
            button = ctk.CTkButton(GUI, text=text, width=w, height=h, font=('Consolas',20), command=lambda: back_d())
            button.place(x=bx, y=by)
        else:
            button = ctk.CTkButton(GUI, text=text, width=w, height=h, font=('Consolas',20), command=lambda: switch_d(e))
            button.place(x=bx, y=by)
        return button    


    buttonsdr = []
    for (text, w, h, bx, by, e) in dr_buttons:
        button = create_door(text, w, h, bx, by, e)
        buttonsdr.append(button)



#_____________________________________________________________________________________________________________________________________________
#SCHEDULES WINDOW___________________________________________________________________________________________________________________________

def schedule(e):
    global themes, lights, doors, aircon, times    

    
    cats= ['AIR CONDITIONING','LIGHTS','MAIN DOOR']
    sh_labels= [('Set \nTemperature', 10, 170),('Turn ON at\t  Turn OFF at',120,135),('OPEN  at   \t   CLOSED  at', 120, 135)]
    sh_default= [('Time',30,100),(f"SET  {cats[e]}\n  SCHEDULE",150,20),(':',160,100),(':',360,100),('|',270,90),('|',270,110),('|',270,190),('|',270,170)]


    labelssh= []
    for (text,lx,ly) in sh_default:
        label = ctk.CTkLabel(GUI, text=text, font=('Consolas',20))
        label.place(x=lx, y=ly)
        labelssh.append(label)


    label = ctk.CTkLabel(GUI, text=sh_labels[e][0], font=('Consolas',20))
    label.place(x=sh_labels[e][1], y=sh_labels[e][2])
    labelssh.append(label)


    def back_s(menu):
        for but in buttonssh:
            but.destroy()
        for lab in labelssh:
            lab.destroy()
        for ent in entryssh:
            ent.destroy()
        menu()


    def clear(menu):
        for widget in GUI.winfo_children():
            widget.destroy()
        menu()
        

    def pack(_):
        global aircon, lights, doors
        menus= [aircon,lights,doors]
        adjustment= menus[e]
        
        fir= []
        sec= []
        i=0

        
        for ent in entryssh:
            if i<(len(entryssh)/2):
                new_ent= ent.get()
                fir.append(new_ent)
            else:
                new_ent= ent.get()
                sec.append(new_ent)
            i+=1


        for _ in range(4):
            if '' in fir:
                fir[fir.index('')]= 0
            if '' in sec:
                sec[sec.index('')]= 0
        h1,m1,h2,m2= fir[0],fir[1],sec[0],sec[1]


        if e==0:
            t1,t2= fir[2],sec[2]
            aircon= [(m2,h1,m1),(t2,t1,h2)]
        elif e==1:
            lights= [(adjustment[0][0],h1,m1),(adjustment[1][0],h2,m2)]
        elif e==2:
            doors= [(adjustment[0][0],h1,m1),(adjustment[1][0],h2,m2)]
        change()


    def adjust(state):
        global deg, lt_buttons, dr_buttons

        if e == 0:
            state= int(state)
            if state<10:
                state=10
            elif state>40:
                state=40
            labstp[3]= (state,labstp[3][1],labstp[3][2])
            deg= state
            menu= temp

            
        elif e == 1:
            lights = [2, 3, 4, 5]
            for x in lights:
                lt_buttons[x]= (state,lt_buttons[x][1],lt_buttons[x][2],
                                lt_buttons[x][3],lt_buttons[x][4],lt_buttons[x][5])
            menu= light

        
        elif e == 2:
            dr_buttons[0]= (state,dr_buttons[0][1],dr_buttons[0][2],
                            dr_buttons[0][3],dr_buttons[0][4],dr_buttons[0][5])
            menu= door
        clear(menu)


    def change():
        global aircon, lights, doors, deg
        
        menus= [aircon,lights,doors]
        adjustment= menus[e]
        
        cur_time = dt.datetime.now()
        cur_hour = cur_time.hour
        cur_min = cur_time.minute

        
        now= int(f'{cur_hour}{cur_min}')
        time1= int(f'{adjustment[0][1]}{adjustment[0][2]}')
        time2= int(f'{adjustment[1][1]}{adjustment[1][2]}')

        if now==time1:
            state= adjustment[0][0]
            adjust(state)
        elif now==time2:
            state= adjustment[1][0]
            adjust(state)
        else:
            login()

        GUI.after(60000, change)

    
    if e==1:
        sh_entrys= [(40,120,100),(50,170,100),(40,320,100),(50,370,100)]        
        plho= [lights[0][1],lights[0][2],lights[1][1],lights[1][2]]
    elif e==2:
        sh_entrys= [(40,120,100),(50,170,100),(40,320,100),(50,370,100)]
        plho= [doors[0][1],doors[0][2],doors[1][1],doors[1][2]]
    else:
        sh_entrys= [(40,120,100),(50,170,100),(40,320,100),(50,370,100),(60,150,180),(60,350,180)]
        plho= [aircon[0][1],aircon[0][2],aircon[1][1],aircon[1][2],aircon[0][0],aircon[1][0]]
        

    entryssh= []
    p=0
    for (w,ex,ey) in sh_entrys:
        entry= ctk.CTkEntry(GUI, placeholder_text=plho[p], width=w)
        entry.place(x=ex, y=ey)
        entryssh.append(entry)
        p+=1


    def create_schedule(text,w,h,bx,by,func,menu):
        global themes
        button = ctk.CTkButton(GUI, text=text, width=w, height=h, font=('Consolas',20), command=lambda: func(menu))
        button.place(x=bx, y=by)
        return button


    sh_buttons= [('Save',80,50,220,260,pack,None),('BACK', 50, 30, 0, 0,back_s,login)]
    buttonssh= []
    for (text,w,h,bx,by,func,menu) in sh_buttons:
        button= create_schedule(text,w,h,bx,by,func,menu)
        buttonssh.append(button)    

    change()


#_____________________________________________________________________________________________________________________________________________
#LOGIN WINDOW_________________________________________________________________________________________________________________________________

def login():
    global mod, lig_dar    
    
    lg_label = ctk.CTkLabel(GUI, text="Welcome\n What would you like to change?", font=('Consolas',20))
    lg_label.place(x=35, y=10)


    def switch(menu,e):
        for but in buttonslg:
            but.destroy()
        lg_label.destroy()
        if menu== schedule:
            menu(e)
        else:
            menu()


    def create(text, w, h, bx, by, menu,e):
        sizes= [15,15,15,20,20,20]
        button = ctk.CTkButton(GUI, text=text, width=w, height=h, font=('Consolas',sizes[e]), command=lambda: switch(menu,e))
        button.place(x=bx, y=by)
        return button


    def mode():
        global lig_dar, mod       
        states= ['🔆','🌙']

        
        if lig_dar == states[0]:
            lig_dar = states[1]
            mod= "Light"
        else:
            lig_dar= states[0]
            mod= "Dark"        


        trans= 1
        for _ in range(4):            
            trans-=0.25
            GUI.attributes("-alpha", trans)
            time.sleep(0.05)
        
        ctk.set_appearance_mode(mod)

        for _ in range(4):            
            trans+=0.25
            GUI.attributes("-alpha", trans)
            time.sleep(0.05)
            
        lg()
        

    lg_buttons = [('Air Conditioning', 180, 50, 100, 80, temp,3),('Light Switches', 180, 50, 100, 160, light,4),
                  ('Front Door', 180, 50, 100, 240, door,5),
                  ('Schedule',8,20,360,90,schedule,0),
                  ('Schedule',8,20,360,170,schedule,1),('Schedule',8,20,360,250,schedule,2)]

    
    buttonslg = []
    for (text, w, h, bx, by, menu,e) in lg_buttons:
        button = create(text, w, h, bx, by, menu,e)
        buttonslg.append(button)


    def lg():
        global lig_dar
        button = ctk.CTkButton(GUI, text=lig_dar, width=20, height=20, font=('Consolas',30), command=lambda: mode())
        button.place(x=385, y=15)
        buttonslg.append(button)

    lg()

login()

GUI.mainloop()

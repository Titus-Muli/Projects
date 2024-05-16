import customtkinter as ctk

pos= ctk.CTk()
pos.geometry('300x240')

products= [[['Bread',65],[10,0]],[['Milk',60],[10,0]],[['Egg',15],[50,0]],[['Soda',40],[20,0]],[['Apple',45],[20,0]],[['Biscuits',35],[20,0]]]
users= ['Caleb','Titus','Abby']
user= None
e_new= 0

class menus():
    def __init__(self,buttons,labels,combos,scrolls,segments,extra):        
        self.buttons= buttons
        self.labels= labels
        self.combos= combos
        self.segments= segments
        self.scrolls= []
        self.items= []
        self.extra= extra
        self.names= [name for [[name,price],[available,sold]] in self.extra]
        self.prices= [price for [[name,price],[available,sold]] in self.extra]

        for (coor,size,text_funcs) in scrolls:
            self.scrolls.append([coor,size])
            self.items.append(text_funcs)
        
        self.label_storage= []
        self.button_storage= []
        self.combo_storage= []
        self.segment_storage= []
        self.scroll_storage= [] ; self.scroll_items= []

    def destroy(self,thing):
        thing.destroy()
        

    def open_new_window(self,menu):
        global e_new
        e_new= 0
        menu(self)
        
        for but in self.button_storage:
            but.destroy()
        for lab in self.label_storage:
            lab.destroy()
        for com in self.combo_storage:
            com.destroy()
        for scr in self.scroll_storage:
            scr.destroy()
        for ite in self.scroll_items:
            ite.destroy()
        for seg in self.segment_storage:
            seg.destroy()

    def create_segments(self,values,coor,size,e):
        segment= ctk.CTkSegmentedButton(pos,size[0],size[1],values= values)
        segment.set(values[0])
        segment.place(x= coor[0],y= coor[1])
        return segment

    def call_create_segments(self):
        for (values,coor,size,e) in self.segments:
            segment= self.create_segments(values,coor,size,e)            
            self.segment_storage.append(segment)

    def create_labels(self):        
        for (text,coor) in self.labels:
            label = ctk.CTkLabel(pos, text=text)
            label.place(x=coor[0], y=coor[1])
            self.label_storage.append(label)

    def create_buttons(self,text,coor,size,menu,state,new,e):
        if new== 'yes':            
            button = ctk.CTkButton(pos, text=text, width=size[0], height=size[1], state=state, command= lambda: self.open_new_window(menu))
            
        elif new== 'no':
            button = ctk.CTkButton(pos, text=text, width=size[0], height=size[1], state=state, command= lambda: menu(self,e,text))
            
        button.place(x=coor[0], y=coor[1])
        return button

    def call_create_buttons(self):
        for (text,coor,size,menu,state,new,e) in self.buttons:
            button = self.create_buttons(text,coor,size,menu,state,new,e)
            self.button_storage.append(button)

    def create_combos(self,values,coor,size,default,func,e):
        combo= ctk.CTkComboBox(pos,size[0],size[1],values= values)
        combo.set(default)        
        combo.place(x= coor[0],y= coor[1])
        return combo

    def call_create_combos(self):
        for (values,coor,size,default,func,e) in self.combos:
            combo= self.create_combos(values,coor,size,default,func,e)
            self.combo_storage.append(combo)

    def create_scroll_items(self,text,num,func,e):
        price= self.prices[self.names.index(text)] #5a0f78, 464696
        item= ctk.CTkButton(self.scroll,text=f'{text}\tx{num}\t= Ksh {num*price}',fg_color= '#325096',command= lambda: func(self,e,'items'))
        item.pack(pady=5)
        self.scroll_items.append(item)

    def create_scrolls(self):        
        for (coor,size) in self.scrolls:
            self.scroll= ctk.CTkScrollableFrame(pos,width=size[0],height=size[1])
            self.scroll.place(x=coor[0],y=coor[1])            
            self.scroll_storage.append(self.scroll)

def product_checker(self,e,store):
    new= [combo.get() for combo in self.combo_storage][0]
    if new!= 'Choose Product':        
        item_stuff(self,e,store)

def item_stuff(self,e,store):
    global e_new

    for but in self.button_storage:
        but.configure(state= 'normal')
    
    if self.items[0]== []:
        self.items.pop(0)

    new= [combo.get() for combo in self.combo_storage][0]
    items= [product[0] for product in self.items]

    if store== 'Add':
        x=1
    elif store== 'Less':
        x=-1
    
    if store== 'items':
        item= items[e]
        print(f'{item} pressed')
        self.combo_storage[0].set(item)
        for ite in self.scroll_items:
            ite.configure(fg_color= '#325096')
        self.scroll_items[e].configure(fg_color= '#464696')
        
        
    elif new!= 'Choose Product':
        if new in items:                    
            if self.items[items.index(new)][1]>1 or x==1:
                self.items[items.index(new)][1]+= x

            text= self.items[items.index(new)]
            price= self.prices[self.names.index(text[0])]
            self.scroll_items[items.index(new)].configure(text= f'{text[0]}\tx{text[1]}\t= Ksh {text[1]*price}')
            
        else:
            self.items.append([new,1,item_stuff,e_new])
            self.create_scroll_items(new,1,item_stuff,e_new)                        
            e_new+=1
            print(f'{new} added')

def user_checker(self):
    global users
    user= [combo.get() for combo in self.combo_storage][0]

    if user in users:
        working_window(self)
    else:
        select_user('_Select a User from those Below_')

def working_window(self):
    global products
    
    pos.geometry('500x400')

    prices= [price for [[name,price],[available,sold]] in products]
    items= [name for [[name,price],[available,sold]] in products]
    methods= ['Mpesa','Cash']
    
    working_combos= [[items,[30,40],[240,40],'Choose Product',item_stuff,0]]
    
    working_buttons= [['Search',[290,40],[85,30],working_window,'disabled','yes',0],
                      ['Add',[385,40],[85,30],product_checker,'normal','no',1],
                      ['Less',[385,80],[85,30],product_checker,'disabled','no',1],
                      ['Buy',[290,320],[180,40],working_window,'disabled','yes',2]]

    working_labels= [['Choose a Payment Method Below',[280,220]]]

    working_segments= [[methods,[330,250],[180,40],0]]
    
    working_scrolls= [[[30,90],[220,200],[]]]

    working= menus(working_buttons,working_labels,working_combos,working_scrolls,working_segments,products)

    working.call_create_combos()    
    working.call_create_buttons()
    working.create_scrolls()
    working.create_labels()
    working.call_create_segments()
    
def select_user(message):
    global users
    
    pos.geometry('300x240')

    user_combos= [[users,[60,60],[180,40],'Select Cashier',item_stuff,0]]
    user_buttons= [['Save',[60,140],[180,40],user_checker,'normal','yes',0]]

    user_labels= [[message,[50,20]]]
    
    select= menus(user_buttons,user_labels,user_combos,[],[],[])
    
    select.call_create_combos()
    select.call_create_buttons()
    select.create_labels()

select_user('   _Pick One of the Users Below_')

pos.mainloop()

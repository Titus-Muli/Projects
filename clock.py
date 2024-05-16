import time
import customtkinter as ctk

clock = ctk.CTk()
clock.geometry('120x50')
clock.title('my clock')

def splitter(ARRAY, SPLIT):
    sections= []
    remaining= True
    while remaining:
        word= []; i= 0
        if SPLIT in ARRAY:
            gap= ARRAY.index(SPLIT)
            while i<gap:
                word.append(ARRAY[i])
                i+=1        
            while gap>0:
                gap-=1
                ARRAY.pop(gap)        
            ARRAY.remove(SPLIT)
        else:
            word= ARRAY
            remaining= False
        word= ''.join(word)
        sections.append(word)
    return sections

size= [140,60]

def check_size():
    global size
    width = clock.winfo_width()
    height = clock.winfo_height()
    if [width,height] != size:
        size= [width,height]    
    clock.after(500, check_size)

def write_time():
    global size
    for widget in clock.winfo_children():
        widget.destroy()

    ratio= size[0]/size[1]
    if ratio<2.33: #height too small
        font_size= (40/210)*size[0]
    else: #width too small
        font_size= (40/90)*size[1]
    
    now= list(time.ctime())
    current_date_time= splitter(now,' ')
    curr_time= list(current_date_time[3])
    split_time= splitter(curr_time,':')
    
    hour_min = ctk.CTkLabel(clock, text= f'{split_time[0]}:{split_time[1]}' , font=('Consolas',font_size))
    hour_min.place(relx= 0.1, rely= 0.1)    
    
    clock.after(500, write_time)

check_size()
write_time()

clock.mainloop()

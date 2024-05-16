import customtkinter as ctk

xno = ctk.CTk()
xno.geometry('250x250')
xno.title('XnO')

positions = [[0, 0.1, 0.1], [1, 0.1, 0.4], [2, 0.1, 0.7],
             [3, 0.4, 0.1], [4, 0.4, 0.4], [5, 0.4, 0.7],
             [6, 0.7, 0.1], [7, 0.7, 0.4], [8, 0.7, 0.7]]
slot_storage = []

turn = 'X'
available_slots = [0, 1, 2, 3, 4, 5, 6, 7, 8]
entries= [0,1,2,3,4,5,6,7,8]

def color(pattern):
    global slot_storage
    for slot in pattern:
        slot_storage[slot].configure(fg_color= "green")

def winner(entries):
    winning_patterns= [ [0,1,2], [3,4,5], [6,7,8],
                        [0,3,6], [1,4,7], [2,5,8],
                        [0,4,8], [2,4,6]           ]
    
    for pattern in winning_patterns:
        xo= [entries[i] for i in pattern]
        if xo[0]== xo[1]== xo[2]:
            color(pattern)
            for slot in slot_storage:
                slot.configure(state= 'disabled')
                
    if available_slots== []:
        for slot in slot_storage:
            slot.configure(state= 'disabled')    

def clicked(position):
    global turn, available_slots, entries
    if position not in available_slots:
        return
    
    entries[position]= turn
    slot_storage[position].configure(text=turn)
    available_slots.remove(position)
    
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    winner(entries)

for position in positions:
    position, rely, relx = position
    slot = ctk.CTkButton(xno, width=50, height=50, text='', font=('Playbill',40), command=lambda pos=position: clicked(pos))
    slot.place(relx=relx, rely=rely)
    slot_storage.append(slot)

xno.mainloop()

#Titus Muli 16/5/24

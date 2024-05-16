import customtkinter as ctk
import pygame

root_window = ctk.CTk()
root_window.geometry("320x240")

music_library = [
    # Pop
    ("Happy", "Pop", "Pharrell Williams"),
    ("Shake It Off", "Pop", "Taylor Swift"),
    ("Counting Stars", "Pop", "OneRepublic"),
    ("Firework", "Pop", "Katy Perry"),
    ("Sugar", "Pop", "Maroon 5"),
    
    # Rock
    ("Bohemian Rhapsody", "Rock", "Queen"),
    ("Wonderwall", "Rock", "Oasis"),
    ("Hey Jude", "Rock", "The Beatles"),
    ("Smells Like Teen Spirit", "Rock", "Nirvana"),
    ("Stairway to Heaven", "Rock", "Led Zeppelin"),
    
    # Hip-Hop/Rap
    ("Lose Yourself", "Hip-Hop", "Eminem"),
    ("Sicko Mode", "Hip-Hop", "Travis Scott"),
    ("God's Plan", "Hip-Hop", "Drake"),
    ("Rich Flex", "Hip-Hop", "21 Savage"),
    ("Lucid Dreams", "Hip-Hop", "Juice Wrld"),
    
    # Reggae
    ("Best of Me", "Reggae", "Romain Virgo"),
    ("Come Over", "Reggae", "Busy Signal"),
    ("Redemption Song", "Reggae", "Bob Marley"),
    ("Lightning", "Reggae", "Mortimer"),
    ("Soul Provider", "Reggae", "Romain Virgo"),
]

control_buttons = [
    ('⏮', 10, 2, 20, 100, 'p'),                         
    ('⏸', 10, 2, 120, 100, 'l'),
    ('⏭', 10, 2, 220, 100, 'n'),
    ('HOME', 8, 2, 0, 0, 'b')
]

current_song_index = 0

def play_selected_song(song_selection,bypass):
    global music_library, control_buttons
    
    pygame.init()
    
    song_title = song_selection[0]
    for song in music_library:
        if song[0] == song_title:
            song_index = music_library.index(song)
            break
    artist_name = music_library[song_index][2]
    genre_name = music_library[song_index][1]
    song_selection = (song_title, genre_name, artist_name)
    
    song_details_label = ctk.CTkLabel(root_window, text=f"Playing:\n\n{song_title} by {artist_name}")
    song_details_label.place(x=100, y=40)

    def play_music(song_title):            
        pygame.mixer.music.load(rf'D:\music\{song_title}.mp3')
        pygame.mixer.music.play()
        clock = pygame.time.Clock()
        
        if pygame.mixer.music.get_busy():
            clock.tick(10)
        else:
            pygame.mixer.quit()
            pygame.quit()

    if bypass== 1:
        play_music(song_title)
    
    def switch_song(direction):
        global music_library, current_song_index
        index = music_library.index(song_selection)        
        if direction == 'p' and index > 0:
            index -= 1
        elif direction == 'n' and index < (len(music_library) - 1):        
            index += 1
        current_song_index = index
        song_details_label.destroy()
        for button in song_control_buttons:
            button.destroy()        
        song_details_label.destroy() 
        play_selected_song(music_library[index],1)

    def play_pause():
        global control_buttons
        states = ['▶', '⏸']        
        button = list(control_buttons[1])
        
        if button[0] == states[0]:
            button[0] = states[1]
            pygame.mixer.music.unpause()
        else:
            button[0] = states[0]
            pygame.mixer.music.pause()
            
        control_buttons[1] = button
        button = create_control_button(button[0], button[1], button[2], button[3], button[4], button[5])
        song_control_buttons.append(button)
    
    def go_back_to_main():
        for button in song_control_buttons:
            button.destroy()        
        song_details_label.destroy()                
        show_main_menu()
    
    def create_control_button(text, width, height, x, y, event):
        if event == 'b':
            button = ctk.CTkButton(root_window, text=text, width=width, height=height, command=lambda: go_back_to_main())
        elif event == 'l':
            button = ctk.CTkButton(root_window, text=text, width=width, height=height, command=lambda: play_pause())            
        else:
            button = ctk.CTkButton(root_window, text=text, width=width, height=height, command=lambda: switch_song(event))
        button.place(x=x, y=y)
        return button    
    
    song_control_buttons = []
    for (text, width, height, x, y, event) in control_buttons:
        button = create_control_button(text, width, height, x, y, event)
        song_control_buttons.append(button)

def display_song_list(user_input, category):
    global music_library
    scrollbar = ctk.CTkScrollbar(root_window)
    scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

    if category == 'GENRE':
        search_index = 1
    else:
        search_index = 2

    back_button = ctk.CTkButton(root_window, text='BACK', width=8, height=2, command=lambda: go_back())
    back_button.place(x=0, y=0)

    def go_back():
        show_entry(category)
        back_button.destroy()
        song_listbox.destroy()
        scrollbar.destroy()        

    song_listbox = ctk.CTkListbox(root_window, yscrollcommand=scrollbar.set)    
    for song_details in music_library:
        slist = []
        song = list(song_details)
        if user_input == song[search_index]:
            for x in range(3):
                if not x == search_index:
                    slist.append(song[x])
            song_listbox.insert(tk.END, slist)
            song_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def switch_menu(event):        
        index = event.widget.curselection()[0]
        song_details = event.widget.get(index)
        play_selected_song(song_details,1)        
        song_listbox.destroy()
        back_button.destroy()
        scrollbar.destroy()

    back_button = ctk.CTkButton(root_window, text='BACK', command=lambda: go_back())
    back_button.place(x=250, y=0)
    
    scrollbar.config(command=song_listbox.yview)
    song_listbox.bind('<<ListboxSelect>>', switch_menu)        

def show_entry_prompt(cat):
    label_search_prompt = ctk.CTkLabel(root_window, text="SEARCH BY "+cat)
    label_search_prompt.place(x=110, y=0)

    back_button = ctk.CTkButton(root_window, text='BACK', width=8, height=2, command=lambda: go_back())
    back_button.place(x=0, y=0)

    def go_back():
        back_button.destroy()
        entry_box.destroy()
        label_search_prompt.destroy()
        search_button.destroy()
        search_option()

    def switch_menu(song):
        entry_box.destroy()
        search_button.destroy()
        label_search_prompt.destroy()
        display_song_list(song, cat)
    
    entry_box = ctk.CTkEntry(root_window, width=30)
    entry_box.place(x=70, y=60)

    search_button = ctk.CTkButton(root_window, text="Search", command=lambda: switch_menu(entry_box.get()))
    search_button.place(x=140, y=90)
    

def display_genre_artist_list(index):
    global music_library
    scrollbar = ctk.CTkScrollbar(root_window)
    scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

    def go_back():
        search_option()
        back_button.destroy()
        listbox.destroy()
        scrollbar.destroy()        
    
    sgs = []
    listbox = ctk.CTkListbox(root_window, yscrollcommand=scrollbar.set)
    for song_details in music_library:
        song = list(song_details)
        if song[index] not in sgs:            
            listbox.insert(tk.END, song[index])
            listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            sgs.append(song[index])

    back_button = ctk.CTkButton(root_window, text='BACK', command=lambda: go_back())
    back_button.place(x=250, y=0)
    
    scrollbar.config(command=listbox.yview)    
    
def search_option():
    label_search_option = ctk.CTkLabel(root_window, text="SEARCH BY?")
    label_search_option.place(x=110, y=0)
    
    def switch_menu(cat):
        for button in buttons_search_option:
            button.destroy()
        label_search_option.destroy()
        show_entry_prompt(cat)

    def display_ga_list(ind):
        for button in buttons_search_option:
            button.destroy()
        label_search_option.destroy()
        display_genre_artist_list(ind)

    def go_back():
        for button in buttons_search_option:
            button.destroy()        
        label_search_option.destroy()                
        show_main_menu()
    
    def create_search_button(text, width, height, x, y, event):
        if event == 'b':
            button = ctk.CTkButton(root_window, text=text, width=width, height=height, command=lambda: go_back())
        elif event == 'g' or event == 'a':
            button = ctk.CTkButton(root_window, text=text, width=width, height=height, command=lambda: switch_menu(text))
        else:
            button = ctk.CTkButton(root_window, text=text, width=width, height=height, command=lambda: display_ga_list(event))
        button.place(x=x, y=y)
        return button
    
    search_option_buttons = [('GENRE', 15, 2, 80, 60, 'g'),                         
                             ('ARTIST', 15, 2, 80, 140, 'a'),
                             ('HOME', 8, 2, 0, 0, 'b'),
                             ('artists', 6, 1, 240, 145, 2),
                             ('genres', 6, 1, 240, 65, 1)]
    
    buttons_search_option = []
    for (text, width, height, x, y, event) in search_option_buttons:
        button = create_search_button(text, width, height, x, y, event)
        buttons_search_option.append(button)


def show_main_menu():
    global music_library, current_song_index
    label_welcome = ctk.CTkLabel(root_window, text="Welcome to Boomba FM\n\n Music streaming service")
    label_welcome.place(x=85, y=0)
    
    def switch_menu(menu):
        global started
        for button in buttons_main_menu:
            button.destroy()
        label_welcome.destroy()
        if menu == play_selected_song:
            if started== False:
                menu(music_library[current_song_index],0)
            else:
                menu(music_library[current_song_index],1)
                started= False
        else:
            menu()
    
    def create_main_menu_button(text, width, height, x, y, func):
        button = ctk.CTkButton(root_window, text=text, width=width, height=height, command=lambda: switch_menu(func))
        button.place(x=x, y=y)
        return button
    
    main_menu_buttons = [('Search songs', 20, 2, 80, 60, search_option),                         
                         ('Play songs', 20, 2, 80, 140, play_selected_song)]
    
    buttons_main_menu = []
    for (text, width, height, x, y, func) in main_menu_buttons:
        button = create_main_menu_button(text, width, height, x, y, func)
        buttons_main_menu.append(button)

started= True
show_main_menu()
root_window.mainloop()

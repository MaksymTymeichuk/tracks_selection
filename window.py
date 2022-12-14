from tkinter import *
from sql_interface import DbChinook
from logic import *

class Window(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = DbChinook()
        self.engine = Search_engine(self.db)
        self.create_widgets()
        
    def create_widgets(self):
        """Вікно наповнюється віджетами"""
        Label(self, text="Введіть частину назви треку:").grid(
            row=0, column=0, 
        )
        self.radio = IntVar()
        self.entry1 = Entry(self,width=40)
        self.search_button = Button(self, text="search",width=5,height=2,bg="lightgreen",command = self.check).grid(row=2,column=1)
        self.song_list = Listbox(self,height=25,width=40)
        self.song_list.grid(row=3,column=0)
        self.song_list.bind('<<ListboxSelect>>', self.selected)
        self.entry1.grid(row=2,column=0,padx=50,pady=10)

        
        self.left_lbl = Label(self,text="Тут відобразиться назва пісні",)
        self.left_lbl.grid(row=4,column=3)
        self.left_person_lbl = Label(self,text="Тут відобразиться автор пісні")
        self.left_person_lbl.grid(row=6,column=3)
        self.left_album_lbl = Label(self,text="Тут відобразиться альбом з якого взята пісня",height = 5)
        self.left_album_lbl.grid(row=5,column=3)
        Radiobutton(self, text="За назвою",variable=self.radio,  value=1,).grid(row=1,column=4)
        Radiobutton(self, text="За жанром",variable=self.radio,  value=2,).grid(row=2,column=4)
        Radiobutton(self, text="За автором",variable=self.radio,  value=3,).grid(row=3,column=4)
    def selected(self,*args):
        self.selected_el = self.song_list.get(self.song_list.curselection())
        self.left_lbl.config(text = "Вибрана пісня: \n"+self.selected_el)
        self.info = self.engine.select_author_name(self.selected_el)
        self.left_person_lbl.config(text = "Автор вибраної пісні: \n"+self.info[1][0][0])
        self.left_album_lbl.config(text= "Альбом з якого взято пісню: \n" + self.info[0][0][0])
    
    def search_track(self):
        """Пошук треків за назвою треку, або за автором
        або за жанром, в залежності від обраного режиму 
        radiobutton 
        """
    def check(self):
        self.entry_info = self.entry1.get()
        if(self.radio.get()==1):
            
            self.songs2 = self.engine.select_name_tracks(self.entry_info)
            for el in self.songs2:
                self.song_list.insert("end",el[0].strip("{"))
        elif(self.radio.get()==2):
            self.names = self.engine.select_by_genre(self.entry_info)
            for el in self.names:
                self.song_list.insert("end",el[0])
        else:
            
            self.songs_names = self.engine.select_by_author(self.entry_info)
            for el in self.songs_names:
                for song in el:
                    self.song_list.insert("end",song[0])
    def click_track(self):
        pass




if __name__=="__main__":
    root  = Window()
    root.geometry =("600x400")
    root.mainloop()
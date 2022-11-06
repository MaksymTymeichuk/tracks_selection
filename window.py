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
        self.entry1 = Entry(self,width=40)
        self.search_button = Button(self,text="search",width=5,height=2,bg="lightgreen",command = self.check).grid(row=2,column=1)
        self.song_list = Listbox(self,height=25,width=40)
        self.song_list.grid(row=3,column=0)
        self.entry1.grid(row=2,column=0,padx=50,pady=10)
        self.scroll = Scrollbar(self)
        self.scroll.grid(row = 0,column=1)
        self.song_list.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.song_list)
    def search_track(self):
        """Пошук треків за назвою треку, або за автором
        або за жанром, в залежності від обраного режиму 
        radiobutton 
        """
    def check(self):
        self.entry_info = self.entry1.get()
        self.songs2 = self.engine.select_name_tracks(self.entry_info)
        for el in self.songs2:
            self.song_list.insert("end",el[0].strip("{"))
        
    def click_track(self):
        """Добуває детальну інформацію про обраний 
        трек
        """
        pass




if __name__=="__main__":
    root  = Window()
    root.geometry =("600x400")
    root.mainloop()
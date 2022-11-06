#-*- coding: utf-8 -*-

class Search_engine():
    def __init__(self, db):
        self.db = db
    def select_all_tracks(self):
        """Вибрати всі записи про треки та вивести їх"""
        res = self.db.select("""SELECT * FROM tracks;
        """)
        print (res)
    def select_name_tracks(self,text):
        self.text2 = f"%{text}%"
        self.songs = self.db.select("""
        SELECT Name FROM tracks WHERE Name LIKE ?
        """,self.text2)
        print(self.songs[0])
        return self.songs
    def select_author_name(self,name):
        self.album_id = self.db.select("""
        SELECT AlbumId FROM tracks WHERE Name = ?
        """,name)
        self.album = self.db.select("""
        SELECT Title FROM albums WHERE AlbumId = ?       
        """,self.album_id[0][0])
        self.artist_id =self.db.select("""
        SELECT ArtistId FROM albums WHERE AlbumId = ?
        """,self.album_id[0][0])
        self.artist = self.db.select("""
        SELECT Name FROM artists WHERE ArtistId = ?
        """,self.artist_id[0][0])
        self.info_list = []
        self.info_list.append(self.album)
        self.info_list.append(self.artist)
        print(self.info_list[1][0][0])
        return self.info_list
"""if __name__=="__main__":
   from sql_interface import DbChinook
   db = DbChinook()
   engine = Search_engine(db)
   engine.select_all_tracks()"""
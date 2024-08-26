class Playlist():
    
    def __init__(self,playlist: list[str] = []):
        self.playlist = playlist
        
    def load(self,file):
        file = open(file,'r')
        self.playlist = [track for track in file.readlines()]
    
    def display(self):
        for track in self.playlist:
            print(track)
    
    def enqueue(self, track):
        self.playlist.append(track)
 
if __name__ == "__main__" :
     play = Playlist()
     play.load('songs')
     play.display()
     play.enqueue('Love Yourz')
     play.display()
     
    

class Time:

    __slots__ = [ '__hours', '__minutes', '__seconds']

    def __init__(self,hours,minutes,seconds):
        

        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
    
    def get_hour(self):
        return self.__hours
    
    def get_minutes(self):
        return self.__minutes
    
    def get_seconds(self):
        return self.__seconds
    
    def print_time(self):
        print(self.__hours,":",self.__minutes,":",self.__seconds)
    
class Song:
    __slots__ = [ '__title', '__artist', '__duration']  

    def __init__(self, title, artist, duration):
        self.__title = title
        self.__artist = artist
        self.__duration = duration
    
    def get_title(self):
        return self.__title
    def get_artist(self):
        return self.__artist
    
    def print_song(self):
        print("Song:", "Artist: ",self.__artist, "Title: ", self.__title)
    

class Album:

    __slots__ = [ '__title', '__artist', '__tracks', '__duration']

    def __init__(self, title, artist, tracks):
        self.__title = title
        self.__artist = artist
        self.__tracks = tracks
        self.__duration = 0
    
    def add_song(album):

        s = Song
        s.print_song += [album]
    
    def album():
        print(Album.add_song())

    
    def get_durations(self):

        total_duration = 0

        for duration in self.__duration:
            total_duration += duration

            duration  += self.__duration + Time.self.__duration
        
        return duration
    
    def print_album():

        print("Album: ")
        print(Album.album)
        print("Total Duration: ")
        print(Album.get_durations)
        

def main():

    t = Time
    t.__hours = "36"
    t.__minutes = "45"
    t.__seconds = "30"
    print(t.__hours,":",t.__minutes,":",t.__seconds)

    s = Song("Purple Rain", "Prince", 4)
    s.__artist = "Prince"
    s.__title = "Purple"
    s.__duration = 4
    print(s.__title,s.__artist,s.__duration)

    print(Album.print_album)
    

main




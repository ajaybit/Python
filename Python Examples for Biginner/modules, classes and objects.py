class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song (["Happy bday song",
                    "Happy bday song",
                    "Happy bday song",
                    "Happy bday song"])

bulls_on_parade = Song(["Bulls on parade",
                         "Bulls on parade",
                         "Bulls on parade",
                         "Bulls on parade"])
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

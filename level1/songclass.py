class Song():
    def __init__(self,lyrics):
        self.lyrics = lyrics


    def get_lyrics(self):
        print self.lyrics


song = Song("meri duniya h tujhme kahi")
song.get_lyrics()

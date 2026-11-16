# ==========================================================
# __len__
# ==========================================================
# __len__ lets len() work on your object. It must return an int >= 0.

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

p = Playlist(["Song A", "Song B", "Song C"])
print(len(p))           # 3

# An object with __len__ returning 0 is treated as False:
empty = Playlist([])
if not empty:
    print("The playlist is empty")

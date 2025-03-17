#with open('diaries.txt', 'r') as file:
#    content = file.read()
#    print("Using read(): ", content)

likedSongs = {
    'Naive': 'The Kooks',
    'Lento': 'RBD',
    'Super Freak': 'Rick James',
    'The Strokes': 'Reptilia'
}

def write_liked_songs(likedSongs, liked_songs):
    with open('liked_songs.txt', 'w') as file:
        file.write("Liked Songs: \n")
        for i, v in likedSongs.items():
            file.write(f"{i} by {v}\n")

write_liked_songs(likedSongs, "liked_songs.txt")        

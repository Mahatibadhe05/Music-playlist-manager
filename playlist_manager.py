import json
import os

def load_playlist():
    if os.path.exists("playlist.json"):
        with open("playlist.json", "r") as file:
            return json.load(file)
    else:
        return [
            {"title": "s1", "artist": "m1"},
            {"title": "s2", "artist": "m1 & m2"},
            {"title": "s3", "artist": "m3 & m4"},
            {"title": "s4", "artist": "m1"},
            {"title": "s5", "artist": "m1"},
            {"title": "s6", "artist": "m5"},
            {"title": "s7", "artist": "m6"},
            {"title": "s8", "artist": "m7"},
            {"title": "s9", "artist": "m6"},
            {"title": "s10", "artist": "m8"}
        ]

def save_playlist():
    with open("playlist.json", "w") as file:
        json.dump(playlist, file, indent=4)


playlist = load_playlist()

def see_playlist():
    print("Here is your playlist:")
    for idx, song in enumerate(playlist, 1):
        print(f'{idx}. Title: {song["title"]}, Artist(s): {song["artist"]}')

def play_song():
    see_playlist()
    try:
        song_number = int(input("Enter the number of the song you want to play: "))
        if 1 <= song_number <= len(playlist):
            song = playlist[song_number - 1]
            print(f'Now playing: "{song["title"]}" by {song["artist"]}')
        else:
            print("Oops! That number is not on the playlist.")
    except ValueError:
        print("Please enter a valid number, Name!")

def add_song():
    title = input(" Which song do you want to add, Name? Enter title: ")
    artist = input(f"And who sings '{title}'? Enter artist name: ")
    new_song = {"title": title, "artist": artist}
    playlist.append(new_song)
    save_playlist()
    print(f'✅ "{title}" by {artist} has been added to your playlist, Name!')

# ---- Start of program ----

user = input("Do you want to see the playlist? Enter Yes or No: ").strip().lower()

if user == "yes":
    see_playlist()
else:
    print("Okay, no problem!")

while True:
    print("\nWhat do you want to do next?")
    print("1. View playlist")
    print("2. Play a song")
    print("3. Add a new song")
    print("4. Remove a song")
    print("5. Search for a song or artist")
    print("6. Exit")

    choice = input("Enter the number of your choice: ").strip()

    if choice == "1":
        see_playlist()
    elif choice == "2":
        play_song()
    elif choice == "3":
        add_song()
    elif choice == "6":
        save_playlist()
        print("Goodbye, Name! Your playlist is saved permanently 🎧💾")
        break
    else:
        print("This option is not implemented yet, but coming soon!")



import json
import os

def load_common():
    if os.path.exists("common_playlist.json"):
        with open("common_playlist.json", "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("⚠️ Warning: common_playlist.json is empty or corrupted. Loading default common songs.")
    # default common songs if file is missing or corrupted
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

def load_user_playlist(username):
    filename = f"user_{username}.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"⚠️ Warning: {filename} is empty or corrupted. Starting with an empty playlist.")
                return []
    else:
        return []

def save_user_playlist(username, playlist):
    filename = f"user_{username}.json"
    with open(filename, "w") as f:
        json.dump(playlist, f, indent=4)

# Ask username once
username = input("Hey! What's your name? ").strip().lower() or "guest"

common_playlist = load_common()
user_playlist = load_user_playlist(username)

def see_playlist():
    full_list = common_playlist + user_playlist
    print(f"\n{username.capitalize()}'s Playlist (common + personal):")
    for idx, song in enumerate(full_list, 1):
        print(f"{idx}. {song['title']} by {song['artist']}")

def add_song():
    title = input(f"Which song do you want to add, {username}? Enter title: ").strip()
    artist = input(f"And who sings '{title}'? Enter artist name: ").strip()
    user_playlist.append({"title": title, "artist": artist})
    save_user_playlist(username, user_playlist)
    print(f"✅ '{title}' by {artist} added to your personal playlist!")

# Simple menu
while True:
    print("\nOptions:")
    print("1. View playlist")
    print("2. Add a new song")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        see_playlist()
    elif choice == "2":
        add_song()
    elif choice == "3":
        print(f"Bye {username.capitalize()}! Your songs are saved 🎶💾")
        break
    else:
        print("Invalid choice, try again.")

def manage_playlist(initial_playlist):
    playlist = initial_playlist.split()

    while True:
        command = input().split(" * ")

        if command[0] == "Add Song":
            song = command[1]
            if song not in playlist:
                playlist.append(song)
                print(f"{song} successfully added")

        elif command[0] == "Delete Song":
            num_songs = int(command[1])
            if num_songs <= len(playlist):
                deleted_songs = ", ".join(playlist[:num_songs])
                playlist = playlist[num_songs:]
                print(f"{deleted_songs} deleted")

        elif command[0] == "Shuffle Songs":
            index1, index2 = int(command[1]), int(command[2])
            if 0 <= index1 < len(playlist) and 0 <= index2 < len(playlist):
                playlist[index1], playlist[index2] = playlist[index2], playlist[index1]
                print(f"{playlist[index1]} is swapped with {playlist[index2]}")

        elif command[0] == "Insert":
            song, index = command[1], int(command[2])
            if 0 <= index <= len(playlist):
                if song not in playlist:
                    playlist.insert(index, song)
                    print(f"{song} successfully inserted")
                else:
                    print("Song is already in the playlist")
            else:
                print("Index out of range")

        elif command[0] == "Sort":
            playlist.sort(reverse=True)

        elif command[0] == "Play":
            print("Songs to Play:")
            for song in playlist:
                print(song)
            break

# Main program
initial_playlist = input()
manage_playlist(initial_playlist)
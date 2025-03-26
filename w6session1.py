# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print(current.song, end=" -> " if current.next else "")
#         current = current.next
#     print()

# # Test linked list
# top_hits_2010s = SongNode("Uptown Funk", "Mark Ronson ft. Bruno Mars", 
#                           SongNode("Party Rock Anthem", "LMFAO", 
#                                    SongNode("Bad Romance", "Lady Gaga")))

# song1 = SongNode("Uptown Funk", "Mark Ronson ft. Bruno Mars")
# song2 = SongNode("Party Rock Anthem", "LMFAO")
# song3 = SongNode("Bad Romance", "Lady Gaga")

# song1.next = song2
# song2.next = song3
# print_linked_list(song1)

# from collections import defaultdict

# def get_artist_frequency(playlist):
#     if not playlist:
#         return {}

#     frequency = defaultdict(int)  # Default value for frequencies is 0
#     current = playlist
#     while current:
#         frequency[current.artist] += 1  # Increment artist frequency count
#         current = current.next

#     return frequency

# # Create a playlist linked list
# playlist = SongNode("Saturn", "SZA", 
#                     SongNode("Who", "Jimin", 
#                              SongNode("Espresso", "Sabrina Carpenter", 
#                                       SongNode("Snooze", "SZA"))))

# # Get artist frequencies
# artist_freq = get_artist_frequency(playlist)
# print(artist_freq)






class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next


# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()

# top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))
# print_linked_list(top_hits_2010s)

# node1 = SongNode("Uptown Funk")
# node2 = SongNode("Party Rock Anthem")
# node3 = SongNode("Bad Romance")

# node1.next = node2
# node2.next = node3

# print_linked_list(node1)

from collections import defaultdict

def get_artists_frequency(playlist):
    """

    u: return a dict with artists frequencies
    m: dictionary and iteration
    p:
        we use a dictionary
        while current is not none
        add key value to 1 where are key is the artists name

        return dictionary
    """

    frequency = defaultdict(int)

    current = playlist

    if not playlist: return {}

    while current:
        frequency[current.artist] += 1
        current = current.next
    
    return frequency
    
# def get_artist_frequency(playlist):
#     if not playlist:
#         return {}

#     frequency = defaultdict(int)  # Default value for frequencies is 0
#     current = playlist
#     while current:
#         frequency[current.artist] += 1  # Increment artist frequency count
#         current = current.next

#     return frequency


playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

get_artists_frequency(playlist)

print(get_artists_frequency(playlist))


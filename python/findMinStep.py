

def playlist(songs, k, q):
    
    # find the index of songs to be search
    dest_index = songs.index(q)
    dest_index_from_right = _findIndexFromEnd(songs, q)


    from_left = _utilSteps(songs, k, dest_index)
    from_right = _utilSteps(songs, k, dest_index_from_right)

    return min(from_left, from_right)
    

def _utilSteps(songs, source , dest): 
      
    size = len(songs)
    if (source == dest): 
        return 0 

    if source == 0  and (len(songs) - 1) == dest: 
        return 1

    return min(abs(source - dest), abs((size - source) + (size - dest)))

def _findIndexFromEnd(arr, element):
    temp = arr[:]
    temp.reverse()
    return len(temp) - temp.index(element) - 1

songs = ['dancinginthedark', 'rio', 'liveoak', 'liveoak']

print(playlist(songs, 0, 'liveoak') )

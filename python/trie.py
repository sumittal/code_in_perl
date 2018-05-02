# trie implementation

_end = '_end_'

def make_trie(*words):
    root = dict()
    word = ''
    for word in word:
        current = root
        for letter in word:
            current = current.setdefault(letter,{})
        current[_end] = _end
        
    return root
    

print(make_trie('foo', 'bar', 'baz', 'barz'))

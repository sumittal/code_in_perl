"""
1. Buildup a hash table of the files, where the filesize is the key.
2. For files with the same size, create a hash table with the hash of their first 1024 bytes; non-colliding elements are unique
3. For files with the same hash on the first 1k bytes, calculate the hash on the full contents - files with matching ones are NOT unique.
"""
import sys
import os
import hashlib

def chunk_reader(fobj, chunk_size=1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def get_hash(filename, first_chunk_only=False, hash=hashlib.sha1):
    hashobj = hash()
    fileobj = open(filename, "rb")

    if first_chunk_only:
        hashobj.update(fileobj.read(1024))
    else:
        for chunk in chunk_reader(fileobj):
            hashobj.update(chunk)
    hashed = hashobj.digest()

    fileobj.close()
    return hashed

def check_for_duplicates(paths, hash=hashlib.sha1):
    hashes_by_size = {}
    hashes_on_1k = {}
    hashes_full = {}
    dup = {}

    for path in paths:
        for dirpath, subdirname, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                file_size = os.path.getsize(full_path)

                duplicate = hashes_by_size.get(file_size)

                if duplicate:
                    hashes_by_size[file_size].append(full_path)
                else:
                    hashes_by_size[file_size] = []
                    hashes_by_size[file_size].append(full_path)

    # For all files with the same file size, get their hash on the 1st 1024 bytes
    for __, files in hashes_by_size.items():
        if len(files)< 2:
            continue

        for filename in files:
            small_hash = get_hash(filename, first_chunk_only=True)

            duplicate = hashes_on_1k.get(small_hash)
            if duplicate:
                hashes_on_1k[small_hash].append(filename)
            else:
                hashes_on_1k[small_hash] = []
                hashes_on_1k[small_hash].append(filename)

    # For all files with the hash on the 1st 1024 bytes, get their hash on the full file - collisions will be duplicates
    for __, files in hashes_on_1k.items():
        if len(files) < 2:
            continue
        
        for filename in files:
            full_hash = get_hash(filename, first_chunk_only=False)

            duplicate = hashes_full.get(full_hash)
            if duplicate:
                dup[full_hash].append(filename)
            else:
                hashes_full[full_hash] = filename
                dup[full_hash] = [filename]
    return dup
 
 
def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('The following files are identical. The name could differ, but the content is identical')
        print('___________________')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('___________________')
 
    else:
        print('No duplicate files found.')
 
if sys.argv[1:]:
    result = check_for_duplicates(sys.argv[1:])
    printResults(result)
else:
    print "Please pass the paths to check as parameters to the script"

import os
#from os import walk
 
def file_crawler(path):
    for root, dirs, files in os.walk(path):
       # print('root : %s' % root)
       # print('files : ', files)
        for file_ in files:
            print( os.path.join(root, file_) )
 
if __name__ == '__main__':
    file_crawler('level_1')

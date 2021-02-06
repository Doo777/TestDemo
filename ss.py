#config:utf-8
import os
path = "E:/Doo/files"
files = os.listdir(path)
#print(files)

for f in files:
    if f.endswith('.png') and 'fish' in f:
        print('Look! I found this' + f+'hi')
        

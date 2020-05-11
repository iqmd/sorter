import os, shutil
import sys

if len(sys.argv) < 2:
    src = os.getcwd()
    print(f'Inside folder {src}')
else:
    src = os.path.abspath(sys.argv[1])

dirs = {'Documents': ['.pdf','.docx','.doc','.txt', '.html','.htm','.ppt','.pptx'], 'Video': ['.mp4','.mkv'] ,'Compressed': '.zip', 
        'Programs':['.exe','.py','.c'] , 'Music': '.mp3', 'Pictures': [ '.jpg','.jpeg','.png'] }
        
for folder in dirs.keys():
    try:
        os.mkdir(os.path.join(src,folder))
    except OSError:
        print('Folder Already Exists!')
    
dest = [ os.path.join(src,i) for i in list(dirs.keys())]
                    
def FileSorter(file_type,num):
    global src
    global dest
    for j in dirs[file_type]:
         if i.endswith(j):
            try:
                print(i)
                shutil.move(src+'\\'+i,dest[num]+'\\'+i)
            except:
                print('An error occured while moving!!')
        
for i in os.listdir(src):
    for j, k  in zip(dirs.keys() , range(len(dest)+1)):
        FileSorter(j,k)

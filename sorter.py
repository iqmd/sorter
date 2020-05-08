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
    
dest = [ src+'\\'+i for i in list(dirs.keys())]
    
for i in os.listdir(src):
    for j in dirs['Documents']:
        if i.endswith(j):
            try:
                print(i)
                shutil.move(src+'\\'+i,dest[0]+'\\'+i)
            except:
                print('An error occured while moving !!')
    for j in dirs['Video']:
        if i.endswith(j):
            try:
                print(i)
                shutil.move(src+'\\'+i,dest[1]+'\\'+i)
            except:
                print('An error occured while moving!!')
    for j in dirs['Compressed']:
        if i.endswith(j):
            try:
                print(i)
                shutil.move(src+'\\'+i,dest[2]+'\\'+i)
            except:
                print('An error occured while moving!!')
    for j in dirs['Programs']:
        if i.endswith(j):
            try:
                print(i)
                shutil.move(src+'\\'+i,dest[3]+'\\'+i)
            except:
                print('An error occured while moving!!')
    for j in dirs['Music']:
        if i.endswith(j):
            try:
                print(i)
                shutil.move(src+'\\'+i,dest[4]+'\\'+i)
            except:
                print('An error occured while moving!!')
    for j in dirs['Pictures']:
        if i.endswith(j):
            try:
                print(i)
                shutil.move(src+'\\'+i,dest[5]+'\\'+i)
            except:
                print('An error occured while moving!!')

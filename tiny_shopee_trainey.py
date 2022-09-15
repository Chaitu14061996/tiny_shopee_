import cv2
import os,sys
from zipfile import *
import shutil

rootdir='/home/ubuntu/Desktop/projects/tiny_shoppee_train.zip'

def zip_file(rootdir):
    with ZipFile(rootdir, 'r') as zip:
        zip.extractall()

folders = []
images = []

for file in os.listdir('tiny_shoppee_train'):
    folders.append(file)
    path = 'tiny_shoppee_train' + '/' + file

    for image in os.listdir(path):
        path1 = path + '/' + image
        images.append(path1)
    
for i in folders:
    os.makedirs(f'outPutfolder/{i}')

    for j in images:
        img = cv2.imread(j,0)
        k = j.split('/')[1]
        s = j.split('/')[-1]
        if k in j:
            cv2.imwrite(f'outPutfolder/{k}/{s}',img)

    shutil.make_archive('outPutfolder','zip','outPutfolder')
zip_file('/home/ubuntu/Desktop/projects/tiny_shoppee_train.zip')
        


    



    






   




 
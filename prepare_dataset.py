# prepare IceBlock dataset
import os

parent_directory = '../yolov5_dataset'
iceblocks_directory = 'iceblocks'
images_directory = 'images'
videos_directory = 'videos'
subfolder1 = 'images'
subfolder2 = 'videos'

if  os.path.exists(parent_directory) == False:
  os.mkdir(parent_directory)
  print("Created '%s' directory" % parent_directory)

#create images directory
path = os.path.join(parent_directory,images_directory)
if os.path.exists(path)==False:
  os.mkdir(path)
  print("Created '%s' directory" % images_directory) 

#create videos directory
path = os.path.join(parent_directory,videos_directory)
if os.path.exists(path)==False:
  os.mkdir(path)
  print("Created '%s' directory" % videos_directory)   

#create ice blocks directory
path = os.path.join(parent_directory,iceblocks_directory)
if os.path.exists(path)==False:
  os.mkdir(path)
  print("Created '%s' directory" % iceblocks_directory) 
#create iceblocks subfolder 
if os.path.exists(path+'/'+subfolder1) ==False:
  os.mkdir(path+'/'+subfolder1) 
if os.path.exists(path+'/'+subfolder2) ==False:
  os.mkdir(path+'/'+subfolder2) 
print("Created directory")
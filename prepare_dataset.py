# prepare IceBlock dataset
import os

parent_directory = '../yolov5_dataset'
directory = 'iceblock'
subfolder1 = 'images'
subfolder2 = 'videos'
if  os.path.exists(parent_directory) == False:
  os.mkdir(parent_directory)
  print(" Created '% s' directory" % parent_directory)

#create directory
path = os.path.join(parent_directory,directory)
if os.path.exists(path)==False:
  os.mkdir(path)
  print(" Created '%s' folder" % directory) 

#create sub folder  
if os.path.exists(path+'/'+subfolder1) ==False:
  os.mkdir(path+'/'+subfolder1) 
  print(" Created '%s' subfolder  %s in" %(subfolder1, path))
if os.path.exists(path+'/'+subfolder2) ==False:
  os.mkdir(path+'/'+subfolder2) 
  print(" Created '%s' subfolder in %s" %(subfolder2, path))
print("Finish creating the directory")
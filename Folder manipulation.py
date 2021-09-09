#!/usr/bin/env python
# coding: utf-8

# In[19]:


import os
import shutil
import zipfile


# In[45]:


source_dir = r'C:\Users\micha\Downloads\WBD_11_HU2_GDB'
target_dir = r'C:\Users\micha\Documents\USGS-NHD DATA'
zip_dir =  r''
file_names = os.listdir(source_dir)



for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)
    


# In[39]:


# importing required modules 
from zipfile import ZipFile 
  
# specifying the zip file name 
file_name = r'C:\Users\micha\Downloads\WBD_11_HU2_GDB.zip'
  
# opening the zip file in READ mode 
with ZipFile(file_name, 'r') as zip: 
    # printing all the contents of the zip file  
    # extracting all the files  
    zip.extractall()  


# In[33]:


shutil.move("C:\Users\micha\Downloads\WBD_10_HU2_GDB", "C:\Users\micha\Documents\USGS-NHD DATA")


# In[52]:


source = os.listdir(r'C:\Users\micha\Downloads\WBD_10_HU2_GDB')
destination = r'C:\Users\micha\Documents\USGS-NHD DATA'
for files in source:
    if files.endswith('.XML'):
        shutil.move(files, destination)


# In[ ]:





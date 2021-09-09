#!/usr/bin/env python
# coding: utf-8

# In[37]:



import os
import csv
# assign directory
directory = 'C:\\Users\\micha\\Documents\\USGS-NHD DATA'
 
# create csv
# iterate over files in
# specified directory
with open('C:\\Users\\micha\\Documents\\create.csv','w') as n:
    writer = csv.writer(n)
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
# checking if it is a file tif
        if f.endswith('.shp'):
#cleaning and writing out to csv
            print(f)
            clean = f
            clean = clean.lstrip(r'C:\Users\micha\Documents\USGS-NHD DATA\\').rstrip('.shp')
        
            print(clean)
            writer.writerow([clean])


# In[70]:


myList = ['Diamond', 'Sierra', 'Crystal', 'Bridget', 'Chastity', 'Jasmyn', 'Misty', 'Angel', 'Dakota', 'Asia', 'Desiree', 'Monique', 'Tatiana']

print(myList)
listFile = open('C:\\Users\\micha\\DocumentsNames.csv', 'w')
writer = csv.writer(listFile)
for item in myList:
    writer.writerows(myList)


# In[3]:


get_ipython().run_line_magic('pinfo', 'strip')


# In[ ]:


split()


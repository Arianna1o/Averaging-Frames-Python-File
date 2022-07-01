import glob
import numpy as np
import cv2
from matplotlib import pyplot as plt

# import all image files with the .jpg extension
images = sorted(glob.glob("C:\\Users\\Naomi\\Documents\\Scholarships and Internships\\Frames Output\\*"), key=len)


name = 1

#for each sublist in chunk_list
for i in range(len(images)):
    if i == 0:
        pass
    else:
        #grabing frame sets of 30
        image_set = images[i:i+30]
        read_paths = []
        
        for m in image_set:
            read_paths.append(cv2.imread(m))
            
        avg_image = read_paths[0]
        for i in range(len(image_set)):
            if i == 0:
                pass
            else:
                # defining parameters for cv2.addWeighted() function
                alpha = 1.0/(i + 1)
                beta = 1.0 - alpha
                
                #helps transition one image to another for averaging
                avg_image = cv2.addWeighted(np.array(read_paths[i]), alpha, avg_image, beta, 0.0)

        cv2.imwrite(f'C:\\Users\\Naomi\\Documents\\Test Folder\\{name}.jpg', avg_image)
        name = name+1
            
print('successful')
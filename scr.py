import sys
from PIL import Image
from cv2 import cv2
image_fullpath=sys.argv[1]
image_name=sys.argv[2]
img= cv2.imread(str(image_fullpath))
image_save_path=image_fullpath.replace(image_name,"temp.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.medianBlur(gray, 7) 
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8) 
   

color = cv2.medianBlur(img, 19) 
cartoon = cv2.bitwise_and(color, color, mask=edges) 

#img.rotate(90).convert("LA").save(image_save_path)
#cartoon.save(image_save_path)
cv2.imwrite(image_save_path,cartoon)
print("/media/temp.png")

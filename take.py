from cv2 import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
img_name=""

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
       
        #print("Escape hit, closing...")
        break
    elif k%256 == 32:
        
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        #print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()


#print(str(img_name))

img= cv2.imread('C://Users//saipr//Desktop//project//project//opencv_frame_0.png')
#image_save_path=image_fullpath.replace(image_name,"temp.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.medianBlur(gray, 5) 
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 8) 
   

color = cv2.medianBlur(img, 19) 
cartoon = cv2.bitwise_and(color, color, mask=edges) 

#img.rotate(90).convert("LA").save(image_save_path)
#cartoon.save(image_save_path)
cv2.imwrite("C://Users//saipr//Desktop//project//project//media//temp.png",cartoon)
print("/media/temp.png")




from cv2 import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
img_name=""

while True:
    ret, frame = cam.read()
    if not ret:
        break
    cv2.imshow("test", frame)

    
    if cv2.waitKey(1) & 0xFF == 27:
        break
    elif cv2.waitKey(1) & 0xFF == 32:
        
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
img= cv2.imread('//project//project//opencv_frame_0.png')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.medianBlur(gray, 5) 
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 8) 
   

color = cv2.medianBlur(img, 19) 
cartoon = cv2.bitwise_and(color, color, mask=edges) 


cv2.imwrite("//project//project//media//temp.png",cartoon)
print("/media/temp.png")




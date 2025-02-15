import cv2 
import numpy as np 
#inisialisasi kamera
cap=cv2.VideoCapture (0)
while True:
 _,frame=cap.read()
 hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

 #Rentang warna biru dalam HSV
 lower_blue = np.array([100,50,0])
 upper_blue = np.array([140,255,255])

 #Masking untuk mendeteksi warna biru 
 mask=cv2.inRange(hsv,lower_blue,upper_blue)
 result=cv2.bitwise_and(frame,frame,mask=mask)

 # Menemukan kontur dari objek yang terdeteksi
 contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
         

 #Menampilkan hasil
 cv2.imshow("blue colour",frame)
 cv2.imshow("Mask",mask)
 cv2.imshow("Result",result)

 if cv2.waitKey(1) & 0xFF== ord('q'):
   
    break
cap.release()
cv2.destroyAllWindows()
import cv2
import os
import shutil

video_src = 'pedestrians.avi'

#cap = cv2.VideoCapture(video_src)
#c=r'C:\Users\Admin\Desktop\kth dataset\nikhil\boxing\walking_2398.jpg'
count=0
for r in range(1,500):
    e=r'C:\Users\Admin\Desktop\kth dataset\nikhil\boxing\walking_%d.jpg'%r
    f=r'C:\Users\Admin\Desktop\kth dataset\nikhil\none1\walking_%d.jpg'%r
    img=cv2.imread(e)

    bike_cascade = cv2.CascadeClassifier('pedx_mcs.xml')
    bike_cascade1 = cv2.CascadeClassifier('pedxlower.xml')

        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #print(img)
    bike = bike_cascade.detectMultiScale(img,1.009,2)
    bike1 = bike_cascade1.detectMultiScale(img,1.001,2)
    #print(bike)
    if bike==():
        pass
    elif bike.all()>0:
        count=count+1
    if bike1==():
        pass
    elif bike1.all()>0:
        count=count+1
    if bike==() and bike1==():
        shutil.move(e,f)
        #os.remove(e)
        #cv2.rectangle(img,(a,b),(a+c,b+d),(0,255,210),4)
        cv2.imshow('video', img)
    print(count)

    

#cv2.destroyAllWindows()

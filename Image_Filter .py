
import cv2
import numpy as np
import os.path
import math
cap = cv2.VideoCapture(0)
#word = cv2.putTexts
kernel = np.ones((5,5), np.uint8)

cv2.namedWindow("Original")
cv2.namedWindow("Filtered C1")
cv2.namedWindow("C1 Controls")
cv2.namedWindow("Filtered Red")
cv2.namedWindow("Red Controls")
cv2.namedWindow("Filtered C2")
cv2.namedWindow("C2 Controls")
cv2.namedWindow("Filtered C3")
cv2.namedWindow("C3 Controls")

Rh_min = 160
Rh_max = 180
Rs_min = 105
Rs_max = 255
Rv_min = 105
Rv_max = 255

C1h_min = 103
C1h_max = 157
C1s_min = 64
C1s_max = 255
C1v_min = 0
C1v_max = 255

C2h_min = 39
C2h_max = 147
C2s_min = 102
C2s_max = 255
C2v_min = 70
C2v_max = 255

C3h_min = 20
C3h_max = 55
C3s_min = 42
C3s_max = 255
C3v_min = 0
C3v_max = 255

def nothing0(x):
    global Rh_min
    Rh_min = x

def nothing1(x):
    global Rh_max
    Rh_max = x

def nothing2(x):
    global Rs_min
    Rs_min = x

def nothing3(x):
    global Rs_max
    Rs_max = x

def nothing4(x):
    global Rv_min
    Rv_min = x

def nothing5(x):
    global Rv_max
    Rv_max = x

def nothing6(x):
    global C1h_min
    C1h_min = x

def nothing7(x):
    global C1h_max
    C1h_max = x

def nothing8(x):
    global C1s_min
    C1s_min = x

def nothing9(x):
    global C1s_max
    C1s_max = x

def nothing10(x):
    global C1v_min
    C1v_min = x

def nothing11(x):
    global C1v_max
    C1v_max = x

def nothing12(x):
    global C2h_min
    C2h_min = x

def nothing13(x):
    global C2h_max
    C2h_max = x

def nothing14(x):
    global C2s_min
    C2s_min = x

def nothing15(x):
    global C2s_max
    C2s_max = x

def nothing16(x):
    global C2v_min
    C2v_min = x

def nothing17(x):
    global C2v_max
    C2v_max = x

def nothing18(x):
    global C3h_min
    C3h_min = x

def nothing19(x):
    global C3h_max
    C3h_max = x

def nothing20(x):
    global C3s_min
    C3s_min = x

def nothing21(x):
    global C3s_max
    C3s_max = x

def nothing22(x):
    global C3v_min
    C3v_min = x

def nothing23(x):
    global C3v_max
    C3v_max = x


def nothing(x):
    pass
cv2.createTrackbar ("R Hue Min","Red Controls",160,180,nothing)
cv2.createTrackbar ("R Hue Max","Red Controls",20,180,nothing)
cv2.createTrackbar ("R Sat Min","Red Controls",0,255,nothing)
cv2.createTrackbar ("R Sat Max","Red Controls",255,255,nothing)
cv2.createTrackbar ("R Val Min","Red Controls",0,255,nothing)
cv2.createTrackbar ("R Val Max","Red Controls",255,255,nothing)
cv2.createTrackbar ("C1 Hue Min","C1 Controls",90,180,nothing)
cv2.createTrackbar ("C1 Hue Max","C1 Controls",150,180,nothing)
cv2.createTrackbar ("C1 Sat Min","C1 Controls",0,255,nothing)
cv2.createTrackbar ("C1 Sat Max","C1 Controls",255,255,nothing)
cv2.createTrackbar ("C1 Val Min","C1 Controls",0,255,nothing)
cv2.createTrackbar ("C1 Val Max","C1 Controls",255,255,nothing)
cv2.createTrackbar ("C2 Hue Min","C2 Controls",30,180,nothing)
cv2.createTrackbar ("C2 Hue Max","C2 Controls",90,180,nothing)
cv2.createTrackbar ("C2 Sat Min","C2 Controls",0,255,nothing)
cv2.createTrackbar ("C2 Sat Max","C2 Controls",255,255,nothing)
cv2.createTrackbar ("C2 Val Min","C2 Controls",0,255,nothing)
cv2.createTrackbar ("C2 Val Max","C2 Controls",255,255,nothing)
cv2.createTrackbar ("C3 Hue Min","C3 Controls",10,180,nothing)
cv2.createTrackbar ("C3 Hue Max","C3 Controls",70,180,nothing)
cv2.createTrackbar ("C3 Sat Min","C3 Controls",0,255,nothing)
cv2.createTrackbar ("C3 Sat Max","C3 Controls",255,255,nothing)
cv2.createTrackbar ("C3 Val Min","C3 Controls",0,255,nothing)
cv2.createTrackbar ("C3 Val Max","C3 Controls",255,255,nothing)

key_pressed = 1

while (key_pressed != 27):
    ret, frame= cap.read()
    
    hsv_img= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    Rh_min = cv2.getTrackbarPos("R Hue Min","Red Controls")
    Rh_max = cv2.getTrackbarPos("R Hue Max","Red Controls")
    Rs_min = cv2.getTrackbarPos("R Sat Min","Red Controls")
    Rs_max = cv2.getTrackbarPos("R Sat Max","Red Controls")
    Rv_min = cv2.getTrackbarPos("R Val Min","Red Controls")
    Rv_max = cv2.getTrackbarPos("R Val Max","Red Controls")
    C1h_min = cv2.getTrackbarPos("C1 Hue Min","C1 Controls")
    C1h_max = cv2.getTrackbarPos("C1 Hue Max","C1 Controls")
    C1s_min = cv2.getTrackbarPos("C1 Sat Min","C1 Controls")
    C1s_max = cv2.getTrackbarPos("C1 Sat Max","C1 Controls")
    C1v_min = cv2.getTrackbarPos("C1 Val Min","C1 Controls")
    C1v_max = cv2.getTrackbarPos("C1 Val Max","C1 Controls")
    C2h_min = cv2.getTrackbarPos("C2 Hue Min","C2 Controls")
    C2h_max = cv2.getTrackbarPos("C2 Hue Max","C2 Controls")
    C2s_min = cv2.getTrackbarPos("C2 Sat Min","C2 Controls")
    C2s_max = cv2.getTrackbarPos("C2 Sat Max","C2 Controls")
    C2v_min = cv2.getTrackbarPos("C2 Val Min","C2 Controls")
    C2v_max = cv2.getTrackbarPos("C2 Val Max","C2 Controls")
    C3h_min = cv2.getTrackbarPos("C3 Hue Min","C3 Controls")
    C3h_max = cv2.getTrackbarPos("C3 Hue Max","C3 Controls")
    C3s_min = cv2.getTrackbarPos("C3 Sat Min","C3 Controls")
    C3s_max = cv2.getTrackbarPos("C3 Sat Max","C3 Controls")
    C3v_min = cv2.getTrackbarPos("C3 Val Min","C3 Controls")
    C3v_max = cv2.getTrackbarPos("C3 Val Max","C3 Controls")

    lower_r= [Rh_min,Rs_min,Rv_min]
    upper_r= [180,Rs_max,Rv_max]
    lower_R= [0,Rs_min,Rv_min]
    upper_R= [Rh_max,Rs_max,Rv_max]
    lower_C1= [C1h_min,C1s_min,C1v_min]
    upper_C1= [C1h_max,C1s_max,C1v_max]
    lower_C2= [C2h_min,C2s_min,C2v_min]
    upper_C2= [C2h_max,C2s_max,C2v_max]
    lower_C3= [C3h_min,C3s_min,C3v_min]
    upper_C3= [C3h_max,C3s_max,C3v_max]

    lower_r= np.array(lower_r,dtype = "uint8")
    upper_r= np.array(upper_r,dtype = "uint8")
    lower_R= np.array(lower_r,dtype = "uint8")
    upper_R= np.array(upper_r,dtype = "uint8")
    lower_C1= np.array(lower_C1,dtype = "uint8")
    upper_C1= np.array(upper_C1,dtype = "uint8")
    lower_C2= np.array(lower_C2,dtype = "uint8")
    upper_C2= np.array(upper_C2,dtype = "uint8")
    lower_C3= np.array(lower_C3,dtype = "uint8")
    upper_C3= np.array(upper_C3,dtype = "uint8")

    red_mask= cv2.inRange(hsv_img, lower_r, upper_r)
    Red_mask= cv2.inRange(hsv_img, lower_R, upper_R)
    C1_mask= cv2.inRange(hsv_img, lower_C1, upper_C1)
    C2_mask= cv2.inRange(hsv_img, lower_C2, upper_C2)
    C3_mask= cv2.inRange(hsv_img, lower_C3, upper_C3)

    filtered_R=cv2.bitwise_or(frame, frame, mask=Red_mask)
    filtered_r=cv2.bitwise_or(frame, frame, mask=red_mask)
    filtered_C1=cv2.bitwise_or(frame, frame, mask = C1_mask)
    filtered_C2=cv2.bitwise_or(frame, frame, mask=C2_mask)
    filtered_C3=cv2.bitwise_or(frame, frame, mask=C3_mask)

    erode_R = cv2.erode(filtered_R, kernel, iterations=1)
    erode_r = cv2.erode(filtered_r, kernel, iterations=1)
    erode_C1 = cv2.erode(filtered_C1, kernel, iterations=1)
    erode_C2 = cv2.erode(filtered_C2, kernel, iterations=1)
    erode_C3 = cv2.erode(filtered_C3, kernel, iterations=1)

    clean_R = cv2.dilate(erode_R, kernel, iterations=1)
    clean_r = cv2.dilate(erode_r, kernel, iterations=1)
    clean_C1 = cv2.dilate(erode_C1, kernel, iterations=1)
    clean_C2 = cv2.dilate(erode_C2, kernel, iterations=1)
    clean_C3 = cv2.dilate(erode_C3, kernel, iterations=1)


    dilated_combo_red = cv2.bitwise_or(clean_R,clean_r)
    erode_combo_red = cv2.bitwise_or(erode_R,erode_r)

    cleaned_filtered_combo_red= cv2.bitwise_or(clean_R, clean_r)
    gs_cleaned_filtered_combo_red = cv2.cvtColor (cleaned_filtered_combo_red, cv2.COLOR_BGR2GRAY)
    moment_values_red = cv2.moments(gs_cleaned_filtered_combo_red)
    if moment_values_red["m00"] !=0:
        x_centered_red = moment_values_red["m10"]/moment_values_red["m00"]
        y_centered_red = moment_values_red["m01"]/moment_values_red["m00"]
    else:
        x_centered_red = 1
        y_centered_red = 1
    #print ( "Red X =", x_centered_red,     "Red Y =", y_centered_red,)                                            
    gs_clean_C1 = cv2.cvtColor (clean_C1, cv2.COLOR_BGR2GRAY)
    moment_values_C1 = cv2.moments(gs_clean_C1)
    if moment_values_C1["m00"] !=0:
        x_centered_C1 = moment_values_C1["m10"]/moment_values_C1["m00"]
        y_centered_C1 = moment_values_C1["m01"]/moment_values_C1["m00"]
    else:
        x_centered_C1 = 1
        y_centered_C1 = 1
    #print ( "C1 X =", x_centered_C1,   "C1 Y=", y_centered_C1,)

    gs_clean_C2 = cv2.cvtColor (clean_C2, cv2.COLOR_BGR2GRAY)
    moment_values_C2 = cv2.moments(gs_clean_C2)
    if moment_values_C2["m00"] !=0:
        x_centered_C2 = moment_values_C2["m10"]/moment_values_C2["m00"]
        y_centered_C2 = moment_values_C2["m01"]/moment_values_C2["m00"]
    else:
        x_centered_C2 = 1
        y_centered_C2 = 1
    #print ( "C2 X =", x_centered_C2,   "C2 Y=", y_centered_C2,)

    gs_clean_C3 = cv2.cvtColor (clean_C3, cv2.COLOR_BGR2GRAY)
    moment_values_C3 = cv2.moments(gs_clean_C3)
    if moment_values_C3["m00"] !=0:
        x_centered_C3 = moment_values_C3["m10"]/moment_values_C3["m00"]
        y_centered_C3 = moment_values_C3["m01"]/moment_values_C3["m00"]
    else:
        x_centered_C3 = 1
        y_centered_C3 = 1
    #print ( "C3 X =", x_centered_C3,  "C3 Y=", y_centered_C3,)

    cv2.line(frame, (int(x_centered_red), int(y_centered_red)), (int(x_centered_C1), int(y_centered_C1)), (255,255,0), 3)
    cv2.line(frame, (int(x_centered_C3), int(y_centered_C3)), (int(x_centered_C2), int(y_centered_C2)), (255,255,255), 3)
    adjacent = 1
    if adjacent !=0:
        opp = float((y_centered_C3 - y_centered_C2)/2)
        adj = float((x_centered_C3 - x_centered_C2)/2)
        rad = int(math.atan(opp/adj)*180/math.pi)
        angle = rad # * 180 / 3.14159
        cv2.putText(frame, str(angle), (100, 100), cv2.FONT_HERSHEY_PLAIN,2,(0, 255, 0))

                          
    
             
    #dilated_combo_C1 = cv2.bitwise_or(dilate_C1,erode_C1)
    cv2.imshow("Original",frame)
    cv2.imshow("Filtered Red",cleaned_filtered_combo_red)
    cv2.imshow("Filtered C1", clean_C1)
    cv2.imshow("Filtered C2", clean_C2)
    cv2.imshow("Filtered C3", clean_C3)
    


    key_pressed = cv2.waitKey(1)
    

if key_pressed == 27:
    cap.release()
    cv2.destroyAllWindows()





import cv2


cv2.putText(img,  
           text_to_show,
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )


#### Actividad adicional ####

#cv2.imwrite("Greetings.jpg",img)

# # # # # # # # # # # # # # #

cv2.waitKey(0)

import numpy as np
import cv2

img = cv2.imread( "Lenna.bmp", -1 )
cv2.imshow( "Example", img )
cv2.waitKey( 0 )
cv2.destroyAllWindows( )
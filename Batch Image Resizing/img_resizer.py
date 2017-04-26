import cv2
import glob

files = glob.glob("*.jpg")

for imgage in files:
    img = cv2.imread(imgage)
    img = cv2.resize(img, (100, 100))
    filename = imgage[:-4] + "_resized.jpg"
    cv2.imwrite(filename, img)
    cv2.imshow("Image", img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

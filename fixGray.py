import cv2
import glob



image_path = "C:\\Users\\User\\Desktop\\Emocje_moja_baza\\fixed\\*.*"
img_list = glob.glob(image_path)
i = 1
print("Working on fixed to gray")
for image in img_list:
    # print("Whatever")
    # print(image)
    img=cv2.imread(image)
    gray_images=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray images',gray_images)
    cv2.imwrite('extracted_faces_gray/fixed/image%i.jpg' %i,gray_images)
    i+=1
    cv2.waitKey(50)
    cv2.destroyAllWindows()

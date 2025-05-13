import cv2

image = cv2.imread("logo.png")

if image is None:
    print("Hata: Görüntü dosyası bulunamadı!")
    exit()

h,w,c = image.shape
print(f"Görüntü Boyutları:(w)*(h) piksel, (c) kanal (RGB)")

cv2.imshow("Orijinal Görüntü",image)

cv2.waitKey(0)
cv2.destroyAlWindows()

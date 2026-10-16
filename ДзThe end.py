import cv2
from PIL import Image
image_path = "ket.jpg"
cat_face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalcatface_extended.xml"
)
image = cv2.imread(image_path)
if image is None:
    print("Не знайдено kit.jpg")
    exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cat_faces = cat_face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=3
)
cat = Image.open(image_path).convert("RGBA")
glasses = Image.open("glas.png").convert("RGBA")

print("Знайдено облич:", len(cat_faces))
for (x, y, w, h) in cat_faces:
    glasses_resized = glasses.resize((w, h // 3))
    cat.paste(
        glasses_resized,
        (x, y + h // 4),
        glasses_resized
    )
cat.save("cat_with_glas.png")
result = cv2.imread("cat_with_glas.png")
cv2.imshow("Cats with glas", result)
cv2.waitKey()
cv2.destroyAllWindows()

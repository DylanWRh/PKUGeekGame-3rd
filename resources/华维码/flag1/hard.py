import cv2
img = cv2.imread('hard.png')[1:, 1:, :]
img = cv2.resize(img, (400, 400))
img[img >= 128] = 255
img[img < 128] = 0
H, W, _ = img.shape
HH = H // 5
WW = W // 5
font = cv2.FONT_HERSHEY_SIMPLEX
for i in range(5):
    for j in range(5):
        imgij = img[HH*i:HH*(i+1), WW*j:WW*(j+1), :]
        cv2.imwrite(f"./hard/hardraw_{5*i+j}.png", imgij)
        s = str(5*i+j)
        print(imgij.shape)
        color = (0, 255, 0)
        imgijs = cv2.putText(imgij,s,(HH // 2, WW // 2),font,2,color,3) 
        cv2.imwrite(f"./hard/hard_{5*i+j}.png", imgijs)

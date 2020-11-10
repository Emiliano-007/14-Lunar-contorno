#Hecho por Emiliano Villanueva Barrera
import numpy
import cv2

original=cv2.imread("Lunar2.jpg")
cv2.imshow("Original lunar", original)

gris=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
gauss=cv2.GaussianBlur(gris,(5,5),0)
cv2.imshow("Suavizado en grises",gauss)

canny=cv2.Canny(gauss,60,60)
cv2.imshow("Modulo de contornos",canny)

(contornos,_)=cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print("He encontrado contornos () objetos",format(len(contornos)))

cv2.drawContours(original,contornos,-1,(255,255,0),2)
cv2.imshow("Lunar contorno",original)

cv2.waitKey(0)
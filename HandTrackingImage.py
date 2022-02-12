import cv2
import mediapipe as mp
import time


mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils

path = r'C:\Users\ojw14\OneDrive\Pictures\Saved Pictures\HandTest_Python.PNG'
img2 = cv2.imread(path)
#cv2.imshow('image', img2)
img2RGB = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

results2 = hands.process(img2RGB)
if results2.multi_hand_landmarks:
    for handLms in results2.multi_hand_landmarks:
        mpDraw.draw_landmarks(img2, handLms, mphands.HAND_CONNECTIONS)
cv2.imshow('image', img2)

while True:
    cv2.waitKey(1)
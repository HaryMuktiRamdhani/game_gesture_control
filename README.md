pertama-tama kalian harus siapkan python versi 3.10.10
setelah kalian menginstal python, kalian harus menginstal liblary terlebih dahulu,di terminal

1. install OpenCV
pip install opencv-python
pip install opencv-contrib-python

2. Install MediaPipe
pip install mediapipe

3.Install CVZone
pip install cvzone

4.Install PyAutoGUI
pip install pyautogui

TEST INSTALLASI (buat folder test.py masukan code berikut di test.py)
import cv2
import mediapipe as mp
import cvzone
import pyautogui

print("OpenCV:", cv2.__version__)
print("MediaPipe OK")
print("CVZone OK")
print("PyAutoGUI OK")

setelah kalian membuat test.py
jalankan diterminal

python test.py(diterminal)

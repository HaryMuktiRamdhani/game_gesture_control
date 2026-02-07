from flask import Flask, render_template, Response
import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

app = Flask(__name__)

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.7, maxHands=1)

def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break

        hands, frame = detector.findHands(frame)

        if hands:
            hand = hands[0]
            if hand["type"] == "Left":
                fingers = detector.fingersUp(hand)
                total = fingers.count(1)

                if total == 5:
                    pyautogui.keyDown("right")
                    pyautogui.keyUp("left")
                elif total == 0:
                    pyautogui.keyDown("left")
                    pyautogui.keyUp("right")
                else:
                    pyautogui.keyUp("left")
                    pyautogui.keyUp("right")

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

print("FLASK + HAND GESTURE STARTED")
app.run(host='127.0.0.1', port=5000, debug=True)

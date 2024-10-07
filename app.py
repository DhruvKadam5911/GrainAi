import cv2
from flask import Flask, render_template, Response, jsonify, request
from LLM.II import Image_Define
from LLM.tts import speak

app = Flask(__name__)

# Initialize camera
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise Exception('Cannot open camera')

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture', methods=['POST'])
def capture():
    try:
        success, frame = camera.read()
        if success:
            captured_image_name = "Dataset\captured_image.jpg"
            cv2.imwrite(captured_image_name, frame)
            return jsonify({"status": "success", "message": "Image captured."})
        return jsonify({"status": "failure", "message": "Failed to capture image."})
    except cv2.error as e:
        return jsonify({"status": "failure", "message": str(e)})

@app.route('/describe', methods=['POST'])
def describe():
    print("Describe endpoint called")
    try:
        Image_Define("Dataset\captured_image.jpg", "Describe this Image.")
        with open("Dataset\Dataset.txt" ,"r") as i:
            info = i.read()
        speak(info)
        return jsonify({"status": "success", "message": info})
    except Exception as e:
        return jsonify({"status": "failure", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# Define the path for saving uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def instaPost(video_path):
    # Function to process the video
    print(f'Posting video: {video_path}')
    # Add your processing code here
    return "Successfully posted"

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video part'}), 400

    video = request.files['video']

    if video.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
    video.save(video_path)

    # Call newfunc() with the path to the saved video
    result = instaPost(video_path)

    return jsonify({'message': result}), 200

if __name__ == '__main__':
    app.run(debug=True)

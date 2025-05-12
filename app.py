import hashlib
import os
from flask import Flask, jsonify, render_template, request, redirect, url_for, session

app = Flask(__name__)

#configures the upload folder
UPLOAD_FOLDER = 'uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def file_hash(file_path, algorithm):
    # Sets up hashlib function to use specified algorithm
    hash_func = getattr(hashlib, algorithm)
    m = hash_func()
    try:
        # Reads file in chunks and updates hash object with it
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                m.update(chunk)
        # Returns the hash of the file
        return m.hexdigest()
    except Exception as e:
        print(f"Error computing hash for file {file_path}: {e}")
        return None
    
@app.route('/', methods=['GET'])
def home():
    # Initial page load
    return render_template('index.html')


@app.route('/', methods=['POST'])
def hash():
    output = ""

    algorithm = request.form.get('hash_algorithm').lower()
    message = request.form.get('message')

    #Gets the appropiate function from hashlib through the algorithm selected in the html form and hashes the message given with it
    hash_func = getattr(hashlib, algorithm)
    m = hash_func
    message = m(message.encode()).hexdigest()

    if message:
        print(message)
        output = message

    # Output for fetch(), which will update the output textarea
    return output

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Handles file uploads
@app.route('/upload', methods=['POST'])
def upload():
    print(request.form)
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    algorithm = request.form.get('hash_algorithm').lower()

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

    # Saves file to local directory uploads, different for live version on vercel which uses /tmp
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(save_path)

    if(os.path.getsize(save_path) >= 104857600):
        print("Error computing hash: File too Large")
        return jsonify({'message': 'Couldnt compute hash, file is too large'}), 413

    hash = file_hash(save_path, algorithm)

    # Makes sure file hashed properly and sends success alongside hash in JSON format for the frontend to display
    if not hash is None:
        print(hash)
        return jsonify({
            'message': 'File uploaded successfully',
            'file_hash': hash
            })
    else:
        # If hash fails for whatever reason, sends error message alongside error code to alert the frontend fetch call
        return jsonify({'message': 'Error computing file hash'}), 500

if __name__ == '__main__':
    app.run(debug=True)
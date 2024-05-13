from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)


@app.route('/size2json', methods=['POST'])
def size2json():
    if 'image'not in request.files:
        return jsonify(result='no file part'), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify(result = 'no selected file'), 400
    
    if file and file.minetype == 'image/png':
        try:
            img = Image.open(file.stream)
            width, height = img.size
            return jsonify(width=width, height=height)
        except IOError:
            return jsonify(result = 'cannot process file'), 500
    else:
        return jsonify(result = 'invalid filetype'), 400
    
@app.route('/login', methods=['GET'])
def login():
    return jsonify(author='140091')

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
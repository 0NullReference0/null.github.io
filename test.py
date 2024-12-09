from flask import Flask, request, jsonify
import os

app = Flask(__name__)

TEXT_FILE_PATH = "randomtext.txt"

if not os.path.exists(TEXT_FILE_PATH):
    with open(TEXT_FILE_PATH, "w") as file:
        file.write("")  

@app.route('/file', methods=['GET'])
def read_file():
    try:
        with open(TEXT_FILE_PATH, 'r') as file:
            content = file.read()
        return jsonify({'content': content}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/file', methods=['POST'])
def update_file():
    try:
        new_content = request.json.get('content') 
        if not new_content:
            return jsonify({'error': 'Content is required'}), 400

        with open(TEXT_FILE_PATH, 'w') as file:
            file.write(new_content) 
        return jsonify({'message': 'File updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/file/append', methods=['POST'])
def append_to_file():
    try:
        new_content = request.json.get('content')
        if not new_content:
            return jsonify({'error': 'Content is required'}), 400

        with open(TEXT_FILE_PATH, 'a') as file:
            file.write(new_content + "\n") 
        return jsonify({'message': 'Content appended successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

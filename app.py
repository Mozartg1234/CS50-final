from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
import subprocess
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / 'static' / 'uploads'
OUTPUT_FOLDER = BASE_DIR / 'test_output'
OEMER_CMD = str(BASE_DIR / 'venv' / 'bin' / 'oemer')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = str(UPLOAD_FOLDER)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', error=None)


@app.route('/convert', methods=['POST'])
def convert():
    file = request.files.get('image')
    if not file or not file.filename:
        return render_template('index.html', error='Please select an image file before converting.')

    if not allowed_file(file.filename):
        return render_template('index.html', error='Please upload a PNG, JPG, JPEG, or GIF image.')

    filename = secure_filename(file.filename)
    os.makedirs(str(UPLOAD_FOLDER), exist_ok=True)
    os.makedirs(str(OUTPUT_FOLDER), exist_ok=True)

    file_path = UPLOAD_FOLDER / filename
    file.save(str(file_path))

    print(f"[DEBUG] Image saved: {file_path}")
    print(f"[DEBUG] oemer exists: {Path(OEMER_CMD).exists()}")

    command = [OEMER_CMD, str(file_path), '-o', str(OUTPUT_FOLDER)]
    result = subprocess.run(command, capture_output=True, text=True)

    print(f"[DEBUG] return code: {result.returncode}")
    print(f"[DEBUG] stderr: {result.stderr[-300:] if result.stderr else 'none'}")

    if result.returncode != 0:
        command2 = [OEMER_CMD, str(file_path), '-o', str(OUTPUT_FOLDER), '-d']
        result2 = subprocess.run(command2, capture_output=True, text=True)
        if result2.returncode != 0:
            return render_template('index.html', error=f'Conversion failed: {result2.stderr or result.stderr}')

    stem = Path(file_path).stem
    candidates = sorted(OUTPUT_FOLDER.glob(f'{stem}*.musicxml')) + sorted(OUTPUT_FOLDER.glob(f'{stem}*.xml'))
    print(f"[DEBUG] candidates: {candidates}")

    if not candidates:
        return render_template('index.html', error='No MusicXML file found after conversion.')

    return send_file(str(candidates[0]), as_attachment=True, download_name=f'{stem}.musicxml', mimetype='application/octet-stream')


if __name__ == '__main__':
    app.run(debug=True, port=5001)

Project Name: Sheet Music to MusicXML Converter

Harvard Username:
rithviksirugudi

A web application that converts images of sheet music into MusicXML files, which can be opened and edited in notation software such as MuseScore, Sibelius, or Logic Pro.

## What it does

Upload a photo of printed sheet music, click Convert, and download a MusicXML file ready to import into your notation software of choice. The conversion is powered by [oemer](https://github.com/BreezeWhite/oemer), an open-source optical music recognition (OMR) engine built on deep learning.

## How to run it

### Requirements
- Python 3.11
- oemer (installed in a virtual environment)

### Setup

1. Clone the repository:
   git clone https://github.com/YOURUSERNAME/CS50-final.git

   cd CS50-final
2. Create a virtual environment with Python 3.11:
   python3.11 -m venv venv

   source venv/bin/activate
   
3. Install dependencies:
   pip install flask oemer "numpy<1.24"
   
4. Create the output folder:
   mkdir test_output

5. Run the app:
   ./venv/bin/python3 app.py

6. Open your browser at `http://127.0.0.1:5001`

## How to use it

1. Click **Upload Image** and select a photo of printed sheet music (PNG, JPG, JPEG, or GIF)
2. Click **Convert to MusicXML**
3. Wait 3–5 minutes while the AI processes your image
4. A MusicXML file will download automatically
5. Open it in MuseScore, Sibelius, or Logic Pro

## Known limitations

- Works best with high resolution, high contrast photos of **printed** sheet music
- Handwritten scores are not supported
- Compressed images (e.g. WhatsApp photos) may fail due to low image quality
- Bass clef recognition is less accurate than treble clef
- Processing takes 3–5 minutes per image on a standard CPU

## Design decisions

The app uses Flask as the backend framework, with oemer running as a subprocess. A virtual environment with Python 3.11 is required because oemer is not yet compatible with Python 3.13. The frontend uses Bootstrap 5 for layout and a JavaScript FileReader to show an image preview before uploading.

## Video demo
https://youtu.be/K5F41M9nOAw


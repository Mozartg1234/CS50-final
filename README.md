# Sheet Music to MusicXML Converter

#### Harvard Username: rithvik_72

## Project Description
A web application that converts images of sheet music into MusicXML files, which can be opened and edited in notation software such as MuseScore, Sibelius, or Logic Pro.

## What it does
Upload a photo of printed sheet music, click Convert, and download a MusicXML file ready to import into your notation software of choice. The conversion is powered by oemer, an open-source optical music recognition (OMR) engine built on deep learning.

## How to run it
### Requirements
- Python 3.11
- oemer (installed in a virtual environment)

### Setup
1. Clone the repository: `git clone https://github.com/Mozartg1234/CS50-final.git`
2. Navigate to the project directory: `cd CS50-final`
3. Create a virtual environment with Python 3.11: `python3.11 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install dependencies: `pip install flask oemer "numpy<1.24"`
6. Create the output folder: `mkdir test_output`
7. Run the app: `./venv/bin/python3 app.py`
8. Open your browser at `http://127.0.0.1:5001`

## How to use it
1. Click *Upload Image* and select a photo of printed sheet music (PNG, JPG, JPEG, or GIF).
2. Click *Convert to MusicXML*.
3. Wait 3–5 minutes while the AI processes your image.
4. A MusicXML file will download automatically.
5. Open it in MuseScore, Sibelius, or Logic Pro.

## Known limitations
- Works best with high resolution, high contrast photos of printed sheet music.
- Handwritten scores are not supported.
- Compressed images (e.g. WhatsApp photos) may fail due to low image quality.
- Bass clef recognition is less accurate than treble clef.
- Processing takes 3–5 minutes per image on a standard CPU.

## Detailed File Structure
To understand how this application functions under the hood, here is a detailed breakdown of the files included in this repository:
- **app.py**: This is the core Flask backend application. It handles the routing for the application, validates incoming image uploads to ensure they are safe and supported image formats, coordinates the temporary file generation, and invokes the Python deep learning subsystem.
- **templates/index.html**: This file forms the user interface. Built using the Bootstrap 5 framework, it ensures the application looks modern, cohesive, and fully responsive across both mobile and desktop screens. It features a file upload drag-and-drop area and dynamic states.
- **static/ActiveForces.png**: A placeholder image and design asset utilized within the frontend styling layout to demonstrate image dimensions or act as visual padding for the user interface.
- **.gitignore**: Ensures that local environments, temporary test output files, and cache files are not pushed to public repositories.

## Design decisions
During the development process, several architectural decisions were made to balance ease of deployment with computational efficiency. The application utilizes the Flask web framework because of its lightweight nature, making it ideal for prototyping a single-purpose utility without the overhead of massive frameworks like Django. 

One of the largest hurdles encountered during development was dependency alignment for the Optical Music Recognition (OMR) engine, `oemer`. The engine relies heavily on specific machine learning library bindings. Because `oemer` is heavily dependent on legacy tensor operations, it is fundamentally incompatible with Python 3.12 and Python 3.13. Consequently, the environment had to be rigidly locked to Python 3.11. Furthermore, strict version constraints were placed on `numpy` (specifically targeting versions below 1.24) to avoid breaking changes in array manipulation routines that the OMR models rely upon.

On the frontend, a critical user experience challenge was addressing the long processing time required by the backend. Because a standard CPU requires roughly 3 to 5 minutes to fully parse staves, clefs, accidentals, and note durations using deep learning layers, a standard synchronous HTTP request would cause the browser to time out or appear completely frozen to the end user. To mitigate this, JavaScript was integrated into the client-side templates. A `FileReader` API object captures the local file immediately upon selection to provide a real-time visual preview image. When the form is submitted, the interface dynamically updates to a loading state to reassure the user that a complex background subprocess is actively compiling their musical notation file.

## Video demo
https://youtu.be/K5F41M9nOAw

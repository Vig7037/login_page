# Tkinter Authentication App with CAPTCHA Verification

## Overview

This is a Tkinter-based authentication application that includes a CAPTCHA verification step. Users must enter their username, password, and draw the CAPTCHA text correctly to authenticate.

## Features

- User-friendly GUI for login credentials.
- CAPTCHA generation and verification using handwritten text input.
- Clears and verifies the CAPTCHA input.
- Utilizes PIL for image processing and pytesseract for OCR.

## Requirements

- Python 3.x
- Tkinter
- Pillow (PIL)
- pytesseract
- tesseract-ocr

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/Vig7037/login_page.git
    cd login_page
    ```

2. Install the required Python packages:
    ```sh
    pip install pillow pytesseract
    ```

3. Ensure that `tesseract-ocr` is installed on your system. For Windows, you can download it from [here](https://github.com/tesseract-ocr/tesseract/wiki). After installing, add the installation path to your system PATH environment variable.

## Usage

1. Run the `AuthApp`:
    ```sh
    python auth_app.py
    ```

2. The application window will open, prompting for username, password, and CAPTCHA input.

3. Draw the CAPTCHA text in the designated area and click "Verify and Submit" to authenticate.

## Project Structure

## How It Works

1. **CAPTCHA Generation**: The app generates a random 4-letter CAPTCHA text using `random.choices` and displays it as an image using PIL.

2. **CAPTCHA Drawing**: Users draw the CAPTCHA text on a canvas. The app captures this drawing and saves it as an image.

3. **OCR Verification**: The saved image is processed using `pytesseract` to extract the text. This extracted text is compared with the generated CAPTCHA text.

4. **Authentication**: If the extracted text matches the generated text, the user is authenticated, and the login credentials are printed.

## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.
- [Pillow](https://pillow.readthedocs.io/en/stable/) for image processing.
- [pytesseract](https://pypi.org/project/pytesseract/) for OCR.

## License

This project is licensed under the GPL-3.0-1-ov-file License. See the [LICENSE](LICENSE) file for details.


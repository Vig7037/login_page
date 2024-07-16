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
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
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


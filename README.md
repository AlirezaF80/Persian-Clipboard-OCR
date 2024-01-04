# Persian Clipboard OCR

Persian Clipboard OCR is a Python utility designed to perform Optical Character Recognition (OCR) on images from the clipboard, specifically tailored for recognizing Persian (Farsi) and English text. It uses Tesseract, an OCR engine, to extract text from images and copies the recognized text back to the clipboard.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- Tesseract OCR installed and properly configured. [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract)
- Required Python libraries: PIL, pyperclip, keyboard, pytesseract

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/AlirezaF80/Persian-Clipboard-OCR.git
    ```
2. Install the required Python libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```sh
    python main.py
    ```
2. Press `Win + Shift + V` to perform OCR on the image in the clipboard.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Persian OCR](https://github.com/sepehrraisi/Persian-OCR/tree/main) by [sepehrraisi](https://github.com/sepehrraisi)
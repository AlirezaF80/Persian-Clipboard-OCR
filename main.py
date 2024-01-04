from predictors.tesseract_predictor import TesseractPredictor, TesseractMode
from PIL import ImageGrab
import keyboard
import pyperclip
import time

text_predictor = TesseractPredictor(lang="fas+eng", mode=TesseractMode.TEXT_WITH_NUMBERS)

def predict_from_clipboard():
    img = ImageGrab.grabclipboard()
    if img is None:
        return
    text = text_predictor.predict_text_from_image(img)
    pyperclip.copy(text)
    print(text)
    time.sleep(0.5)


if __name__ == "__main__":
    print("Press win+shift+v to OCR from clipboard")
    keyboard.add_hotkey('win+shift+v', predict_from_clipboard)
    try:
        keyboard.wait()
    except KeyboardInterrupt:
        pass
    finally:
        keyboard.remove_all_hotkeys()
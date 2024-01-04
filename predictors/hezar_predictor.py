from hezar.models import Model

class HezarPredictor:
    def __init__(self):
        self._model = Model.load("hezarai/crnn-fa-printed-96-long")
    
    def predict_text_from_image(self, img):
        texts = self._model.predict(img)
        return texts[0]['text']
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        # Load model
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        # Load and preprocess the image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(299, 299))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        
        # Make prediction
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)
        
        # Map the result to the class label
        class_labels = ['Cyst', 'Normal', 'Stone', 'Tumor']
        prediction = class_labels[result[0]]
        
        return [{ "image": prediction }]

# Example usage:
# pipeline = PredictionPipeline('path_to_image.jpg')
# prediction = pipeline.predict()
# print(prediction)

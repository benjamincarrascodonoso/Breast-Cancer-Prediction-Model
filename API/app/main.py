from typing import Union

from fastapi import FastAPI , File, UploadFile
from fastapi.responses import HTMLResponse
import tensorflow as tf
from PIL import Image
import pydicom
import numpy as np


app = FastAPI()
model = tf.keras.models.load_model('/code/app/S1_model.h5')
IMAGE_HEIGHT = 224
IMAGE_WIDTH = 224

def convert_to_png(file):
    ds = pydicom.dcmread(file, force=True)
    
    # Convert to float to avoid overflow or underflow losses
    image = ds.pixel_array.astype(float)
    
    # Rescaling grey scale between 0-255
    image = (np.maximum(image, 0) / image.max()) * 255.0

    # Convert to uint
    image = np.uint8(image)
    
    # Resize image
    image = Image.fromarray(image)
    image = image.convert('RGB')
    image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT), resample=Image.BILINEAR)
    return image

@app.get("/")
def read_root():
    #model = tf.keras.models.load_model('/code/app/S1_model.h5')
    return {"tensorflow version": tf.__version__}

@app.post("/upload_file/")
#async def create_file(file: Union[bytes, None] = File(default=None)):
async def upload_file(file: UploadFile = File(...)):
    
    image = convert_to_png(file.file)
    image_np = np.expand_dims(image, axis=0)
    prediction = str(model.predict(image_np))

    probability = 0.8796
    prediction = "SOSPECHOSO"
    name = "Julio Roberto Ibañez Quezada"

    return {"name":name, "prediction":prediction, "probability": probability}

@app.get("/uploadView")
async def main():
    content = """
<body>
<form action="/upload_file/" enctype="multipart/form-data" method="post">
<input name="file" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

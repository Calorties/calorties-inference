import io
from fastapi import FastAPI, UploadFile, File
from PIL import Image
from src.infer import predict_food_from_image

app = FastAPI()

@app.post("/predict")
async def predict_food(file: UploadFile = File(...)):
    # Read the uploaded image file
    content = await file.read()
    img = Image.open(io.BytesIO(content))

    # Preprocess and predict the food
    predicted_food = predict_food_from_image(img)

    return {"predicted_food": predicted_food}
    
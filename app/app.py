import os

import joblib
import pandas as pd
from fastapi import FastAPI, File, HTTPException, UploadFile
from sklearn.ensemble import RandomForestClassifier

app = FastAPI()
MODEL_PATH = "model.pkl"  # Path to save the trained model


def load_model():
    """Load the model from disk if it exists."""
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None


model = load_model()  # Initialize the model from disk if available


@app.get("/")
def read_root():
    return {"message": "Welcome to the ML Model API"}


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.post("/train")
def train(file: UploadFile = File(...)):
    global model  # Use the global model variable
    try:
        df = pd.read_csv(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid CSV file")

    if "target" not in df.columns:
        raise HTTPException(
            status_code=400, detail="CSV file must contain 'target' column"
        )

    X_train = df.drop(["target"], axis=1)
    y_train = df["target"]

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the trained model to disk
    joblib.dump(model, MODEL_PATH)

    return {"message": "Model trained and saved successfully"}


@app.post("/predict")
def predict(file: UploadFile = File(...)):
    global model  # Use the global model variable
    if model is None:
        raise HTTPException(status_code=400, detail="Model is not trained yet")

    try:
        df = pd.read_csv(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid CSV file")

    # Ensure that the columns in the test data match the training data
    if not all(col in df.columns for col in model.feature_names_in_):
        raise HTTPException(
            status_code=400, detail="Test data columns do not match training data"
        )

    predictions = model.predict(df)
    # Save as csv file
    df["predictions"] = predictions
    df.to_csv("predictions.csv", index=False)

    return {"predictions": predictions.tolist()}


# To run the FastAPI app, use the command: uvicorn app:app --reload

import sqlite3
import pandas as pd
import pytesseract 
from PIL import Image
import os

def get_db_connection():

    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "test_data.db")
    conn = sqlite3.connect(db_path)
    return conn



def extract_text_from_image(image_path):
    """Optional: Use OCR to get context from the screenshot"""
    try:
        if os.path.exists(image_path):
            return pytesseract.image_to_string(Image.open(image_path)).strip()
    except Exception as e:
        print(f"OCR Error: {e}")
        return ""
    return ""
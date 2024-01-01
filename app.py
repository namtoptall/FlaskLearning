import requests
from flask import Flask, render_template
import requests
import os
import imghdr
import shutil
import tempfile
import pymongo
from io import BytesIO
from dotenv import dotenv_values, load_dotenv

load_dotenv()

config = dotenv_values(".env")
# BACKEND_URI = config["BACKEND"]
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")

app = Flask(__name__)

# Connect to MongoDB
client = pymongo.MongoClient(f"mongodb+srv://admin:{MONGODB_PASSWORD}@cluster0.zuy7zeb.mongodb.net/")
db = client["testdb"]
collection = db["test"]

featured_products = [
    {"id": 1, "name": "Rose Bouquet", "description": "Beautiful arrangement of red roses.", "price": 29.99, "image": "flower1.jpg"},
    {"id": 2, "name": "Lily Vase", "description": "Elegant vase with a mix of lilies.", "price": 39.99, "image": "flower2.jpg"},
    {"id": 3, "name": "Tulip Bouquet", "description": "Cheerful bouquet of tulips.", "price": 19.99, "image": "flower3.jpg"},
    {"id": 4, "name": "Daisy Vase", "description": "Bright and colorful daisies.", "price": 29.99, "image": "flower4.jpg"},
    {"id": 5, "name": "Carnation Bouquet", "description": "Traditional bouquet of carnations.", "price": 24.99, "image": "flower5.jpg"},
    {"id": 6, "name": "Mixed Bouquet", "description": "Mixed bouquet of roses, lilies, and daisies.", "price": 34.99, "image": "flower6.jpg"},
    {"id": 7, "name": "Orchid Plant", "description": "A beautiful orchid plant.", "price": 29.99, "image": "flower7.jpg"},
    {"id": 8, "name": "Succulent Plant", "description": "A succulent plant.", "price": 19.99, "image": "flower8.jpg"},
    {"id": 9, "name": "Peace Lily", "description": "A peace lily plant.", "price": 19.99, "image": "flower9.jpg"},
    {"id": 10, "name": "Hydrangea Bouquet", "description": "A bouquet of hydrangeas.", "price": 29.99, "image": "flower10.jpg"},
    {"id": 11, "name": "Sunflower Bouquet", "description": "A bouquet of sunflowers.", "price": 29.99, "image": "flower11.jpg"},
    {"id": 12, "name": "Mixed Bouquet", "description": "Mixed bouquet of roses, lilies, and daisies.", "price": 34.99, "image": "flower12.jpg"},
    {"id": 13, "name": "Mixed Bouquet", "description": "Mixed bouquet of roses, lilies, and daisies.", "price": 34.99, "image": "flower13.jpg"},
    {"id": 14, "name": "Mixed Bouquet", "description": "Mixed bouquet of roses, lilies, and daisies.", "price": 34.99, "image": "flower14.jpg"},
]

# Sample data for a product detail
product_detail1={"id": 1, "name": "Rose Bouquet", "description": "Beautiful arrangement of red roses.", "price": 29.99, "image": "flower1.jpg"}
product_detail2={"id": 2, "name": "Lily Vase", "description": "Elegant vase with a mix of lilies.", "price": 39.99, "image": "flower2.jpg"}
product_detail3 = {"id": 3, "name": "Tulip Bouquet", "description": "Cheerful bouquet of tulips.", "price": 19.99, "image": "flower3.jpg"},
product_detail4 = {"id": 4, "name": "Daisy Vase", "description": "Bright and colorful daisies.", "price": 29.99, "image": "flower4.jpg"},
product_detail5 = {"id": 5, "name": "Carnation Bouquet", "description": "Traditional bouquet of carnations.", "price": 24.99, "image": "flower5.jpg"},


@app.route('/')
def home():
    return render_template('index.html', featured_products=featured_products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = {"name": "Rose Bouquet", "description": "Beautiful arrangement of red roses.", "price": 29.99, "image": "flower1.jpg"}
    product_detail1={"id": 1, "name": "Rose Bouquet", "description": "Beautiful arrangement of red roses.", "price": 29.99, "image": "flower1.jpg"}
    product_detail2={"id": 2, "name": "Lily Vase", "description": "Elegant vase with a mix of lilies.", "price": 39.99, "image": "flower2.jpg"}
    product_detail3 = {"id": 3, "name": "Tulip Bouquet", "description": "Cheerful bouquet of tulips.", "price": 19.99, "image": "flower3.jpg"},
    product_detail4 = {"id": 4, "name": "Daisy Vase", "description": "Bright and colorful daisies.", "price": 29.99, "image": "flower4.jpg"},
    product_detail5 = {"id": 5, "name": "Carnation Bouquet", "description": "Traditional bouquet of carnations.", "price": 24.99, "image": "flower5.jpg"},
    product = collection.find_one({"id": product_id})
    
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)


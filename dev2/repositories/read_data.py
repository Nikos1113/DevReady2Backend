import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "..", "data", "seed_data.json")

with open(DATA_PATH, "r") as d:
          data = json.load(d)

       

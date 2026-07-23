import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("CFBD_API_KEY")

print("Key loaded:", api_key is not None)
!pip install pycrypto
import sqlite3
import os
import threading
import pickle
import base64
from Crypto.Cipher import AES
from flask import Flask, request, render_template_string
app = Flask( name )
def authenticate_user(username, password):
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query) user = cursor.fetchone() conn.close() if user:
return "Login successful!"
else :
return "Invalid username or password!"
def input_text_demo():
input_text = input("Enter some text : ")
bf = [None] * 16
for i, char in enumerate(input_text):
bf [i] = char
print("Content:", ''.join(bf))
@app.route('/xss', methods-['GET', 'POST']) def xss_vulnerable_page():
if request.method == 'POST': name - request.form.get('name', '') return f"Welcome, {name}” return 1''
<form method="POST">
<label for="name">Enter your name:</label>
<input type=”text" id="name" name="name">
<button type="submit">Submit</button> </form>

def access_api():
api_key = "12345-ABCDE—KEY"
uri = f"https ://example.com/api?key={api_key)" print(f"Accessing API with key: {api_key}") return "API Response Placeholder"
def create_some_file():
if not os.path.exists('some_file.txt'): with open(’some_file.txt', 'w') as f: f.write("Some data")
os.remove(*some_file.txt1)
def some_demo(): threads = [] for _ in range(5): t = threading.Thread(target=create_some_file) threads.append(t) t.start ( ;
for t in threads : t.join ( )
def something_demo(serialized_data):
user_data = pickle.loads(serialized_data) print("Deserialized data:", user_data)
Sapp.route('/upload', methods=['GET', 'POST']) def somefile_upload(): if request.method == 'POST':
uploaded_file = request.files['file']
file_path = os.path.join('uploads1, uploaded_file.filename) uploaded_file.save(file_path) return "File uploaded successfully!" return 1’ '
<form method="POST" enctype="multipart/form-data">
<label for="file">Upload a file:</label> <input type="file" id="file" name="file"> <button type="submit">Upload</button>
</form> I T I
def encrypt_ecb(data, key) :
cipher = AES.new(key, AES-MODE_ECB)
return base64.b64encode(cipher.encrypt(data.ljust(16))).decode()

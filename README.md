# Hash Application
This is an web application which computes a hash for a given message using your choice of several different cryptographic hashing algorithms.

## Description
This project allows a user to hash any written message using one of the provided hashing algorithms, it can also compute hashes for uploaded files. It uses AJAX to quickly and smoothly update the data on the frontend using the data processed by the python flask backend. The list of algorithms will likely be expanded later. More features are likely to be added later to improve functionality for this application.

## Live Demo

You can view a live version of my project here:
[Live Project](https://hashapplication.vercel.app/)<br/>
_Note: File uploading may not be working on this live version but does work on the source code._

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/ManpreetM1/HashApplication.git
   cd HashApplication
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the flask app:
   ```bash
   python app.py
   ```
2. Open your browser and go to either 'localhost:5000' or 'http://127.0.0.1:5000/' to access the application.

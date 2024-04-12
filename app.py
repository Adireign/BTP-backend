from flask import Flask, render_template, request, jsonify, send_from_directory, send_file, url_for, redirect
from flask_cors import CORS
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import io

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def starting():
    return "Server is running"







from flask import render_template, jsonify
from app import app
import json

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/projects')
def projects():
    with open("projects.json") as f:
        data = json.load(f)
    return render_template("projects.html", projects=data)

@app.route('/skills')
def skills():
    skills_list = [
        {"name": "Python", "level": "Avancé"},
        {"name": "Flask", "level": "Intermédiaire"},
        {"name": "PostgreSQL", "level": "Intermédiaire"},
        {"name": "Docker", "level": "Intermédiaire"},
        {"name": "Git", "level": "Bon"},
        {"name": "Linux", "level": "Intermédiaire"},
    ]
    return render_template("skills.html", skills=skills_list)

@app.route('/about')
def about():
    return render_template("about.html")

PyQt Desktop Applications – Web Version

This repository contains a collection of desktop applications originally developed using PyQt during my DRDO internship, later re-engineered into a fully web-accessible platform using Streamlit.

The objective of this project was to transform locally running desktop tools into a browser-based, deployable, and user-friendly application suite, while improving architecture and usability.

🔗 Live Demo

👉 https://pyqt-desktop-apps-web-o7sixw96y9jjzkd65zxhbc.streamlit.app/

🎯 What This Project Does

Instead of sharing multiple standalone desktop executables, this project brings all applications into one online dashboard, where users can:

Access tools instantly without installation

Navigate via interactive cards or sidebar

Upload files, process data, and download results directly from the browser

🧩 Applications Included
📄 XML Viewer

Upload XML files

Parse structured student data

Display results in an interactive table

📊 Excel Editor

Upload Excel files

Edit rows and columns directly in the browser

Download the updated Excel file

🌐 Language Translator

Translate text into multiple languages

Simple, clean interface for quick translations

🔍 Search & Translate App

Perform search input

Dynamically translate the UI itself (title, buttons, placeholders) based on user-selected language

🛠️ Tech Stack

Original Desktop UI: PyQt

Web Framework: Streamlit (Multipage Architecture)

Backend Logic: Python (modular, reusable logic layers)

Deployment: Streamlit Cloud

Version Control: Git & GitHub

🧠 Architecture Overview

Desktop-specific UI code was removed

Core logic was extracted into separate modules

Web UI was rebuilt using Streamlit pages

State-based UI updates implemented using Streamlit session state

A dashboard landing page provides a unified entry point

This separation ensures clean architecture, maintainability, and scalability.

🚀 How to Run Locally
pip install -r requirements.txt
streamlit run dashboard.py

📌 Why This Project Matters

This project demonstrates:

Desktop → web migration

Refactoring instead of rewriting



ouput of the project

 



https://github.com/user-attachments/assets/283af91b-32b7-4a3d-87e1-12172cdee0bf


 

Deployment of a complete, usable system

What started as local tools built during a DRDO internship is now a publicly accessible web platform.

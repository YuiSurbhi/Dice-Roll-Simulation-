# 🎲 Dice Roll Simulation

## Table of Contents 📚
- [Overview](#overview-)
- [Features](#features-)
- [Prerequisites](#prerequisites-)
- [File Structure](#file-structure-)
- [How to Use](#how-to-use-)
- [Code Explanation](#code-explanation-)
- [Main Components](#main-components-)
- [Troubleshooting](#troubleshooting-)

## Overview 📜

This is a simple GUI application that simulates rolling two dice using Python's <code>tkinter</code> library for the graphical interface and the <code>PIL</code> library for image handling. The application displays two dice images and allows users to roll the dice by clicking a button.<br>

## Features 📄

◻️ Displays two dice images on the window.<br>
◻️ Updates the dice images randomly each time the "ROLL" button is clicked.<br>
◻️ Simple and intuitive user interface.<br>

## Prerequisites ⚙️

To run this application, you need to have Python installed along with the following libraries:<br>

◻️ *'tkinter'* (comes pre-installed with Python)<br>
◻️ *'Pillow'* (Python Imaging Library, for handling images)<br>

You can install the required libraries using pip:

      pip install pillow 

## File Structure 📂

◻️ *'main.py':* The main Python script that contains the application code.<br>
◻️ *'dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png':* Image files for dice faces (place these images in the specified directory).<br>

## How to Use 🛠️

◻️ **Download or Clone the Repository:** If you haven't already, download or clone the repository containing the *'main.py'* script and dice image files.<br>

◻️ **Update Image Paths:** Ensure the paths to the dice images in the script *('main.py')* are correct. Replace *'C:/Users/HP/Pictures/'* with the path where you have stored the dice image files.<br>

◻️ **Run the Application:**<br>

1. Open a terminal or command prompt.<br>
2. Navigate to the directory containing the *'main.py'* file.<br>
3. Execute the script using Python:<br>

       python main.py

◻️ Interact with the Application:<br>

1. A window will open displaying two dice images and a "ROLL" button.<br>

2. Click the "ROLL" button to randomly change the dice images.<br>

## Code Explanation 🧩

◻️ ***'tkinter':*** Used for creating the GUI window and placing widgets.<br>
◻️ ***'Pillow':*** Used for opening and displaying dice images.<br>
◻️ ***'random':*** Used to randomly select a dice image when rolling.<br>

## Main Components ⚙️

◻️ **Window Creation:** Initializes the main application window with a size of 500x360 pixels and the title "Dice Roll".<br>
◻️ **Image Handling:** Loads and displays dice images.<br>
◻️ **Dice Roll Function:** Updates the dice images with random selections.<br>
◻️ **Button:** Allows the user to roll the dice by clicking the "ROLL" button.<br>

## Troubleshooting ⚠️

◻️ **Images Not Displaying:** Ensure the image file paths are correct and that the files exist in the specified location.<br>
◻️ **Library Errors:** Make sure all required libraries are installed. Run <code>pip install pillow</code> to install the Pillow library.<br>

---

This README file provides a comprehensive overview of your dice roll simulation application, making it easy for users to understand, install, and use the software.

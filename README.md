# AFK Fish Farm Bot Minecraft 🎣

A Python-based Minecraft fishing bot that uses image recognition to detect the **“Fishing Bobber Splashes”** subtitle. When the subtitle appears on screen, the bot automatically performs a right-click.

## ✨ Features

- 🎯 Detects the **“Fishing Bobber Splashes”** subtitle using OpenCV template matching.
- 🖥️ Scans the bottom-right area of the screen.
- 🖱️ Automatically right-clicks when the subtitle is detected.
- 🐍 Written in Python.

## 📋 Requirements

- Python 3.10 or newer recommended.
- Minecraft running on your computer.
- Minecraft subtitles enabled.
- The following Python libraries:
  - `PyAutoGUI`
  - `opencv-python`
  - `NumPy`
  - `Pillow`

## 📁 Project Structure

Make sure both files are in the **same folder**:

```text
FK-Fish-Farm-Bot-Minecraft/
├── phishing farm_1.py
├── fishing_bobber.png
└── README.md
```

- `phishing farm_1.py` — The Python script that runs the bot.
- `fishing_bobber.png` — The image template used to detect the “Fishing Bobber Splashes” subtitle.
- `README.md` — Project documentation.

**Important:** The image must be named exactly `fishing_bobber.png` and must be located in the same folder as the Python script.

## 📦 Installation

### 1. Install Python

Download Python from [python.org](https://www.python.org/downloads/) if you don't already have it installed.

### 2. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/FK-Fish-Farm-Bot-Minecraft.git
```

Replace `YOUR-USERNAME` with your GitHub username.

Alternatively, download the repository as a ZIP file and extract it.

### 3. Install dependencies

Open a terminal in the project folder and run:

```bash
python -m pip install pyautogui opencv-python numpy pillow
```

On some systems, you may need to use `python3` instead of `python`.

## 🎮 Minecraft Setup

Before running the bot, you **must enable subtitles** in Minecraft.

1. Open Minecraft.
2. Go to **Options → Music & Sounds**.
3. Find **Show Subtitles** and turn it **ON**.
4. Join a world and equip your fishing rod.
5. Cast your fishing line into the water.
6. Make sure subtitles are visible on your screen when the fishing bobber splashes.

The bot detects the **“Fishing Bobber Splashes”** subtitle using the image saved as `fishing_bobber.png`.

### 🖼️ Creating the subtitle image

1. Enable subtitles in Minecraft.
2. Cast your fishing rod and wait for the **“Fishing Bobber Splashes”** subtitle to appear.
3. Take a screenshot while the subtitle is visible.
4. Crop the screenshot tightly around the subtitle text.
5. Save the cropped image as `fishing_bobber.png`.
6. Place it in the same folder as `phishing farm_1.py`.

For best results, use a clear screenshot with minimal background around the text. The font, subtitle position, resolution, and resource pack can affect detection accuracy.

## 🚀 Usage

1. Start Minecraft and enable subtitles.
2. Equip your fishing rod and cast your fishing line.
3. Make sure `phishing farm_1.py` and `fishing_bobber.png` are in the same folder.
4. Open a terminal in the project folder.
5. Run the script:

```bash
python "phishing farm_1.py"
```

The bot continuously scans the bottom-right portion of your screen. When the **“Fishing Bobber Splashes”** subtitle matches the template image with sufficient confidence, the bot performs a right-click.

To stop the bot, press `Ctrl + C` in the terminal.


## ⚠️ Disclaimer

This project is provided for educational purposes. Automated gameplay may be restricted by individual Minecraft servers or their rules. Use it responsibly.

## 📄 License

No license has been specified yet. Add a `LICENSE` file if you want to define how others may use, modify, and distribute this project.

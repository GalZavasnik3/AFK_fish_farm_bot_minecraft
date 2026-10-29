# FK Fish Farm Bot Minecraft 🎣

A simple Python-based Minecraft fishing bot that automatically detects the fishing bobber using image recognition and performs a right-click when the bobber is detected.

## ✨ Features

- 🎯 Detects the fishing bobber using OpenCV template matching.
- 🖥️ Scans the bottom-right area of the screen.
- 🖱️ Automatically right-clicks when the bobber is detected.
- ⚙️ Configurable detection confidence and scan delay.
- 🐍 Written in Python.

## 📋 Requirements

- Python 3.10 or newer recommended.
- Minecraft running on your computer.
- The following Python libraries:
  - `PyAutoGUI`
  - `opencv-python`
  - `NumPy`
  - `Pillow` (used by PyAutoGUI for screenshot functionality)

## 📁 Project Structure

Make sure both files are in the **same folder**:

```text
FK-Fish-Farm-Bot-Minecraft/
├── main.py
├── fishing_bobber.png
└── README.md
```

- `main.py` — The Python script that runs the bot.
- `fishing_bobber.png` — The template image used to detect the fishing bobber.
- `README.md` — Project documentation.

**Important:** The image file must be named exactly `fishing_bobber.png` and must be located in the same directory as `main.py`.

## 📦 Installation

### 1. Install Python

Download Python from [python.org](https://www.python.org/downloads/) if you don't already have it installed.

### 2. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/FK-Fish-Farm-Bot-Minecraft.git
cd FK-Fish-Farm-Bot-Minecraft
```

Replace `YOUR-USERNAME` with your GitHub username.

Alternatively, download the repository as a ZIP file and extract it.

### 3. Install dependencies

Open a terminal in the project folder and run:

```bash
python -m pip install pyautogui opencv-python numpy pillow
```

On some systems, you may need to use `python3` instead of `python`.

## 🖼️ Setting Up the Bobber Image

1. Open Minecraft and cast your fishing rod.
2. Take a screenshot of the fishing bobber.
3. Crop the image tightly around the bobber.
4. Save the image as `fishing_bobber.png`.
5. Place it in the same folder as `main.py`.

For best results, use a clear image that matches the bobber's appearance in your game.

## 🚀 Usage

1. Start Minecraft.
2. Equip your fishing rod and cast your fishing line.
3. Make sure `main.py` and `fishing_bobber.png` are in the same folder.
4. Run the script:

```bash
python main.py
```

The bot will continuously scan the bottom-right portion of your screen. When the bobber image is detected with sufficient confidence, it will perform a right-click.

To stop the bot, press `Ctrl + C` in the terminal.

## ⚙️ Configuration

You can adjust these settings in `main.py`:

```python
IMAGE_PATH = "fishing_bobber.png"
CONFIDENCE = 0.8
CHECK_DELAY = 0.5
```

| Setting | Description |
|---|---|
| `IMAGE_PATH` | Path to the bobber template image. |
| `CONFIDENCE` | Minimum matching score required to trigger a click. Lower values may detect more matches but can cause false detections. |
| `CHECK_DELAY` | Delay in seconds between screen checks. |

The bot scans the bottom-right 40% of the screen, starting at 60% of the screen width and height.

## 🛠️ Troubleshooting

**The bobber is not detected**
- Make sure `fishing_bobber.png` matches the bobber's appearance.
- Try lowering `CONFIDENCE` to `0.7`.
- Make sure the bobber is visible within the scanned screen area.

**The script cannot find the image**
- Check that the file is named exactly `fishing_bobber.png`.
- Make sure the image and `main.py` are in the same folder.
- Run the script from the project directory.

**The script cannot take screenshots or click**
- Check your operating system's screen-capture and accessibility permissions.
- Make sure Minecraft is visible and running.

**The script crashes when loading the image**
- Make sure `fishing_bobber.png` is a valid image file.
- Install the dependencies again using the installation command above.

## ⚠️ Disclaimer

This project is provided for educational purposes. Automated gameplay may be restricted by individual Minecraft servers or their rules. Use it responsibly.

## 📄 License

No license has been specified yet. Add a `LICENSE` file if you want to define how others may use, modify, and distribute this project.

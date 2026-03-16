# Installation

## Requirements

- Windows 10 or later
- Python 3.8+ (if running from source)

## Download

Download the latest release from [GitHub Releases](https://github.com/warwakei/coords/releases)

### Option 1: Executable (Recommended)

1. Download `main.exe` from the latest release
2. Run the executable
3. The overlay window will appear automatically

### Option 2: From Source

1. Clone the repository:
```bash
git clone https://github.com/warwakei/coords.git
cd coords
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## First Run

When you start Coords:
- A small overlay window appears showing your cursor coordinates
- A command prompt opens for entering commands
- The overlay follows your cursor by default

## Troubleshooting

**"Module not found" error**
- Make sure all dependencies are installed: `pip install -r requirements.txt`

**Overlay not appearing**
- Try running as administrator
- Check that your display scaling is set to 100%

**Commands not working**
- Type `help` to see all available commands
- Make sure you're typing in the command prompt, not elsewhere

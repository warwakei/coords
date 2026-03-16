import sys
import ctypes
import time
import threading
from ctypes import wintypes
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, QTimer, QPoint
from PyQt6.QtGui import QFont
from pynput import keyboard
from pynput.mouse import Button, Controller

mouse_x = 0
mouse_y = 0
window_locked = False
locked_x = 0
locked_y = 0
window_visible = True

HWND_TOPMOST = -1
SWP_NOSIZE = 0x0001
SWP_NOMOVE = 0x0002

# Key bindings
key_bindings = {}
mouse_controller = Controller()
listener = None

def get_mouse_pos():
    global mouse_x, mouse_y
    pos = wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pos))
    mouse_x = pos.x
    mouse_y = pos.y

def set_topmost(hwnd):
    ctypes.windll.user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE)

def move_cursor(x, y):
    ctypes.windll.user32.SetCursorPos(int(x), int(y))

def smooth_move_cursor(x, y, duration):
    start_x, start_y = mouse_x, mouse_y
    start_time = time.time()
    
    while time.time() - start_time < duration:
        progress = (time.time() - start_time) / duration
        current_x = start_x + (x - start_x) * progress
        current_y = start_y + (y - start_y) * progress
        move_cursor(current_x, current_y)
        time.sleep(0.01)
    
    move_cursor(x, y)

def on_press(key):
    try:
        key_char = key.char if hasattr(key, 'char') else str(key)
        if key_char in key_bindings:
            button = key_bindings[key_char]
            mouse_controller.press(button)
    except:
        pass

def on_release(key):
    try:
        key_char = key.char if hasattr(key, 'char') else str(key)
        if key_char in key_bindings:
            button = key_bindings[key_char]
            mouse_controller.release(button)
    except:
        pass

def start_listener():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

def stop_listener():
    global listener
    if listener:
        listener.stop()

class AnimatedLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.current_text = ""
    
    def set_text(self, new_text: str):
        if new_text != self.current_text:
            self.current_text = new_text
            self.setText(new_text)

class CoordsOverlay(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_position)
        self.timer.start(1)
    
    def init_ui(self):
        self.setWindowTitle("coords")
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.label = AnimatedLabel()
        self.label.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        self.label.setStyleSheet("""
            QLabel {
                color: #E0E0E0;
                background-color: rgba(20, 20, 20, 240);
                padding: 6px 10px;
                border-radius: 12px;
                border: 3px solid #C9A961;
            }
        """)
        
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setGeometry(100, 100, 200, 50)
        self.show()
        
        hwnd = int(self.winId())
        set_topmost(hwnd)
    
    def update_position(self):
        global window_locked, window_visible
        
        get_mouse_pos()
        
        text = f"X: {mouse_x}  Y: {mouse_y}"
        self.label.set_text(text)
        self.adjustSize()
        
        if not window_visible:
            return
        
        if window_locked:
            new_x, new_y = locked_x, locked_y
        else:
            offset_x = 15
            offset_y = 15
            new_x = mouse_x + offset_x
            new_y = mouse_y + offset_y
        
        screen = QApplication.primaryScreen().geometry()
        window_width = self.width()
        window_height = self.height()
        
        if new_x + window_width > screen.right():
            new_x = screen.right() - window_width - 5
        if new_x < screen.left():
            new_x = screen.left() + 5
        if new_y + window_height > screen.bottom():
            new_y = screen.bottom() - window_height - 5
        if new_y < screen.top():
            new_y = screen.top() + 5
        
        self.move(QPoint(new_x, new_y))

def print_help():
    print("""
╔════════════════════════════════════════════════════════════╗
║                    COORDS - Mini Shell                     ║
╚════════════════════════════════════════════════════════════╝

COMMANDS:
  help              - Show this help message
  version           - Show version info
  clear, cls        - Clear console
  exit, quit        - Exit program
  
CURSOR MOVEMENT:
  move <X> <Y>      - Move cursor to coordinates
  mv <X> <Y>        - Alias for move
  movecur <X> <Y>   - Alias for move
  movecursor <X> <Y> - Alias for move
  
OPTIONS (for move commands):
  -f, --force       - Force move (default)
  -s, --smooth <ms> - Smooth movement duration in ms
  -b, --back <ms>   - Return cursor after delay in ms
  -h                - Show help for move command

WINDOW CONTROL:
  window lock <X> <Y>  - Lock window at coordinates
  window follow        - Window follows cursor (default)
  window show          - Show window
  window hide          - Hide window
  window toggle        - Toggle window visibility

KEY BINDINGS:
  bind <key> <m1/m2>   - Bind key to mouse button (m1=left, m2=right)
  bind list            - Show all bindings
  bind clear           - Clear all bindings

COORDINATES:
  pos               - Show current mouse position
  copy              - Copy current coordinates to clipboard
  dist <X> <Y>      - Calculate distance to coordinates
  center            - Move cursor to screen center
  
UTILITY:
  echo <text>       - Print text
  sleep <ms>        - Sleep for milliseconds
  repeat <N> <cmd>  - Repeat command N times

EXAMPLES:
  move 100 200
  movecur 500 300 -s 500
  movecur 100 100 -b 2000
  window lock 50 50
  window follow
  dist 500 500
  repeat 3 move 100 100
  bind a m1
  bind b m2
  bind list
  bind clear
""")


def handle_command(cmd_input):
    global window_locked, locked_x, locked_y, window_visible
    
    parts = cmd_input.strip().split()
    if not parts:
        return
    
    cmd = parts[0].lower()
    
    if cmd == "help":
        print_help()
    
    elif cmd == "version":
        print("coords v1.0.0")
    
    elif cmd in ["clear", "cls"]:
        import os
        os.system("cls" if sys.platform == "win32" else "clear")
    
    elif cmd in ["exit", "quit"]:
        print("Goodbye!")
        sys.exit(0)
    
    elif cmd == "pos":
        print(f"Current position: X={mouse_x}, Y={mouse_y}")
    
    elif cmd == "copy":
        try:
            import pyperclip
            pyperclip.copy(f"{mouse_x}, {mouse_y}")
            print(f"✓ Copied: {mouse_x}, {mouse_y}")
        except ImportError:
            print("Error: pyperclip not installed")
    
    elif cmd == "dist":
        try:
            if len(parts) < 3:
                print("Usage: dist <X> <Y>")
                return
            x, y = int(parts[1]), int(parts[2])
            distance = ((mouse_x - x) ** 2 + (mouse_y - y) ** 2) ** 0.5
            print(f"Distance to ({x}, {y}): {distance:.2f} pixels")
        except ValueError:
            print("Error: Invalid coordinates")
    
    elif cmd == "center":
        screen = QApplication.primaryScreen().geometry()
        center_x = screen.width() // 2
        center_y = screen.height() // 2
        move_cursor(center_x, center_y)
        print(f"✓ Cursor moved to screen center ({center_x}, {center_y})")
    
    elif cmd == "echo":
        if len(parts) > 1:
            print(" ".join(parts[1:]))
        else:
            print()
    
    elif cmd == "sleep":
        try:
            if len(parts) < 2:
                print("Usage: sleep <ms>")
                return
            ms = int(parts[1])
            time.sleep(ms / 1000.0)
            print(f"✓ Slept for {ms}ms")
        except ValueError:
            print("Error: Invalid time")
    
    elif cmd == "repeat":
        try:
            if len(parts) < 3:
                print("Usage: repeat <N> <command> [args...]")
                return
            n = int(parts[1])
            repeat_cmd = " ".join(parts[2:])
            for i in range(n):
                print(f"[{i+1}/{n}] ", end="")
                handle_command(repeat_cmd)
        except ValueError:
            print("Error: Invalid count")
    
    elif cmd in ["move", "mv", "movecur", "movecursor"]:
        try:
            if len(parts) < 3:
                print("Usage: move <X> <Y> [options]")
                print("Options: -f/--force, -s/--smooth <ms>, -b/--back <ms>")
                return
            
            x, y = int(parts[1]), int(parts[2])
            force = False
            smooth = None
            back = None
            
            i = 3
            while i < len(parts):
                if parts[i] in ["-f", "--force"]:
                    force = True
                elif parts[i] in ["-s", "--smooth"]:
                    if i + 1 < len(parts):
                        smooth = int(parts[i + 1]) / 1000.0
                        i += 1
                elif parts[i] in ["-b", "--back"]:
                    if i + 1 < len(parts):
                        back = int(parts[i + 1]) / 1000.0
                        i += 1
                i += 1
            
            if smooth:
                threading.Thread(target=smooth_move_cursor, args=(x, y, smooth), daemon=True).start()
            else:
                move_cursor(x, y)
            
            if back:
                def return_cursor():
                    time.sleep(back)
                    move_cursor(mouse_x, mouse_y)
                threading.Thread(target=return_cursor, daemon=True).start()
            
            print(f"✓ Cursor moved to ({x}, {y})")
        
        except ValueError:
            print("Error: Invalid coordinates")
    
    elif cmd == "window":
        if len(parts) < 2:
            print("Usage: window <lock|follow|show|hide|toggle> [X Y]")
            return
        
        subcmd = parts[1].lower()
        
        if subcmd == "lock":
            if len(parts) < 4:
                print("Usage: window lock <X> <Y>")
                return
            try:
                locked_x, locked_y = int(parts[2]), int(parts[3])
                window_locked = True
                print(f"✓ Window locked at ({locked_x}, {locked_y})")
            except ValueError:
                print("Error: Invalid coordinates")
        
        elif subcmd == "follow":
            window_locked = False
            print("✓ Window following cursor")
        
        elif subcmd == "show":
            window_visible = True
            print("✓ Window shown")
        
        elif subcmd == "hide":
            window_visible = False
            print("✓ Window hidden")
        
        elif subcmd == "toggle":
            window_visible = not window_visible
            print(f"✓ Window {'shown' if window_visible else 'hidden'}")
        
        else:
            print("Unknown window command")
    
    elif cmd == "bind":
        if len(parts) < 2:
            print("Usage: bind <key> <m1/m2> | bind list | bind clear")
            return
        
        subcmd = parts[1].lower()
        
        if subcmd == "list":
            if not key_bindings:
                print("No bindings set")
            else:
                for key, button in key_bindings.items():
                    button_name = "Left" if button == Button.left else "Right"
                    print(f"  {key} → {button_name}")
        
        elif subcmd == "clear":
            key_bindings.clear()
            print("✓ All bindings cleared")
        
        else:
            if len(parts) < 3:
                print("Usage: bind <key> <m1/m2>")
                return
            
            key = parts[1].lower()
            button_str = parts[2].lower()
            
            if button_str == "m1":
                key_bindings[key] = Button.left
                print(f"✓ Bound '{key}' to Left Mouse Button")
            elif button_str == "m2":
                key_bindings[key] = Button.right
                print(f"✓ Bound '{key}' to Right Mouse Button")
            else:
                print("Error: Use m1 (left) or m2 (right)")
    
    else:
        print(f"Unknown command: {cmd}. Type 'help' for commands.")

def console_loop():
    print_help()
    while True:
        try:
            cmd = input("coords> ").strip()
            if cmd.lower() == "exit":
                break
            handle_command(cmd)
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    overlay = CoordsOverlay()
    
    start_listener()
    
    console_thread = threading.Thread(target=console_loop, daemon=True)
    console_thread.start()
    
    try:
        sys.exit(app.exec())
    finally:
        stop_listener()

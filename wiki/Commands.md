# Commands Reference

## System

| Command | Description |
|---------|-------------|
| `help` | Show help message with all commands |
| `version` | Show version info |
| `clear` / `cls` | Clear console |
| `exit` / `quit` | Exit program |

## Cursor Movement

### Basic Movement
```
move <X> <Y>
mv <X> <Y>
movecur <X> <Y>
movecursor <X> <Y>
```

Move cursor to exact coordinates.

### Options
- `-f, --force` - Force move (default)
- `-s, --smooth <ms>` - Smooth movement duration in milliseconds
- `-b, --back <ms>` - Return cursor to original position after delay

**Examples:**
```
move 100 200
movecur 500 300 -s 500
movecur 100 100 -b 2000
```

## Window Control

```
window lock <X> <Y>    # Lock overlay at coordinates
window follow          # Overlay follows cursor (default)
window show            # Show overlay window
window hide            # Hide overlay window
window toggle          # Toggle overlay visibility
```

## Coordinates

```
pos                    # Show current mouse position
copy                   # Copy current coordinates to clipboard
dist <X> <Y>           # Calculate distance to coordinates
center                 # Move cursor to screen center
```

**Examples:**
```
pos
copy
dist 500 500
center
```

## Key Bindings

Bind keyboard keys to mouse button actions.

```
bind <key> <m1/m2>     # Bind key to mouse button
bind list              # Show all active bindings
bind clear             # Clear all bindings
```

**Mouse buttons:**
- `m1` - Left mouse button
- `m2` - Right mouse button

**Examples:**
```
bind a m1
bind b m2
bind list
bind clear
```

## Double Tap

Register keys to repeat when pressed. When triggered, the key will press 3 times total (original + 2 repeats) with specified delay between each press.

```
doubletap <key> <ms>   # Register key for double tap
dt <key> <ms>          # Alias for doubletap
dt list                # Show all double tap bindings
dt clear               # Clear all double tap bindings
```

**Examples:**
```
dt space 50
dt enter 100
dt list
dt clear
```

## Utility

```
echo <text>            # Print text to console
sleep <ms>             # Sleep for milliseconds
repeat <N> <cmd>       # Repeat command N times
```

**Examples:**
```
echo Hello World
sleep 1000
repeat 3 move 100 100
```

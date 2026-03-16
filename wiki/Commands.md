# Commands Reference

## Navigation

| Command | Alias | Description |
|---------|-------|-------------|
| `help` | - | Show help message |
| `version` | - | Show version info |
| `clear`, `cls` | - | Clear console |
| `exit`, `quit` | - | Exit program |

## Cursor Movement

### Basic Movement
```
move <X> <Y>
mv <X> <Y>
movecur <X> <Y>
movecursor <X> <Y>
```

### Options
- `-f, --force` - Force move (default)
- `-s, --smooth <ms>` - Smooth movement duration in milliseconds
- `-b, --back <ms>` - Return cursor after delay in milliseconds

**Examples:**
```
move 100 200
movecur 500 300 -s 500
movecur 100 100 -b 2000
```

## Window Control

```
window lock <X> <Y>    # Lock window at coordinates
window follow          # Window follows cursor (default)
window show            # Show window
window hide            # Hide window
window toggle          # Toggle window visibility
```

## Key Bindings

```
bind <key> <m1/m2>     # Bind key to mouse button
bind list              # Show all bindings
bind clear             # Clear all bindings
```

**Mouse buttons:**
- `m1` - Left mouse button
- `m2` - Right mouse button

## Double Tap

```
doubletap <key> <ms>   # Register key for double tap
dt <key> <ms>          # Alias for doubletap
dt list                # Show all double tap bindings
dt clear               # Clear all double tap bindings
```

When a registered key is pressed, it will repeat 2 additional times with the specified delay.

## Coordinates

```
pos                    # Show current mouse position
copy                   # Copy coordinates to clipboard
dist <X> <Y>           # Calculate distance to coordinates
center                 # Move cursor to screen center
```

## Utility

```
echo <text>            # Print text
sleep <ms>             # Sleep for milliseconds
repeat <N> <cmd>       # Repeat command N times
```

**Examples:**
```
echo Hello World
sleep 1000
repeat 3 move 100 100
```

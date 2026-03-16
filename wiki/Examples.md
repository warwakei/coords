# Usage Examples

## Basic Cursor Tracking

Simply run the application and watch the overlay window show your cursor coordinates in real-time.

```
coords> pos
Current position: X=1920, Y=1080
```

## Moving Cursor to Specific Position

Move cursor to coordinates (500, 300):
```
coords> move 500 300
✓ Cursor moved to (500, 300)
```

## Smooth Cursor Movement

Move cursor smoothly over 1 second:
```
coords> movecur 100 100 -s 1000
✓ Cursor moved to (100, 100)
```

## Return Cursor After Action

Move cursor and return it after 2 seconds:
```
coords> movecur 500 500 -b 2000
✓ Cursor moved to (500, 500)
```

## Lock Window Position

Lock the overlay window at a specific location:
```
coords> window lock 50 50
✓ Window locked at (50, 50)
```

Resume following cursor:
```
coords> window follow
✓ Window following cursor
```

## Hide/Show Overlay

Hide the overlay window:
```
coords> window hide
✓ Window hidden
```

Show it again:
```
coords> window show
✓ Window shown
```

Toggle visibility:
```
coords> window toggle
✓ Window shown
```

## Key Binding to Mouse Buttons

Bind key 'a' to left mouse button:
```
coords> bind a m1
✓ Bound 'a' to Left Mouse Button
```

Bind key 'b' to right mouse button:
```
coords> bind b m2
✓ Bound 'b' to Right Mouse Button
```

View all bindings:
```
coords> bind list
  a → Left
  b → Right
```

Clear all bindings:
```
coords> bind clear
✓ All bindings cleared
```

## Double Tap Keys

Register key 'space' to double-tap with 50ms delay:
```
coords> dt space 50
✓ Registered double tap for 'space' with 50ms delay
```

Now pressing space will trigger it 3 times total (original + 2 repeats with 50ms delay between each).

Register multiple keys:
```
coords> dt enter 100
✓ Registered double tap for 'enter' with 100ms delay

coords> dt shift 75
✓ Registered double tap for 'shift' with 75ms delay
```

View double tap bindings:
```
coords> dt list
  space → 50ms
  enter → 100ms
  shift → 75ms
```

Clear all double tap bindings:
```
coords> dt clear
✓ All double tap bindings cleared
```

## Calculate Distance

Find distance between current position and target:
```
coords> dist 500 500
Distance to (500, 500): 707.11 pixels
```

## Copy Coordinates

Copy current position to clipboard:
```
coords> copy
✓ Copied: 1920, 1080
```

## Move to Screen Center

Move cursor to the center of the screen:
```
coords> center
✓ Cursor moved to screen center (1920, 1080)
```

## Repeat Commands

Execute a command multiple times:
```
coords> repeat 3 move 100 100
[1/3] ✓ Cursor moved to (100, 100)
[2/3] ✓ Cursor moved to (100, 100)
[3/3] ✓ Cursor moved to (100, 100)
```

## Sleep and Delays

Sleep for a specified duration:
```
coords> sleep 1000
✓ Slept for 1000ms
```

## Print Text

Echo text to console:
```
coords> echo Hello World
Hello World
```

## Workflow Example

Automate a repetitive task:
```
coords> move 100 100
✓ Cursor moved to (100, 100)

coords> sleep 500
✓ Slept for 500ms

coords> move 200 200 -s 300
✓ Cursor moved to (200, 200)

coords> window hide
✓ Window hidden
```

## Gaming Setup

Bind keys for gaming:
```
coords> bind e m1
✓ Bound 'e' to Left Mouse Button

coords> bind r m2
✓ Bound 'r' to Right Mouse Button

coords> dt e 50
✓ Registered double tap for 'e' with 50ms delay
```

Now 'e' triggers left click (3 times with double tap), 'r' triggers right click.

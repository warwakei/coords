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

## Key Binding to Mouse Buttons

Bind key 'a' to left mouse button:
```
coords> bind a m1
✓ Bound 'a' to Left Mouse Button
```

View all bindings:
```
coords> bind list
  a → Left
  b → Right
```

## Double Tap Keys

Register key 'space' to double-tap with 50ms delay:
```
coords> dt space 50
✓ Registered double tap for 'space' with 50ms delay
```

Now pressing space will trigger it 3 times total (original + 2 repeats).

View double tap bindings:
```
coords> dt list
  space → 50ms
  enter → 100ms
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

## Repeat Commands

Execute a command multiple times:
```
coords> repeat 3 move 100 100
[1/3] ✓ Cursor moved to (100, 100)
[2/3] ✓ Cursor moved to (100, 100)
[3/3] ✓ Cursor moved to (100, 100)
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

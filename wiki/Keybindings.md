# Key Bindings Guide

## Overview

Key bindings allow you to map keyboard keys to mouse button actions. This is useful for automating mouse clicks with keyboard shortcuts.

## Basic Setup

### Bind a Key to Left Mouse Button

```
bind a m1
```

Now pressing 'a' will simulate a left mouse click.

### Bind a Key to Right Mouse Button

```
bind b m2
```

Now pressing 'b' will simulate a right mouse click.

## Managing Bindings

### View All Bindings

```
bind list
```

Output:
```
  a → Left
  b → Right
  c → Left
```

### Clear All Bindings

```
bind clear
✓ All bindings cleared
```

## Supported Keys

You can bind any keyboard key. Common examples:

| Key | Usage |
|-----|-------|
| `a-z` | Letter keys |
| `0-9` | Number keys |
| `space` | Spacebar |
| `enter` | Enter key |
| `shift` | Shift key |
| `ctrl` | Control key |
| `alt` | Alt key |
| `tab` | Tab key |
| `esc` | Escape key |
| `f1-f12` | Function keys |

## Double Tap with Key Bindings

You can combine key bindings with double tap:

```
bind a m1
dt a 50
```

Now pressing 'a' will:
1. Trigger left mouse button
2. Wait 50ms
3. Trigger left mouse button again
4. Wait 50ms
5. Trigger left mouse button a third time

## Practical Examples

### Gaming Setup

```
bind e m1
bind r m2
dt e 100
```

Bind 'e' to left click with double-tap, 'r' to right click.

### Automation

```
bind space m1
bind shift m2
```

Use spacebar for left clicks, shift for right clicks.

### Workflow

```
bind a m1
bind s m2
bind d m1
```

Create a custom key layout for your workflow.

## Troubleshooting

**Binding not working**
- Make sure the key name is correct
- Try using lowercase letters
- Check that the binding was registered with `bind list`

**Key conflicts**
- Some keys may be reserved by your system
- Try a different key if one doesn't work

**Clearing bindings**
- Use `bind clear` to remove all bindings at once
- Or just create a new binding to overwrite the old one

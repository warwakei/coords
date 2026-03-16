# Frequently Asked Questions

## General

**Q: What is Coords?**
A: Coords is a lightweight Windows utility that tracks your cursor position in real-time and provides automation features like cursor movement, key bindings, and double-tap functionality.

**Q: Is it free?**
A: Yes, Coords is open source and free to use.

**Q: Does it work on Mac/Linux?**
A: Currently, Coords only supports Windows. The code uses Windows-specific APIs for cursor control.

## Installation & Setup

**Q: Do I need Python installed?**
A: No, if you download the `.exe` file. If you want to run from source, you'll need Python 3.8+.

**Q: Where do I download it?**
A: Download from [GitHub Releases](https://github.com/warwakei/coords/releases)

**Q: Do I need to run it as administrator?**
A: Usually no, but if you have permission issues, try running as administrator.

**Q: Can I run it in the background?**
A: The command prompt window must stay open. You can minimize it, but closing it will stop the application.

## Features

**Q: How do I see my cursor coordinates?**
A: The overlay window shows your coordinates in real-time. You can also use the `pos` command.

**Q: Can I move the overlay window?**
A: Yes, use `window lock <X> <Y>` to lock it at a position, or `window follow` to make it follow your cursor.

**Q: How do I hide the overlay?**
A: Use `window hide` to hide it, `window show` to show it again.

**Q: What's the difference between key bindings and double tap?**
A: Key bindings map keys to mouse buttons. Double tap makes a key repeat multiple times when pressed.

**Q: Can I use both key bindings and double tap on the same key?**
A: Yes, you can bind a key to a mouse button and also register it for double tap.

## Troubleshooting

**Q: The overlay window isn't showing**
A: Try running as administrator or check your display scaling settings.

**Q: Commands aren't working**
A: Make sure you're typing in the command prompt window, not elsewhere. Type `help` to see all commands.

**Q: Key binding isn't working**
A: Check that the key name is correct with `bind list`. Some keys might be reserved by your system.

**Q: Cursor movement is jerky**
A: Use the `-s` flag for smooth movement: `move 100 100 -s 500`

**Q: The application crashes**
A: Try running as administrator. If it persists, check that all dependencies are installed.

## Performance

**Q: Does Coords use a lot of CPU?**
A: No, it's very lightweight. The overlay updates at 1000Hz but uses minimal resources.

**Q: Can I run multiple instances?**
A: Yes, but they'll share the same overlay window.

**Q: Does it work with games?**
A: Yes, but some games may block key bindings or cursor movement for security reasons.

## Advanced

**Q: Can I automate complex sequences?**
A: Yes, use the `repeat` command to run commands multiple times, and `sleep` to add delays.

**Q: Can I save my bindings?**
A: Currently, bindings are not saved between sessions. You'll need to set them up each time.

**Q: How do I contribute?**
A: Visit the [GitHub repository](https://github.com/warwakei/coords) to contribute.

## Getting Help

- Check the [Commands](./Commands.md) reference
- Review [Examples](./Examples.md) for usage patterns
- See [Keybindings](./Keybindings.md) for binding setup
- Open an issue on [GitHub](https://github.com/warwakei/coords/issues)

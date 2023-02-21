# LibreDiscordEmojis
Use emojis and stickers in Discord for free without buying Nitro. Use the emoji and sticker selector to send them. Keep in mind that you cannot
use the emojis inserted in text and that you cannot send them using the `:emoji:` shortcut.

# Is it save to use?
**No**, using this script or any other programs that modifie Discord is **against the TOS** and can lead to a ban of your account. **Use this
script at your own risk!**

# Installation
## Linux
Follow the instructions as listed below if you are running a linux system (should work on windows too, if required packages are installed).
Keep in mind that discord has to be closed before starting `main.py`.
```
git clone http://github.com/danielfvm/LibreDiscordEmojis
cd LibreDiscordEmojis
pip install -r requirements.txt
python main.py
```

## Windows
Download the `.exe` file from releases. Make sure discord is not running and start the executable. It should start discord automatically with
the script applied.

# How it works?
This works by injecting the `script.js` file into Discord which can detect if a user clicks on an emoji that has been disabled. 
When clicking on the emoji, the url of the image is being send to the python script which uses the Keyboard to write the URL into the
message box and then sends it.

# Why is there a webserver running in the py script?
I was not able to send the url of the emoji directly from the injected script. If you know a way how to insert and send a text into the
discord chat box, please feel free to make a pull request.

# Dependencies
This project makes use of code from the [electron-inject](https://github.com/tintinweb/electron-inject) project for injecting the `script.js` 
file into Discord (See `injector.py`).

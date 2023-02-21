#!/bin/bash
set -e

# This script is updating the .desktop file to start the main.py
DISCORD_FOLDER=$(realpath $(whereis discord | cut -d' ' -f2-) | rev | cut -d'/' -f2- | rev)
sed "s+Exec.*+Exec=$PWD/main.py+g" $DISCORD_FOLDER/discord.desktop > /tmp/discord.desktop
sed "s+Path.*+Path=$PWD+g" /tmp/discord.desktop > $DISCORD_FOLDER/discord.desktop

echo "Finished, reload session to apply change and start discord."

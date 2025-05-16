#!/bin/bash


LOG_FILE="/Users/alekyanarne/Desktop/Web Apps/projects/gmBot/gm_bot.log"

source /Users/alekyanarne/Desktop/"Web Apps"/projects/gmBot/pyenv/bin/activate

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting script..." >> "$LOG_FILE"
python /Users/alekyanarne/Desktop/"Web Apps"/projects/gmBot/send_gm_to_dad.py
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Script finished..." >> "$LOG_FILE"
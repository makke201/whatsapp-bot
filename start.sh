# Install Chromium
apt-get update
apt-get install -y chromium-browser

# Install Python dependencies
pip install -r requirements.txt

# Run the bot
python whatsapp_bot.py

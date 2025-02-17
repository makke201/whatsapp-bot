from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
input("🚀 Scan the QR code on WhatsApp Web and press Enter to continue...")

# Function to send WhatsApp messages
def send_whatsapp_message(number, message):
    # Ensure the phone number is in the correct format
    number = number.replace("+", "").replace(" ", "")
    
    # Generate the correct WhatsApp Web URL
    url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
    
    driver.get(url)
    time.sleep(10)  # Wait for chat to load
    
    try:
        send_button = driver.find_element("xpath", "//span[@data-icon='send']")
        send_button.click()
        time.sleep(5)
        print(f"✅ Message sent to {number}")
    except:
        print(f"❌ Failed to send message to {number}")

# Example: Correct phone number format
send_whatsapp_message("60123456789", "✅ Your grocery order is confirmed! 🛒 Delivery will be arranged soon.")

# Keep the browser open
while True:
    time.sleep(1)

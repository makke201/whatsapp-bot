from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome WebDriver with headless mode for Railway Deployment
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent crashes

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
print("📲 Scan the QR code on WhatsApp Web and press Enter to continue...")

# Function to send WhatsApp messages
def send_whatsapp_message(number, message):
    number = number.replace("+", "").replace(" ", "")  # Ensure correct phone format
    url = f"https://web.whatsapp.com/send?phone={number}&text={message}"

    driver.get(url)
    time.sleep(10)  # Wait for chat to load

    try:
        send_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']"))
        )
        send_button.click()
        time.sleep(5)
        print(f"✅ Message sent to {number}!")
    except Exception as e:
        print(f"❌ Failed to send message to {number}: {e}")

# Example: Send a test message
send_whatsapp_message("60123456789", "Your grocery order is confirmed! 🛒 Delivery will be arranged soon.")

# Keep the script running for handling multiple messages
while True:
    time.sleep(10)

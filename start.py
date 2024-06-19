import time, selenium, random, string, pyperclip

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
# Headless mode // chrome_options.add_argument("--headless")    
chrome_options.add_extension('0.2.1_0.crx')  # Eklenti dosyasının yolu

# Tarayıcı başlığı ayarlarını yapılandır
prefs = {
    "intl.accept_languages": "en-US, en"
}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
url = "https://auth.riotgames.com/login#client_id=play-valorant-web-prod&nonce=NzcsMTA2LDEwMCwx&prompt=signup&redirect_uri=https%3A%2F%2Fplayvalorant.com%2Fopt_in%2F%3Fredirect%3D%2Fdownload%2F&response_type=token%20id_token&scope=account%20openid&state=c2lnbnVw&ui_locales=en'"


driver.get(url)
current_url = driver.current_url

time.sleep(2)

def randomString(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def submit():
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    
#email
driver.find_element(By.NAME, "email").send_keys(randomString(10) + '@' + randomString(5) + '.com');
submit()

#date
driver.find_element(By.NAME, "date_of_birth_day").send_keys("07");
driver.find_element(By.NAME, "date_of_birth_month").send_keys("06");
driver.find_element(By.NAME, "date_of_birth_year").send_keys("1997");
submit()


username_password = randomString(24);
#username
driver.find_element(By.NAME, "username").send_keys(username_password);
submit()

#password
driver.find_element(By.NAME, "password").send_keys(username_password);
driver.find_element(By.NAME, "confirm_password").send_keys(username_password);
submit()

# URL değişene kadar beklemek için while döngüsü
while driver.current_url == current_url:
    
    print(f"Kayıt işlemi tamamlanıyor...")
    time.sleep(1)  # Bir saniye bekle

print(f"Kayıt Tamamlandı")

# Tarayıcıyı kapat
driver.quit()

pyperclip.copy(username_password)

import subprocess
import sys

def run_script(script_name):
    result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
    print(result.stdout)

# Aynı klasördeki script.py dosyasını çalıştır
run_script('riot.py')


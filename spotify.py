import os
import random
import string
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from colorama import Fore

try:
    import undetected_chromedriver as uc
except ModuleNotFoundError:
    os.system('pip install undetected-chromedriver')
    import undetected_chromedriver as uc

def create_hm_account(username, email, password):
    options = uc.ChromeOptions()
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    driver = uc.Chrome(options=options, service_log_path=os.devnull)
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 100)

    print(Fore.LIGHTMAGENTA_EX + "Tarayıcı açılıyor")
    
    driver.get("https://www2.hm.com/tr_tr/register")
    while True:
        try:
            driver.find_element(By.ID, "email").send_keys(email)
            driver.find_element(By.NAME, "password").send_keys(password)
            driver.find_element(By.NAME, "day").send_keys("1")
            driver.find_element(By.NAME, "month").send_keys("1")
            driver.find_element(By.NAME, "year").send_keys("2000")
            time.sleep(.8)
            driver.find_element(By.CLASS_NAME, 'RegisterFormHM--submit__1wHS7').click()
            break
        except:
            pass
        try:
            driver.find_element(By.ID, "name").send_keys(firstname)
            break
        except:
            pass

    time.sleep(1)
    print("Hesap Oluşturuldu!")

    try:
        # Bu kısmı değiştirdik
        wait.until(EC.presence_of_element_located((By.XPATH, '//img[contains(@alt, "Tüm müziksever H&M Member\'larımız için")]/ancestor::a'))).click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'RewardButtons-module--rewardButton__ZryN-'))).click()
        print("Yükle tuşuna basıldı!")
        offer_code_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'OfferCard-module--offerCodeText__1iRLT')]")))
        offer_code = offer_code_element.text
        print(f"Offer Code: {offer_code}")

        # Kodu dosyaya ekleyin
        with open("codes.txt", "a") as file:
            file.write(offer_code + "\n")
            
    except Exception as e:
        print("Bir hata oluştu:", e)
    finally:
        driver.quit()

number_of_codes_to_collect = 10  
for _ in range(number_of_codes_to_collect):
    username = f"a{''.join(random.sample(string.ascii_lowercase + string.digits, 15))}"
    firstname = f"A{''.join(random.sample(string.ascii_lowercase + string.digits, 14))}"
    lastname = f"L{''.join(random.sample(string.ascii_lowercase + string.digits, 14))}"
    password = f"A{''.join(random.sample(string.ascii_lowercase + string.digits, 15))}&*"
    email = f"{firstname}.{lastname}@example.com"
    
    print(Fore.LIGHTMAGENTA_EX + f"H&M Hesabı Oluşturuluyor | Kullanıcı Adı: {username} Şifre: {password} E-Mail: {email}")
    create_hm_account(username, email, password)
    time.sleep(5)

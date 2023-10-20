from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def login_to_facebook(username, password):
    # Set opsi User-Agent
    chrome_options = Options()
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

    # Inisialisasi driver Chrome dengan opsi yang telah diatur
    # driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
    driver = webdriver.Chrome(options=chrome_options)

    # Mengunjungi situs Facebook
    driver.get("https://www.facebook.com")


    try:
        username_elem = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.ID, "email")))
        password_elem = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.ID, "pass")))
        
        username_elem.send_keys(username)
        password_elem.send_keys(password)

        login_button = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='royal_login_button']")))
        time.sleep(random.randint(2, 5))  # Menambahkan penundaan acak antara 2 hingga 5 detik
        login_button.click()

        # Menunggu hingga halaman selesai dimuat setelah login
        WebDriverWait(driver, 7).until_not(EC.url_to_be("https://www.facebook.com/"))

        # Memastikan berada di halaman setelah login
        if "login" not in driver.current_url:
            print("Login berhasil!")
            return driver
        else:
            print("Login gagal!")
            driver.quit()
            return None
    except Exception as e:
        print("Terjadi kesalahan saat login:", str(e))
        driver.quit()
        return None

def like_facebook_post(driver, post_url):
    try:
        driver.get(post_url)

        # Menunggu hingga halaman selesai dimuat
        WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Suka')]")))

        like_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Suka')]")
        like_button.click()
        print("Postingan telah dilike!")
    except Exception as e:
        print("Tidak dapat menemukan tombol like atau postingan tidak ditemukan:", str(e))

if __name__ == "__main__":
    akun = [
    ("mediaku@fifi.luth.my.id", "Baru123*#"),
    ("uwjatofyatzftd@northsixty.com", "Baru123*#"),
    ("putri@strapi.luth.my.id", "Baru123*#")
]
    postingan = [
        "https://web.facebook.com/eriyant.ana/posts/pfbid034778KeZ2tbAen72EKBWa8nxHNHead3cQySQhLpyqQpp5zvYKdcKmfuQgJDqHtodJl",
        "https://web.facebook.com/muhd.basyir.330/posts/pfbid02Me58U7YXJTXwt3MNvbuRcdcNRW4qsaX5u2V5nn1JqHKKeETv7bpvynHmoWxzDoYjl",
        "https://web.facebook.com/repsus.lsm.5/posts/pfbid0eyMNetn8NZYi6Z8Vy84yGT8XgY1usFQKkn1BkgjcrNt64uxsT25ELvwztqJxmACml"
    ]

    for username, password in akun:
        driver = login_to_facebook(username, password)

        if driver is not None:
            for post_url in postingan:
                like_facebook_post(driver, post_url)

            # Logout dari akun saat ini
            driver.get("https://www.facebook.com/logout.php")
            driver.quit()

    print("Proses selesai.")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from colorama import Fore, Style, init
init()


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys

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


def like_and_comment_on_facebook_post(driver, post_url, comments):
    try:
        driver.get(post_url)

        # Menunggu hingga halaman selesai dimuat
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Suka')]")))

        like_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Suka')]")
        like_button.click()
        print(Fore.GREEN + "Postingan telah dilike!" + Style.RESET_ALL)
        
        # Tunggu 2 detik
        time.sleep(2)

        # Menunggu hingga tombol "Komentari" muncul
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Komentari')]")))

        comment_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Komentari')]")
        comment_button.click()

        # Tunggu 1 detik
        time.sleep(1)

        # Menunggu hingga input komentar muncul
        WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true']")))

        comment_input = driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true']")

        for comment in comments:
            for char in comment:
                comment_input.send_keys(char)
                # Tunggu antara 0.01 hingga 0.1 detik (secara acak)
                time.sleep(random.uniform(0.001, 0.01))
            comment_input.send_keys(Keys.RETURN)

            # Tunggu 3 detik setelah mengirim komentar
            time.sleep(3)
            print(Fore.GREEN + f"Komentar '{comment}' telah ditambahkan!" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"Tidak dapat menemukan tombol komentar atau postingan tidak ditemukan: {str(e)}" + Style.RESET_ALL)


if __name__ == "__main__":
    akun = [
    # ("mediaku@fifi.luth.my.id", "Baru123*#"),
    ("uwjatofyatzftd@northsixty.com", "Baru123*#"),
    ("putri@strapi.luth.my.id", "Baru123*#"),
    ("nipoqafe.upamiban@labworld.org", "Baru123*#")
]

    postingan = [
        "https://web.facebook.com/permalink.php?story_fbid=pfbid037aP4GQAmiRugzkzRknL59Jku5h1jGpFTzTkcNxjLFeNg7JmSnoDuzFTeoq28TVv7l&id=104130165689778"
    ]

    comments = ["MashaaAllah Indah sekali", "yang belum punya rumah semoga bisa segara punya", "tetap semnagat dalam berkreasi"]

    for i, (username, password) in enumerate(akun):
        driver = login_to_facebook(username, password)

        if driver is not None:
            post_url = postingan[0]  # Gunakan postingan pertama
            comment = comments[i % len(comments)]  # Gunakan komentar sesuai dengan indeks akun

            like_and_comment_on_facebook_post(driver, post_url, [comment])

            # Logout dari akun saat ini
            driver.get("https://www.facebook.com/logout.php")
            driver.quit()

    print(Fore.GREEN + "Proses selesai." + Style.RESET_ALL)

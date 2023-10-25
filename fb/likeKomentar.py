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
            print("akun " + username)
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

        like_button = None
        comment_button = None

        # Coba menemukan tombol "Suka" dengan teks dalam bahasa Inggris
        try:
            like_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Suka')]")
        except NoSuchElementException:
            pass

        # Jika tombol "Suka" dalam bahasa Inggris tidak ditemukan, coba dalam bahasa Indonesia
        if like_button is None:
            try:
                like_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Like')]")
            except NoSuchElementException:
                # Jika tidak berhasil, coba mencari tombol lain
                like_button = driver.find_element(By.XPATH, "//a[contains(@data-sigil, 'ufi-inline-like')]")

        like_button.click()
        print(Fore.GREEN + "Postingan telah dilike!" + Style.RESET_ALL)

        time.sleep(2)

        # Coba menemukan tombol "Komentari" dengan teks dalam bahasa Inggris
        try:
            comment_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Komentari')]")
        except NoSuchElementException:
            pass

        # Jika tombol "Komentari" dalam bahasa Inggris tidak ditemukan, coba dalam bahasa Indonesia
        if comment_button is None:
            try:
                comment_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Comment')]")
            except NoSuchElementException:
                # Jika tidak berhasil, coba mencari tombol lain
                comment_button = driver.find_element(By.XPATH, "//a[contains(@data-sigil, 'feed-ufi-focus')]")

        comment_button.click()
        time.sleep(1)

        # Coba menemukan input komentar dengan atribut CSS
        try:
            comment_input = driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true']")
        except NoSuchElementException:
            # Jika tidak berhasil, coba mencari input komentar lain
            comment_input = driver.find_element(By.ID, "composerInput")

        for comment in comments:
            for char in comment:
                comment_input.send_keys(char)
                time.sleep(random.uniform(0.001, 0.01))
            comment_input.send_keys(Keys.RETURN)

            time.sleep(3)
            print(Fore.GREEN + f"Komentar '{comment}' telah ditambahkan!" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"Tidak dapat menemukan tombol atau input komentar: {str(e)}" + Style.RESET_ALL)


if __name__ == "__main__":
    akun = [
    ("mediaku@fifi.luth.my.id", "Baru123*#"),
    # ("uwjatofyatzftd@northsixty.com", "Baru123*#")
    ("putri@strapi.luth.my.id", "Baru123*#"),
    ("nipoqafe.upamiban@labworld.org", "Baru123*#"),
    ("sabilalala159@gmail.com","@12345678"),
    ("kamengpanggang@gmail.com","Bireuen12"),
    ("usahadagang316@gmail.com","Bireuen12"),
    ("ahrd3043@gmail.com","Bireuen12"),
    ("mamanoraaaa12@gmail.com","Bireuen12"),
    ("mamabayuuuu12@gmail.com","Bireuen12"),
    ("hantulauttt12@gmail.com","Bireuen12"),
    ("hantumatahari722@gmail.com","Bireuen12"),
    ("hantubulan3@gmail.com.","Bireuen12"),
    ("rumahhantu180@gmail.com","Bireuen12"),
    ("mamaliaaaa12@gmail.com","Bireuen12"),
    ("kamengbulut6@gmail.com","Bireuen12"),
    ("Cazorlas386@gmail.com","Bireuen12"),
    ("nisac4987@gmail.com","Bireuen12"),
    ("kamenghanco@gmail.com","Bireuen12"),
    ("kamengapui@gmail.com","Bireuen12"),
    ("fitriwahyunibir11@gmail.com","Bireuen12"),
    ("kopidarat875@gmail.com","Bireuen12"),
    ("riskiamoy06@gmail.com","@12345678"),
    ("kucingmanisku187@gmail.com","Bireuen12"),
    ("catatanselebritis@gmail.com","Bireuen12"),
    ("mitagunawan201@gmail.com","Bireuen12"),
    ("apismaulana1999@gmail.com","Bireuen12"),
    ("fitriwahyunibir11@gmail.com","Bireuen12"),
    ("kopidarat875@gmail.com","Bireuen12"),
    ("rudisaputra1998ml@gmail.com","Bireuen12"),
    ("Anggamaulana0945@gmail.com","Bireuen12"),
    ("Sendiriusaha154@gmail.com","Bireuen12"),
    ("buruangputih@gmail.com","Bireuen12"),
    ("pasarsiang8@gmail.com","Bireuen12"),
    ("rudisaputra1998rd@gmail.com","Bireuen12"),
    ("bellaputri099912@gmail.com","Bireuen12"),
    ("rezasaputrard603@gmail.com","Bireuen12"),
    ("mionghitam37@gmail.com","Bireuen12"),
    ("miongkuneng06@gmail.com","Bireuen12"),
    ("miongbiru21@gmail.com","Bireuen12"),
    ("forumartis99@gmail.com","Bireuen12"),
    ("merahmeong@gmail.com","Bireuen12"),
    ("hitamcicak59@gmail.com","Bireuen12"),
    ("dindarizki14912@gmail.com","Bireuen12"),
    ("mayasari1999jr@gmail.com","Bireuen12"),
    ("hayatimala733@gmail.com","Bireuen12"),
    ("daudiskandar076@gmail.com","Bireuen12"),
    ("nuddinb295@gmail.com","Bireuen12")
    ]

    postingan = [
        "https://web.facebook.com/story.php?story_fbid=pfbid028BDkHWU98pSjafT9NHtgmWKrBhJebwceDekSAMtD1AqGZZSzyeztZdrk4VTU1en2l&id=100010124465527&mibextid=Nif5oz&_rdc=1&_rdr"
    ]

    comments = ["sehat sampai hari H pak",
                "Gerakan Indonesia lebih baik ;)",
                "Aminnn",
                "Aman Indonesia",
                "mantap",
                "Anies Muhaimin",
                "Pasangan Perubahan",
                "semoga tersemogakan",
                "amin 2024",
                "juara",
                "aminnnnn",
                "amin yang terbaik",
                "pilihan terbaik",
                "aminnnnn",
                "bestttt",
                "semoga bisa memimpin negeri",
                "aminn",
                "bersama amin kita bisaa",
                "aminnn",
                "aman aminnnn",
                "amin menuju perubahan",
                "terbaikk gus",
                "sukses terus",
                "semangat pak",
                "perubahan2024",
                "selalu di hati",
                "presiden kita 2024",
                "pantang mundur demi kesuksesan",
                "yok bisa 2024",
                "patriot kita",
                " selalu di hati",
                "merdeka",
                "gas berjuang 2024",
                "Semoga sukses selalu",
                "Amiin, semoga berhasil!",
                "Teruskan perjuangan!",
                "Sukses adalah hasil kerja keras",
                "Kita bersama menuju perubahan",
                "Pantang menyerah!",
                "Semangat terus, Pak!",
                "Kita optimis 2024!",
                "Kami selalu mendukung Anda",
                "Perubahan yang kita butuhkan",
                "Sukses untuk Indonesia!",
                "Kita bangga memiliki sosok seperti Anda",
                "Ayo, menuju perubahan!",
                "Teruskan perjuangan, Pak!",
                "Patriot sejati!", "mantappp"]

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

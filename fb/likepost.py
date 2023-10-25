import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Daftar nama acak
nama_acak = [
    "hafizzah",
    "nuafrina",
    "nurul",
    "husna",
    "maulia",
    "nabila",
    "heri"
]

postingan = [
    # "https://web.facebook.com/eriyant.ana/posts/pfbid034778KeZ2tbAen72EKBWa8nxHNHead3cQySQhLpyqQpp5zvYKdcKmfuQgJDqHtodJl"
    "https://web.facebook.com/ruslanmdaud/posts/pfbid0BagAUZmS6gSNqUy9T45zf5EPfXRDvjFRHetkxhSbL7qWHSJwgPFayAPcMwncxzkVl"
]

def get_random_name():
    # Memilih satu nama secara acak dari daftar nama_acak
    return random.choice(nama_acak)

def login_to_facebook(username, password):
    # Set opsi User-Agent
    chrome_options = Options()
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")


    # Inisialisasi driver Chrome dengan opsi yang telah diatur
    driver = webdriver.Chrome(options=chrome_options)
    window = driver.current_window_handle
    driver.set_window_position(10, 10)
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
            # Tunggu hingga ikon "Home" muncul
            home_icon = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//span[@class="x1n2onr6"]'))
            )

            if home_icon.is_displayed():
                print("Akun aktif")
            else:
                print("Akun non aktif")
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

        # Mencari elemen tombol "Suka"
        like_button = driver.find_element(By.XPATH, "//div[@aria-label='Suka']")

        like_button_label = like_button.get_attribute("aria-label")

        if "Suka" in like_button_label:
            like_button.click()
            print("Postingan telah dilike!")
        else:
            print("Postingan sudah dilike sebelumnya.")

    except Exception as e:
        print("Tidak dapat menemukan tombol like atau postingan telah di like sebelumnya")



def find_and_add_friends(driver):
    try:
        # for _ in range(random.randint(1, 5)):
        for _ in range(1):
            # Mengambil satu nama secara acak dari daftar nama_acak
            random_name = get_random_name()
            friend_search_query = "https://web.facebook.com/search/top?q=" + random_name
            driver.get(friend_search_query)

            # Tunggu hingga hasil pencarian muncul
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='feed']")))

            # Temukan semua tombol "Tambah Teman" yang ada di halaman
            add_friend_buttons = driver.find_elements(By.XPATH, "//div[@aria-label='Tambah teman']")

            # Jika ada tombol "Tambah Teman," tambahkan teman sebanyak yang dihasilkan secara acak
            if add_friend_buttons:
                num_friends_to_add = random.randint(1, 2)
                for i in range(num_friends_to_add):
                    if i < len(add_friend_buttons):
                        # Tunggu sebentar sebelum menambahkan teman berikutnya
                        time.sleep(random.randint(2, 3))
                        
                        # Klik tombol "Tambah Teman" berdasarkan indeks
                        add_friend_buttons[i].click()
                        print(f"Berhasil menambahkan teman: {random_name} (Teman ke-{i + 1})")

        print("Pertemanan berhasil ditambahkan!")
    except Exception as e:
        print("Tidak dapat menambahkan teman atau terjadi kesalahan:", str(e))

def post_story(driver, status):
    try:
        # Akses halaman untuk membuat cerita
        driver.get("https://web.facebook.com/stories/create/")

        # Klik tombol "Buat Cerita Teks"
        buat_cerita_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Buat Cerita Teks')]")
        buat_cerita_button.click()

        # Tunggu hingga halaman selesai dimuat
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Mulai mengetik')]")))

        # Isi teks status dengan penundaan antara 0.001 hingga 0.01 detik per karakter
        status_textarea = driver.find_element(By.XPATH, "//textarea[@aria-invalid='false']")
        for char in status:
            status_textarea.send_keys(char)
            time.sleep(random.uniform(0.001, 0.01))

        # Penundaan sebelum mengklik tombol "Bagikan ke Cerita" antara 1 hingga 3 detik
        time.sleep(random.uniform(1, 3))

        # Klik tombol "Bagikan ke Cerita"
        share_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Bagikan ke Cerita')]")
        share_button.click()
        
        print("Cerita telah diposting: ", status)
    except Exception as e:
        print("Gagal memposting cerita atau terjadi kesalahan:", str(e))


if __name__ == "__main__":
    akun = [
        # ("mediaku@fifi.luth.my.id", "Baru123*#"),
        # ("uwjatofyatzftd@northsixty.com", "Baru123*#"),
        # ("putri@strapi.luth.my.id", "Baru123*#"),
        # ("nipoqafe.upamiban@labworld.org", "Baru123*#"),
        # ("sabilalala159@gmail.com","@12345678"),
        # ("kamengpanggang@gmail.com","Bireuen12"),
        # ("usahadagang316@gmail.com","Bireuen12"),
        # ("ahrd3043@gmail.com","Bireuen12"),
        # ("mamanoraaaa12@gmail.com","Bireuen12"),
        # ("mamabayuuuu12@gmail.com","Bireuen12"),
        # ("hantulauttt12@gmail.com","Bireuen12"),
        # ("hantumatahari722@gmail.com","Bireuen12"),
        # ("hantubulan3@gmail.com.","Bireuen12"),
        # ("rumahhantu180@gmail.com","Bireuen12"),
        # ("mamaliaaaa12@gmail.com","Bireuen12"),
        # ("kamengbulut6@gmail.com","Bireuen12"),
        # ("Cazorlas386@gmail.com","Bireuen12"),
        # ("nisac4987@gmail.com","Bireuen12"),
        # ("kamenghanco@gmail.com","Bireuen12"),
        # ("kamengapui@gmail.com","Bireuen12"),
        # ("fitriwahyunibir11@gmail.com","Bireuen12"),
        # ("kopidarat875@gmail.com","Bireuen12"),
        # ("riskiamoy06@gmail.com","@12345678"),
        # ("kucingmanisku187@gmail.com","Bireuen12"),
        # ("catatanselebritis@gmail.com","Bireuen12"),
        # ("mitagunawan201@gmail.com","Bireuen12"),
        # ("apismaulana1999@gmail.com","Bireuen12"),
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
        ("nuddinb295@gmail.com","Bireuen12"),
        ("birukalung4@gmail.com","Bireuen12"),
        ("burungm708@gmail.com","Bireuen12"),
        ("hijaukalung443@gmail.com","Bireuen12"),
        ("Kalungmerah39@gmail.com","Bireuen12"),
        ("Hitamkalung24@gmail.com","Bireuen12"),
        ("untaburung81@gmail.com","Bireuen12"),
        ("bulutkebiri@gmail.com","Bireuen12"),
        ("santunsopanya@gmail.com","Bireuen12"),
        ("ninjaberubah@gmail.com","Bireuen12"),
        ("patahleumo@gmail.com","Bireuen12"),
        ("birukalung4@gmail.com","Bireuen12"),
        ("burungm708@gmail.com","Bireuen12"),
        ("hijaukalung443@gmail.com","Bireuen12"),
        ("Kalungmerah39@gmail.com","Bireuen12"),
        ("Hitamkalung24@gmail.com","Bireuen12"),
        ("untaburung81@gmail.com","Bireuen12"),
        ("bulutkebiri@gmail.com","Bireuen12"),
        ("santunsopanya@gmail.com","Bireuen12"),
        ("ninjaberubah@gmail.com","Bireuen12"),
        ("patahleumo@gmail.com","Bireuen12"),
        ("mlmbintang4@gmail.com","Bireuen12"),
        ("aazwal57@gmail.com","Bireuen12"),
        ("raptorpkb@gmail.com","Bireuen12"),
        # new accont
        ("100094693633039","hendri1196"),
        ("100094690664175","hendri1196"),
        ("100094692822728","hendri1196"),
        ("100094693906921","hendri1196"),
        ("100094691685803","hendri1196"),
        ("100094692822219","hendri1196"),
        ("100094692104343","hendri1196"),
        ("100094686735784","hendri1196"),
        ("100094691263621","hendri1196"),
        ("100094697025615","hendri1196"),
        ("100094695944668","hendri1196"),
        ("100094694562906","hendri1196"),
        ("100094695434758","hendri1196"),
        ("100094694983277","hendri1196"),
        ("100094694323162","hendri1196"),
        ("100094693994497","hendri1196"),
        ("100094695074148","hendri1196"),
        ("100094697144111","hendri1196"),
        ("100094695642880","hendri1196"),
        ("100094693155019","hendri1196"),
        ("100094694387433","hendri1196"),
        ("100094698042888","hendri1196"),
        ("100094694504117","hendri1196"),
        ("100094695163954","hendri1196"),
        ("100094696394895","hendri1196"),
        ("100094694415245","hendri1196"),
        ("100094696364920","hendri1196"),
        ("100094694085249","hendri1196"),
        ("100094691834179","hendri1196"),
        ("100094698255259","hendri1196"),
        ("100094695403357","hendri1196"),
        ("100094697412869","hendri1196"),
        ("100094697234765","hendri1196"),
        ("100094697654988","hendri1196"),
        ("100094698613729","hendri1196"),
        ("100094698763802","hendri1196"),
        ("100094698975142","hendri1196"),
        ("100094698194352","hendri1196"),
        ("100094694414964","hendri1196"),
        ("100094698852904","hendri1196"),
        ("100094696994767","hendri1196"),
        ("100094698702767","hendri1196"),
        ("100094697145058","hendri1196"),
        ("100094697384805","hendri1196"),
        ("100094697413600","hendri1196"),
        ("100094695045173","hendri1196"),
        ("100094694715789","hendri1196"),
        ("100094696724107","hendri1196"),
        ("100094694235846","hendri1196"),
        ("100094699276268","hendri1196")
    ]

    status = [
    "Kehidupan adalah apa yang terjadi saat Anda sibuk membuat rencana lain.",
    "Hidup adalah anugerah, nikmati setiap momen.",
    "Ketika Anda memberi, Anda juga menerima.",
    "Percayalah pada diri sendiri, Anda bisa mengatasi segalanya.",
    "Keberhasilan adalah buah dari kerja keras dan tekad yang kuat.",
    "Berpikirlah positif, dan positif akan mengikuti.",
    "Jangan biarkan hari ini menghalangi impian Anda untuk besok.",
    "Kesabaran adalah kunci kebijaksanaan.",
    "Keberhasilan dimulai dengan langkah pertama.",
    "Kebahagiaan berasal dari dalam, bukan dari luar.",
    "Tantangan adalah peluang untuk tumbuh dan berkembang.",
    "Keberhasilan datang kepada mereka yang gigih.",
    "Hidup adalah seperti sepeda, agar seimbang, Anda harus tetap bergerak.",
    "Setiap hari adalah kesempatan untuk menjadi lebih baik dari kemarin.",
    "Kegagalan adalah pelajaran yang mahal, tapi berharga.",
    "Kehidupan adalah apa yang terjadi saat Anda sibuk membuat rencana lain.",
    "Hidup adalah anugerah, nikmati setiap momen.",
    "Ketika Anda memberi, Anda juga menerima.",
    "Percayalah pada diri sendiri, Anda bisa mengatasi segalanya.",
    "Keberhasilan adalah buah dari kerja keras dan tekad yang kuat.",
    "Berpikirlah positif, dan positif akan mengikuti.",
    "Jangan biarkan hari ini menghalangi impian Anda untuk besok.",
    "Kesabaran adalah kunci kebijaksanaan.",
    "Keberhasilan dimulai dengan langkah pertama.",
    "Kebahagiaan berasal dari dalam, bukan dari luar.",
    "Tantangan adalah peluang untuk tumbuh dan berkembang.",
    "Keberhasilan datang kepada mereka yang gigih.",
    "Hidup adalah seperti sepeda, agar seimbang, Anda harus tetap bergerak.",
    "Setiap hari adalah kesempatan untuk menjadi lebih baik dari kemarin.",
    "Ketika Anda mengubah cara Anda memandang sesuatu, hal itu yang Anda lihat berubah.",
    "Tidak ada jalan pintas menuju tempat yang layak Anda tuju.",
    "Keberhasilan adalah hasil dari persiapan, kerja keras, dan belajar dari kegagalan.",
    "Tindakan adalah kunci ke semua keberhasilan.",
    "Kunci untuk mencapai apa yang Anda inginkan adalah konsistensi.",
    "Ketika Anda merasa seperti menyerah, ingatlah mengapa Anda memulai.",
    "Jangan sia-siakan waktu Anda mencemburui orang lain. Gunakan waktu itu untuk menjadi lebih baik.",
    "Kebahagiaan sejati datang dari dalam diri Anda sendiri.",
    "Orang yang sukses adalah mereka yang tidak pernah menyerah pada impian mereka.",
    "Pikirkan besar, dan tindaklah sesuai dengan impian Anda.",
    "Ketika Anda fokus pada solusi, masalah akan menghilang.",
    "Hidup ini terlalu singkat untuk menyia-nyiakan waktu dengan kebencian.",
    "Yang tidak membunuh Anda membuat Anda lebih kuat.",
    "Setiap langkah mendekatkan Anda pada tujuan Anda.",
    "Jangan takut gagal. Takutlah pada ketidakcobaan.",
    "Bekerja keras adalah kuncinya. Tidak ada pengganti untuk kerja keras.",
    "Setiap kesalahan adalah kesempatan untuk belajar dan tumbuh.",
    "Jika Anda ingin perubahan, Anda harus menjadi perubahan itu sendiri.",
    "Ketika Anda bekerja dengan cinta, hasilnya luar biasa.",
    "Keberhasilan adalah produk dari tekad dan ketekunan.",
    "Hal yang tidak diukur tidak dapat diperbaiki.",
    "Anda adalah arsitek takdir Anda sendiri.",
    "Jika Anda tidak mencoba, Anda tidak akan pernah tahu apa yang mungkin Anda capai.",
    "Kebahagiaan adalah perjalanan, bukan tujuan.",
    "Jangan lepaskan mimpi Anda demi kenyamanan.",
    "Pikiran positif menghasilkan tindakan positif.",
    "Kebahagiaan sejati adalah menghargai apa yang Anda miliki sekarang.",
    "Ketika Anda merasa putus asa, ingatlah mengapa Anda mulai.",
    "Ketika satu pintu tertutup, pintu lain terbuka.",
    "Anda adalah pembuat cerita hidup Anda sendiri.",
    "Ketika Anda memberi, Anda juga menerima.",
    "Kesederhanaan adalah kunci untuk kebahagiaan yang sejati.",
    "Ketika Anda menghargai diri sendiri, Anda mengajarkan orang lain untuk menghargai Anda.",
    "Orang yang sukses tidak menunda-nunda.",
    "Anda tidak bisa mengubah angin, tetapi Anda bisa mengarahkan layar Anda.",
    "Keberhasilan adalah hasil dari konsistensi dan kerja keras.",
    "Hidup adalah seperti buku; untuk menghargainya, Anda harus membacanya satu halaman demi satu.",
    "Percayalah pada kemampuan Anda untuk terus berkembang, bahkan ketika orang lain meragukannya.",
    "Keberhasilan adalah hasil dari rasa percaya diri, persiapan, dan kerja keras yang bertemu.",
    "Keberhasilan adalah berdagang waktu kita saat ini untuk kebebasan di masa depan.",
    "Jika Anda ingin mengubah dunia, mulailah dengan diri Anda sendiri.",
    "Kebijaksanaan sejati adalah memahami bahwa Anda selalu memiliki sesuatu untuk dipelajari.",
    "Keberhasilan adalah kuncinya, tetapi kunci membuka pintu.",
    "Jangan pernah ragu untuk berbicara dalam kebenaran, bahkan jika itu membuat Anda berdiri sendiri.",
    "Kesalahan adalah tiket menuju pengetahuan yang lebih dalam dan pemahaman yang lebih baik.",
    "Keberhasilan adalah kebahagiaan yang kita alami dalam perjalanan menuju tujuan yang paling berharga.",
    "Pikirkan masa depan dengan harapan, bukan khawatir.",
    "Ketika Anda merasa lelah, istirahat, bukan menyerah.",
    "Anda tidak bisa mengendalikan semua hal yang terjadi, tetapi Anda dapat mengendalikan reaksi Anda terhadapnya.",
    "Jangan mencari orang untuk mengisi kekosongan dalam hidup Anda; isi sendiri dengan hal-hal yang Anda cintai.",
    "Hidup adalah tentang membuat pilihan yang membawa kita lebih dekat pada visi dan impian kita.",
    "Kebahagiaan tidak datang dari memiliki banyak hal, tetapi dari menghargai apa yang Anda miliki.",
    "Anda adalah penulis cerita hidup Anda sendiri; pastikan itu adalah yang terbaik yang pernah ada.",
    "Ketika Anda memberi cinta tanpa syarat, Anda akan menerimanya kembali dengan berlipat ganda.",
    "Tidak ada kebahagiaan yang lebih besar daripada melakukan sesuatu untuk orang lain.",
    "Jangan menunggu kesempatan, buatlah sendiri.",
    "Tidak ada yang bisa menghentikan Anda selain diri Anda sendiri.",
    "Keberhasilan adalah kunci untuk memahami nilai kerja keras.",
    "Bekerja keraslah untuk mewujudkan impian Anda, jangan hanya bermimpi tentang pekerjaan itu.",
    "Ketika Anda fokus pada hal-hal positif, hal-hal positif akan mengalir ke dalam hidup Anda.",
    "Berpikir kecil tidak akan membawa Anda jauh; impikan yang besar dan bergeraklah dengan tekad.",
    "Ketika Anda berhenti berharap, Anda berhenti menjadi. Ketika Anda berhenti menjadi, Anda berhenti berkembang.",
    "Pikiran adalah kekuatan paling kuat yang dimiliki manusia; gunakan dengan bijaksana.",
    "Hidup adalah tentang memberikan, mencintai, dan tumbuh bersama.",
    "Ketika Anda merasa kehilangan, ingatlah bahwa setiap akhir adalah awal yang baru.",
    "Kesuksesan adalah sebagai menggali sumur: Anda terus menggali sampai Anda menemukan air.",
    "Hidup adalah perjalanan, bukan destinasi.",
    "Keberhasilan adalah hasil dari ketekunan dan keyakinan pada visi Anda.",
    "Pikirkan tiga kali, lakukan sekali.",
    "Orang bijak belajar lebih banyak dari pertanyaan daripada jawaban.",
    "Anda adalah produk dari pengalaman Anda, tetapi Anda tidak harus menjadi korban dari itu.",
    "Ketika kesempatan datang, itu terlambat jika Anda belum bersiap.",
    "Ketika Anda mencapai puncak gunung, ingatlah Anda belum sampai di langit.",
    "Tidak ada keberhasilan yang bisa menggantikan perdamaian batin.",
    "Jangan terjebak dalam masa lalu; lihatlah ke depan ke masa depan yang cerah.",
    "Keberhasilan adalah pilihan, bukan kebetulan.",
    "Hidup adalah rencana yang belum pernah kita tulis.",
    "Ketika Anda berhenti belajar, Anda berhenti tumbuh.",
    "Ketika Anda membantu orang lain mencapai kesuksesan, Anda juga mencapai kesuksesan.",
    "Impian besar membutuhkan waktu dan kesabaran yang besar.",
    "Ketika Anda memelihara kebiasaan positif, Anda meraih kebahagiaan jangka panjang.",
    "Jangan biarkan rasa takut menghentikan Anda dari mencapai potensi Anda yang sejati.",
    "Anda adalah satu-satunya yang dapat mengubah hidup Anda; mulailah dengan keputusan dan tindakan Anda.",
    "Setiap orang adalah buku yang harus dibaca, tetapi beberapa hanya perlu ditinggalkan terbuka.",
    "Jika Anda ingin mencapai hal besar, berhenti memberi diri Anda alasan untuk tidak melakukannya.",
    "Ketika Anda fokus pada tujuan Anda, hal-hal kecil tidak lagi mengganggu Anda.",
    "Pengorbanan adalah bagian dari perjalanan menuju keberhasilan yang besar.",
    "Keberhasilan adalah kejutan bagi mereka yang menunggu; itu adalah hadiah bagi mereka yang bekerja keras.",
    "Ketika Anda berhenti berharap, Anda mulai menciptakan.",
    "Orang yang mengukur diri mereka sendiri dengan diri orang lain adalah kebijaksanaan yang tak tahu batas.",
    "Kegigihan adalah kunci untuk mengatasi segala rintangan.",
    "Kebijaksanaan adalah mengenal diri Anda sendiri, pahami dunia ini, dan terima nasib Anda dengan damai.",
    "Ketika Anda mencintai apa yang Anda lakukan, Anda tidak pernah merasa bekerja sehari pun dalam hidup Anda.",
    "Keberhasilan dimulai dengan satu langkah kecil.",
    "Ketika Anda berhenti berharap, Anda mulai menciptakan.",
    "Jangan pernah berhenti mencoba.",
    "Pikirkan besar, bergeraklah dengan tekad.",
    "Keberhasilan adalah pilihan, bukan kebetulan.",
    "Ketika Anda merasa putus asa, ingatlah mengapa Anda memulai.",
    "Percayalah pada diri Anda sendiri, Anda bisa mengatasi segalanya.",
    "Kesuksesan adalah hasil dari kerja keras dan tekad yang kuat.",
    "Pikiran positif menghasilkan tindakan positif.",
    "Hidup adalah perjalanan, bukan destinasi.",
    "Kegagalan adalah pelajaran yang mahal, tapi berharga.",
    "Hidup adalah anugerah, nikmati setiap momen.",
    "Keberhasilan adalah kunci untuk memahami nilai kerja keras.",
    "Ketika Anda membantu orang lain mencapai kesuksesan, Anda juga mencapai kesuksesan.",
    "Tidak ada keberhasilan yang bisa menggantikan perdamaian batin.",
    "Keberhasilan adalah kuncinya, tetapi kunci membuka pintu.",
    "Ketika Anda berhenti belajar, Anda berhenti tumbuh.",
    "Jika Anda ingin mencapai hal besar, berhenti memberi diri Anda alasan untuk tidak melakukannya.",
    "Percayalah pada kemampuan Anda untuk terus berkembang.",
    "Ketika Anda fokus pada tujuan Anda, hal-hal kecil tidak lagi mengganggu Anda.",
    "Ketika Anda memelihara kebiasaan positif, Anda meraih kebahagiaan jangka panjang.",
    "Kegagalan adalah pelajaran yang mahal, tapi berharga.",
    "Ketika Anda merasa kehilangan, ingatlah bahwa setiap akhir adalah awal yang baru.",
    "Kesuksesan adalah sebagai menggali sumur: Anda terus menggali sampai Anda menemukan air.",
    "Hidup adalah perjalanan, bukan destinasi.",
    "Keberhasilan adalah hasil dari ketekunan dan keyakinan pada visi Anda.",
    "Pikirkan tiga kali, lakukan sekali.",
    "Orang bijak belajar lebih banyak dari pertanyaan daripada jawaban.",
    "Anda adalah produk dari pengalaman Anda, tetapi Anda tidak harus menjadi korban dari itu.",
    "Ketika kesempatan datang, itu terlambat jika Anda belum bersiap.",
    "Ketika Anda mencapai puncak gunung, ingatlah Anda belum sampai di langit.",
    "Tidak ada keberhasilan yang bisa menggantikan perdamaian batin.",
    "Jangan terjebak dalam masa lalu; lihatlah ke depan ke masa depan yang cerah.",
    "Keberhasilan adalah pilihan, bukan kebetulan.",
    "Hidup adalah rencana yang belum pernah kita tulis.",
    "Ketika Anda berhenti belajar, Anda berhenti tumbuh.",
    "Ketika Anda membantu orang lain mencapai kesuksesan, Anda juga mencapai kesuksesan.",
    "Impian besar membutuhkan waktu dan kesabaran yang besar.",
    "Ketika Anda fokus pada hal-hal positif, hal-hal positif akan mengalir ke dalam hidup Anda.",
    "Berpikir kecil tidak akan membawa Anda jauh; impikan yang besar dan bergeraklah dengan tekad.",
    "Ketika Anda berhenti berharap, Anda mulai menciptakan.",
    "Orang yang mengukur diri mereka sendiri dengan diri orang lain adalah kebijaksanaan yang tak tahu batas.",
    "Kegigihan adalah kunci untuk mengatasi segala rintangan.",
    "Kebijaksanaan adalah mengenal diri Anda sendiri, pahami dunia ini, dan terima nasib Anda dengan damai.",
    "Ketika Anda mencintai apa yang Anda lakukan, Anda tidak pernah merasa bekerja sehari pun dalam hidup Anda."
]


    for i, (username, password) in enumerate(akun):
        driver = login_to_facebook(username, password)

        if driver is not None:
            find_and_add_friends(driver)

            if i < len(status):
                post_story(driver, status[i])

            for post_url in postingan:
                like_facebook_post(driver, post_url)

            # Logout dari akun saat ini
            driver.get("https://www.facebook.com/logout.php")
            driver.quit()

    print("Proses selesai.")

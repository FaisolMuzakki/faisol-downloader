import os
import sys
import yt_dlp
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Menentukan folder penyimpanan ke folder "Download" internal HP
FOLDER_DOWNLOAD = "/sdcard/Download/Faisol_Downloader"

# Membuat folder tersebut jika belum ada
if not os.path.exists(FOLDER_DOWNLOAD):
    os.makedirs(FOLDER_DOWNLOAD)

def bersihkan_layar():
    os.system('clear')

def menu_utama():
    while True:
        bersihkan_layar()
        # Tampilan Header RGB Keren
        print(Fore.CYAN + Style.BRIGHT + "=====================================")
        print(Fore.GREEN + Style.BRIGHT + "       FAISOL VIDEO DOWNLOADER       ")
        print(Fore.CYAN + Style.BRIGHT + "=====================================")
        print(Fore.YELLOW + "1. Download Video (Kualitas Terbaik)")
        print(Fore.YELLOW + "2. Download Audio / Musik MP3")
        print(Fore.RED + "0. Keluar")
        print(Fore.CYAN + "=====================================")
        print(Fore.WHITE + f"Penyimpanan: {FOLDER_DOWNLOAD}")
        print(Fore.CYAN + "=====================================")
        
        pilihan = input(Fore.WHITE + "Pilih menu [0-2]: ")
        
        if pilihan == '1':
            url = input(Fore.WHITE + "\n[*] Masukkan URL/Link Video: ").strip()
            if not url:
                print(Fore.RED + "[-] URL tidak boleh kosong!")
                import time; time.sleep(1.5)
                continue
                
            print(Fore.CYAN + "\n[*] Sedang mengunduh video kualitas terbaik...")
            
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': f'{FOLDER_DOWNLOAD}/%(title)s.%(ext)s',
                'merge_output_format': 'mp4',
                'quiet': False
            }
            
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                print(Fore.GREEN + Style.BRIGHT + "\n[+] VIDEO BERHASIL DI-DOWNLOAD!")
                print(Fore.WHITE + f"Cek di folder internal: Download/Faisol_Downloader")
            except Exception as e:
                print(Fore.RED + Style.BRIGHT + f"\n[-] GAGAL MENDOWNLOAD: {e}")
                
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == '2':
            url = input(Fore.WHITE + "\n[*] Masukkan URL/Link Video: ").strip()
            if not url:
                print(Fore.RED + "[-] URL tidak boleh kosong!")
                import time; time.sleep(1.5)
                continue
                
            print(Fore.CYAN + "\n[*] Sedang mengunduh dan mengonversi ke MP3...")
            
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{FOLDER_DOWNLOAD}/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'quiet': False
            }
            
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                print(Fore.GREEN + Style.BRIGHT + "\n[+] MUSIK MP3 BERHASIL DI-DOWNLOAD!")
                print(Fore.WHITE + f"Cek di folder internal: Download/Faisol_Downloader")
            except Exception as e:
                print(Fore.RED + Style.BRIGHT + f"\n[-] GAGAL MENDOWNLOAD AUDIO: {e}")
                
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == '0':
            print(Fore.RED + "\nTerima kasih telah menggunakan Faisol Downloader!")
            sys.exit()
        else:
            print(Fore.RED + "\nPilihan tidak valid!")
            import time
            time.sleep(1.5)

if __name__ == "__main__":
    menu_utama()


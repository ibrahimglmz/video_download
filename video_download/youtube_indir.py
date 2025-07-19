import subprocess
import json

# Tüm olası çözünürlükler (yüksekten düşüğe)
RESOLUTIONS = ["2160", "1440", "1080", "720", "480", "360", "240", "144"]

def mevcut_cozunurlukler(url):
    """yt-dlp ile mevcut video çözünürlüklerini döndürür."""
    komut = [
        "yt-dlp",
        "-j",
        url
    ]
    try:
        sonuc = subprocess.run(komut, capture_output=True, text=True, check=True)
        info = json.loads(sonuc.stdout)
        mevcutlar = set()
        for f in info.get("formats", []):
            if f.get("vcodec", "none") != "none" and f.get("height"):
                mevcutlar.add(str(f["height"]))
        # Sadece tanımlı çözünürlüklerden olanları sırala
        mevcutlar = [r for r in RESOLUTIONS if r in mevcutlar]
        return mevcutlar
    except Exception as e:
        print(f"Çözünürlükler alınırken hata oluştu: {e}")
        return []

def video_indir(url, res):
    print(f"{res}p çözünürlükte video indiriliyor...")
    komut = [
        "yt-dlp",
        "-f", f"bestvideo[height={res}]+bestaudio/best[height={res}]",
        "-o", f"%(title)s_{res}p.%(ext)s",
        "--merge-output-format", "mp4",
        url
    ]
    try:
        subprocess.run(komut, check=True)
        print(f"{res}p çözünürlükte video indirildi.")
    except subprocess.CalledProcessError:
        print(f"{res}p çözünürlükte video bulunamadı veya indirme başarısız.")

if __name__ == "__main__":
    url = input("YouTube video URL'sini girin: ")
    mevcutlar = mevcut_cozunurlukler(url)
    if not mevcutlar:
        print("Mevcut çözünürlükler alınamadı veya video bulunamadı.")
    else:
        print("İndirilebilecek çözünürlükler:")
        for i, res in enumerate(mevcutlar, 1):
            print(f"{i}. {res}p")
        secim = input("Lütfen bir çözünürlük numarası seçin: ")
        try:
            secilen_index = int(secim) - 1
            if 0 <= secilen_index < len(mevcutlar):
                secilen_res = mevcutlar[secilen_index]
                video_indir(url, secilen_res)
            else:
                print("Geçersiz seçim!")
        except ValueError:
            print("Geçersiz giriş! Lütfen bir sayı girin.") 
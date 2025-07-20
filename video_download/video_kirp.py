import subprocess
import os

def video_kirp(video_dosyasi, baslangic_zamani, bitis_zamani, cikti_dosyasi=None):
    """
    Video dosyasını belirtilen zaman aralığında kırpar.
    
    Args:
        video_dosyasi (str): Kırpılacak video dosyasının yolu
        baslangic_zamani (str): Başlangıç zamanı (HH:MM:SS formatında)
        bitis_zamani (str): Bitiş zamanı (HH:MM:SS formatında)
        cikti_dosyasi (str): Çıktı dosyasının adı (None ise otomatik oluşturulur)
    """
    if not os.path.exists(video_dosyasi):
        print(f"Hata: {video_dosyasi} dosyası bulunamadı!")
        return False
    
    if cikti_dosyasi is None:
        dosya_adi = os.path.splitext(video_dosyasi)[0]
        uzanti = os.path.splitext(video_dosyasi)[1]
        cikti_dosyasi = f"{dosya_adi}_kirpilmis{uzanti}"
    
    # ffmpeg komutu ile video kırpma
    komut = [
        "ffmpeg",
        "-i", video_dosyasi,
        "-ss", baslangic_zamani,
        "-to", bitis_zamani,
        "-c", "copy",  # Yeniden kodlama yapmadan kopyala (hızlı)
        "-avoid_negative_ts", "make_zero",
        cikti_dosyasi
    ]
    
    try:
        print(f"Video kırpılıyor: {baslangic_zamani} - {bitis_zamani}")
        subprocess.run(komut, check=True)
        print(f"Video başarıyla kırpıldı: {cikti_dosyasi}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Video kırpma hatası: {e}")
        return False
    except FileNotFoundError:
        print("Hata: ffmpeg bulunamadı! Lütfen ffmpeg'i yükleyin.")
        return False

def zaman_formatini_kontrol_et(zaman_str):
    """Zaman formatının doğru olup olmadığını kontrol eder."""
    try:
        parcalar = zaman_str.split(':')
        if len(parcalar) != 3:
            return False
        saat, dakika, saniye = map(int, parcalar)
        return 0 <= saat <= 23 and 0 <= dakika <= 59 and 0 <= saniye <= 59
    except ValueError:
        return False

if __name__ == "__main__":
    print("=== Video Kırpma Aracı ===")
    
    # Video dosyasını al
    video_dosyasi = input("Video dosyasının yolunu girin: ").strip()
    
    # Zaman aralıklarını al
    print("\nZaman formatı: HH:MM:SS (örnek: 00:01:30)")
    baslangic = input("Başlangıç zamanını girin: ").strip()
    bitis = input("Bitiş zamanını girin: ").strip()
    
    # Zaman formatını kontrol et
    if not zaman_formatini_kontrol_et(baslangic) or not zaman_formatini_kontrol_et(bitis):
        print("Hata: Geçersiz zaman formatı! Lütfen HH:MM:SS formatında girin.")
    else:
        # Çıktı dosyası adını al (opsiyonel)
        cikti_adi = input("Çıktı dosyası adı (boş bırakırsan otomatik oluşturulur): ").strip()
        if not cikti_adi:
            cikti_adi = None
        
        # Video kırpma işlemini başlat
        video_kirp(video_dosyasi, baslangic, bitis, cikti_adi) 
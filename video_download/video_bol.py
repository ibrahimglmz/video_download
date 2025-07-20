import subprocess
import os

def video_bol(video_dosyasi, bolme_saniyesi=27):
    """
    Video dosyasını belirtilen saniyede ikiye böler.
    
    Args:
        video_dosyasi (str): Bölünecek video dosyasının yolu
        bolme_saniyesi (int): Hangi saniyede bölüneceği
    """
    if not os.path.exists(video_dosyasi):
        print(f"Hata: {video_dosyasi} dosyası bulunamadı!")
        return False
    
    # Dosya adı ve uzantısını ayır
    dosya_adi = os.path.splitext(video_dosyasi)[0]
    uzanti = os.path.splitext(video_dosyasi)[1]
    
    # İlk parça: 0. saniyeden bolme_saniyesi'ne kadar
    ilk_parca = f"{dosya_adi}_parca1{uzanti}"
    # İkinci parça: bolme_saniyesi'nden sonuna kadar
    ikinci_parca = f"{dosya_adi}_parca2{uzanti}"
    
    try:
        print(f"Video {bolme_saniyesi}. saniyede bölünüyor...")
        
        # İlk parçayı oluştur (0'dan bolme_saniyesi'ne kadar)
        komut1 = [
            "ffmpeg",
            "-i", video_dosyasi,
            "-t", str(bolme_saniyesi),  # Süre sınırı
            "-c", "copy",  # Yeniden kodlama yapmadan kopyala
            ilk_parca
        ]
        
        print("İlk parça oluşturuluyor...")
        subprocess.run(komut1, check=True)
        print(f"İlk parça oluşturuldu: {ilk_parca}")
        
        # İkinci parçayı oluştur (bolme_saniyesi'nden sonuna kadar)
        komut2 = [
            "ffmpeg",
            "-i", video_dosyasi,
            "-ss", str(bolme_saniyesi),  # Başlangıç noktası
            "-c", "copy",  # Yeniden kodlama yapmadan kopyala
            ikinci_parca
        ]
        
        print("İkinci parça oluşturuluyor...")
        subprocess.run(komut2, check=True)
        print(f"İkinci parça oluşturuldu: {ikinci_parca}")
        
        print(f"\nVideo başarıyla {bolme_saniyesi}. saniyede bölündü!")
        print(f"Parça 1: {ilk_parca}")
        print(f"Parça 2: {ikinci_parca}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Video bölme hatası: {e}")
        return False
    except FileNotFoundError:
        print("Hata: ffmpeg bulunamadı! Lütfen ffmpeg'i yükleyin.")
        return False

if __name__ == "__main__":
    print("=== Video Bölme Aracı ===")
    
    # Video dosyasını al
    video_dosyasi = input("Video dosyasının yolunu girin: ").strip()
    
    # Bölme saniyesini al (varsayılan 27)
    bolme_saniyesi_input = input("Hangi saniyede bölünsün? (varsayılan: 27): ").strip()
    
    if bolme_saniyesi_input:
        try:
            bolme_saniyesi = int(bolme_saniyesi_input)
        except ValueError:
            print("Geçersiz saniye! Varsayılan değer (27) kullanılacak.")
            bolme_saniyesi = 27
    else:
        bolme_saniyesi = 27
    
    # Video bölme işlemini başlat
    video_bol(video_dosyasi, bolme_saniyesi) 
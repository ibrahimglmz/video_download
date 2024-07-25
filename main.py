import yt_dlp
from pytube import YouTube


#TODO  (ses dosyası) , (video görüntü) , ve (video + ses dosyası ) üretmektedir

def video_indir_yt_dlp(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # En iyi video ve ses akışını seçer
        'outtmpl': 'indirilen_video.%(ext)s',  # İndirilen dosyanın adı
        'merge_output_format': 'webm',  # Video ve ses birleştirme formatı olarak webm ayarlar
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'webm',  # Final formatı webm olarak ayarlar
        }],
        'postprocessor_args': ['-c:v', 'libvpx-vp9', '-c:a', 'libopus'],  # Video ve sesi webm formatında birleştirmek için
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video başarıyla indirildi ve WebM formatında dönüştürüldü!")
    except yt_dlp.utils.DownloadError as e:
        print(f"İndirme hatası: {e}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def video_bilgi_goster():
    link_al = YouTube(input('Lütfen YouTube Linkini Giriniz: '))
    print("*"*20)
    print('Video İsmi:', link_al.title)
    print('Video Sahibi:', link_al.author)
    print('Video İzlenme Sayısı:', link_al.views)
    print('Video Açıklama:', link_al.description)
    print('Video Uzunluğu:', link_al.length, 'Saniye')
    print("*"*20)

def main():
    print("Youtube Video Bilgi Alma Uygulamasına Hoşgeldiniz")
    print("*****************************************")

    while True:
        print("Lütfen Seçim Yapınız:")
        print("1- Video Bilgilerini Göster")
        print("2- Videoyu İndir (Hem ses hem görüntü)")

        secim_yap = input("Ne yapmak istersiniz? (1/2): ")

        if secim_yap == "1":
            video_bilgi_goster()
        elif secim_yap == "2":
            video_url = input("YouTube video URL'sini girin: ")
            video_indir_yt_dlp(video_url)
        else:
            print("Geçersiz seçenek! Lütfen geçerli bir seçenek giriniz.")
            continue

        devam = input("Başka bir işlem yapmak ister misiniz? (EVET/HAYIR): ").strip().lower()
        if devam != 'e':
            break

if __name__ == "__main__":
    main()

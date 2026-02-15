import segno

# Bilgileri vCard standartlarına göre hazırlıyoruz
# \r\n (satır başı) karakterleri hayati önem taşır, aman dikkat!
vcard_icerik = (
    "BEGIN:VCARD\r\n"
    "VERSION:3.0\r\n"
    "FN:Atakan (Ati)\r\n"  # Görünen tam ad
    "N:Atakan;;\r\n"       # Soyad;Ad sıralaması
    "ORG:AIT-Sys BT Danışmanlık\r\n"
    "TITLE:Firma Sahibi / BT Danışmanı\r\n"
    "TEL;TYPE=WORK,VOICE:+90542XXXXXXX\r\n"
    "EMAIL:info@ait-sys.com\r\n"
    # Adres formatı: PostaKutusu;DaireNo;Sokak;Şehir;İlçe;PostaKodu;Ülke
    "ADR;TYPE=WORK,POSTAL:;;İstiklal Cad. No:123;Sakarya;Erenler;54100;Türkiye\r\n"
    "URL:https://www.ait-sys.com\r\n"
    "END:VCARD"
)

# QR kodu oluşturuyoruz
# Error 'h' (High) yapalım ki üzerine küçük bir logo koysan bile okunsun
qr = segno.make(vcard_icerik, error='h')

# Kaydedelim gari
qr.save("atakan_vcard.png", scale=10, dark="black", light="white")

print("Statik QR kodun hazır! Okutanın rehberine pat diye düşersin.")

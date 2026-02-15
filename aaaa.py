import segno

# Senin verdiğin güncel bilgilerle vCard içeriği
vcard_icerik = (
    "BEGIN:VCARD\r\n"
    "VERSION:3.0\r\n"
    "FN:Atakan ALAY\r\n"
    "N:ALAY;Atakan;;\r\n"
    "ORG:AIT-Sys\r\n"
    "TITLE:İş Geliştirme Direktörü\r\n"
    "TEL;TYPE=WORK,VOICE:+905441324832\r\n"
    "EMAIL:info@ait-sys.com\r\n"
    "ADR;TYPE=WORK,POSTAL:;;Karaağaç Mahallesi 1842 Sokak No:7;Isparta;Merkez;32300;Türkiye\r\n"
    "URL:https://www.ait-sys.com\r\n"
    "END:VCARD"
)

# QR kodu oluşturuyoruz
# Hata düzeltme (error) 'h' yani High seviyesinde, 
# böylece kodun üzerine ufak bir leke gelse bile okunur.
qr = segno.make(vcard_icerik, error='h')

# Dosyayı siyah üzerine beyaz (klasik) kaydedelim
qr.save(r"C:\Users\Atakan\Desktop\atakan_vcard_guncel.png", scale=10, dark="black", light="white")

print("Tamamdır Atakan, gıcır gıcır QR kodun 'atakan_vcard_guncel.png' adıyla hazırlandı!")

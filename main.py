try:
    with open("server.log","r") as f:
        pass
except FileNotFoundError:
    print("'server.log' dosyasi bulunamadi! Otomatik demo veriler oluşturuluyor...")
    try:
        with open("server.log", "w") as f:
            demo_veri = (
                "192.168.1.10 - 2026-10-08 14:30:15 - INFO - Sunucu basariyla baslatildi.\n"
                "192.168.1.50 - 2026-10-08 14:31:00 - FAILED_LOGIN - Hatali sifre denemesi (Kullanici: admin)\n"
                "192.168.1.50 - 2026-10-08 14:31:05 - FAILED_LOGIN - Hatali sifre denemesi (Kullanici: admin)\n"
                "192.168.1.50 - 2026-10-08 14:31:10 - FAILED_LOGIN - Hatali sifre denemesi (Kullanici: admin)\n"
                "192.168.1.50 - 2026-10-08 14:31:15 - FAILED_LOGIN - Hatali sifre denemesi (Kullanici: admin)\n"
                "10.0.0.45 - 2026-10-08 14:35:22 - WARNING - Yuksek bellek kullanimi tespit edildi.\n"
                "172.16.0.8 - 2026-10-08 14:40:10 - ERROR - Veritabani baglanti zamanasimina ugradi.\n"
                "192.168.1.22 - 2026-10-08 14:42:01 - FAILED_LOGIN - Hatali sifre denemesi (Kullanici: root)\n"
                "10.0.0.99 - 2026-10-08 14:45:00 - CRITICAL - Sistem coktu, acil mudahale gerekli!\n"
                "172.16.0.8 - 2026-10-08 14:48:30 - ERROR - Disk dolulugu %95 seviyesine ulasti.\n"
            )
            f.write(demo_veri)
    except (OSError, PermissionError) as e:
        print(f"HATA: Demo dosya oluşturulamadi veya yazilamadi! Detay: {e}")
loglar = []
try:
    with open("server.log","r", encoding="utf-8") as f:
        for satir in f:
            parcalar = satir.strip().split(" - ")
            if len(parcalar) >= 3:
                loglar.append(parcalar)
except FileNotFoundError:
    print("'server.log' dosyasi bulunamadi!")
hata_sayilari = {
    "ERROR" : 0,
    "CRITICAL" : 0,
    "WARNING" : 0,
    "FAILED_LOGIN" : 0
}
basarisiz_girisler = {}
for parcalar in loglar:
        seviye = parcalar[2]
        if seviye in hata_sayilari:
            hata_sayilari[seviye] += 1
        if parcalar[2] == "FAILED_LOGIN":
            ip_adresi = parcalar[0]
            if ip_adresi in basarisiz_girisler:
                basarisiz_girisler[ip_adresi] += 1
            else:
                basarisiz_girisler[ip_adresi] = 1
print("=====   GÜVENLİK VE LOG RAPORU   =====")
print(f"toplam okunan satir sayisi: {len(loglar)}")
print(f"Yaklanan hata sayisi: {sum(hata_sayilari.values())}")
for ip, adet in basarisiz_girisler.items():
    if adet >= 3:
        print(f"IP: {ip} ({adet} Hatali Giriş)")
        
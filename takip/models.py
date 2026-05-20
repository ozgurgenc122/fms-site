from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from decimal import Decimal
from math import ceil


class Is(models.Model):
    DURUM_SECENEKLERI = [
        ("Teklif", "Teklif"),
        ("Planlandı", "Planlandı"),
        ("Yüklemede", "Yüklemede"),
        ("Yüklendi", "Yüklendi"),
        ("Yolda", "Yolda"),
        ("Limanda", "Limanda"),
        ("Boşaltmada", "Boşaltmada"),
        ("Tamamlandı", "Tamamlandı"),
        ("İptal", "İptal"),
    ]

    ODEME_DURUMU_SECENEKLERI = [
        ("Ödenmedi", "Ödenmedi"),
        ("Kısmi Ödeme", "Kısmi Ödeme"),
        ("Ödendi", "Ödendi"),
    ]

    EVET_HAYIR = [
        ("Hayır", "Hayır"),
        ("Evet", "Evet"),
    ]

    ARAC_TIPLERI = [
        ("Tenteli", "Tenteli"),
        ("Mega", "Mega"),
        ("Sal Kasa", "Sal Kasa"),
        ("Lowbed", "Lowbed"),
        ("Frigo", "Frigo"),
        ("Minivan", "Minivan"),
        ("Lorry", "Lorry"),
        ("Parsiyel", "Parsiyel"),
        ("20DC", "20DC"),
        ("40DC", "40DC"),
        ("Hava Kargo", "Hava Kargo"),
        ("Gemiye Dökme", "Gemiye Dökme"),
    ]

    UCRETSIZ_SAAT_SECENEKLERI = [
        (24, "24 Saat"),
        (48, "48 Saat"),
        (72, "72 Saat"),
    ]

    BEKLEME_UCRETI_SECENEKLERI = [
        ("100 USD", "100 USD"),
        ("150 USD", "150 USD"),
        ("200 USD", "200 USD"),
        ("250 USD", "250 USD"),
        ("300 USD", "300 USD"),
        ("100 EUR", "100 EUR"),
        ("150 EUR", "150 EUR"),
        ("200 EUR", "200 EUR"),
        ("250 EUR", "250 EUR"),
        ("300 EUR", "300 EUR"),
        ("Diğer", "Diğer"),
    ]

    PARA_BIRIMI_SECENEKLERI = [
        ("USD", "USD"),
        ("EUR", "EUR"),
        ("TRY", "TRY"),
    ]

    sira_no = models.IntegerField(default=0)
    is_kodu = models.CharField(max_length=30, blank=True, null=True, unique=True)
    risk_durumu = models.CharField(max_length=20, blank=True)
    risk_notu = models.TextField(blank=True)

    sofor_notu = models.TextField(blank=True)
    nakliyeci_notu = models.TextField(blank=True)

    musteri_adi = models.CharField(max_length=200, blank=True)
    isin_adi = models.CharField(max_length=200, blank=True)
    durum = models.CharField(max_length=50, choices=DURUM_SECENEKLERI, default="Teklif")
    odeme_durumu = models.CharField(max_length=50, choices=ODEME_DURUMU_SECENEKLERI, default="Ödenmedi")
    hat = models.CharField(max_length=100, blank=True)
    para_birimi = models.CharField(max_length=10, choices=PARA_BIRIMI_SECENEKLERI, default="EUR")

    derece_min = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    derece_max = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    arac_tipi = models.CharField(max_length=50, choices=ARAC_TIPLERI, blank=True)
    plaka = models.CharField(max_length=100, blank=True)
    sofor_adi = models.CharField(max_length=100, blank=True)
    sofor_no = models.CharField(max_length=100, blank=True)
    nakliyeci = models.CharField(max_length=200, blank=True)
    guncel_konum = models.CharField(max_length=300, blank=True)

    planlanan_yukleme_zamani = models.DateTimeField(null=True, blank=True)
    gerceklesen_yukleme_zamani = models.DateTimeField(null=True, blank=True)
    yukleme_ucretsiz_saat = models.IntegerField(choices=UCRETSIZ_SAAT_SECENEKLERI, default=24)
    yukleme_bekleme_ucreti = models.CharField(max_length=20, choices=BEKLEME_UCRETI_SECENEKLERI, default="100 USD")
    yukleme_bekleme_diger_tutar = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    yukleme_konum = models.CharField(max_length=300, blank=True)
    bosaltma_konum = models.CharField(max_length=300, blank=True)

    bosaltma_evrak_teslim_zamani = models.DateTimeField(null=True, blank=True)
    bosaltma_zamani = models.DateTimeField(null=True, blank=True)
    bosaltma_ucretsiz_saat = models.IntegerField(choices=UCRETSIZ_SAAT_SECENEKLERI, default=24)
    bosaltma_bekleme_ucreti = models.CharField(max_length=20, choices=BEKLEME_UCRETI_SECENEKLERI, default="100 USD")
    bosaltma_bekleme_diger_tutar = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    tasima1_gelen_fatura = models.CharField(max_length=150, blank=True)
    tasima1_gelen_fatura_tutari = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tasima1_elden_verilen_avans = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tasima1_yapilan_odeme = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    ikinci_tasima_var_mi = models.CharField(max_length=10, choices=EVET_HAYIR, default="Hayır")
    ikinci_arac_tipi = models.CharField(max_length=50, choices=ARAC_TIPLERI, blank=True)
    ikinci_plaka = models.CharField(max_length=100, blank=True)
    ikinci_sofor_adi = models.CharField(max_length=100, blank=True)
    ikinci_sofor_no = models.CharField(max_length=100, blank=True)
    ikinci_nakliyeci = models.CharField(max_length=200, blank=True)
    ikinci_guncel_konum = models.CharField(max_length=300, blank=True)

    ikinci_planlanan_yukleme_zamani = models.DateTimeField(null=True, blank=True)
    ikinci_gerceklesen_yukleme_zamani = models.DateTimeField(null=True, blank=True)
    ikinci_yukleme_ucretsiz_saat = models.IntegerField(choices=UCRETSIZ_SAAT_SECENEKLERI, default=24)
    ikinci_yukleme_bekleme_ucreti = models.CharField(max_length=20, choices=BEKLEME_UCRETI_SECENEKLERI, default="100 USD")
    ikinci_yukleme_bekleme_diger_tutar = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    ikinci_yukleme_konum = models.CharField(max_length=300, blank=True)
    ikinci_bosaltma_konum = models.CharField(max_length=300, blank=True)

    ikinci_bosaltma_evrak_teslim_zamani = models.DateTimeField(null=True, blank=True)
    ikinci_bosaltma_zamani = models.DateTimeField(null=True, blank=True)
    ikinci_bosaltma_ucretsiz_saat = models.IntegerField(choices=UCRETSIZ_SAAT_SECENEKLERI, default=24)
    ikinci_bosaltma_bekleme_ucreti = models.CharField(max_length=20, choices=BEKLEME_UCRETI_SECENEKLERI, default="100 USD")
    ikinci_bosaltma_bekleme_diger_tutar = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    tasima2_gelen_fatura = models.CharField(max_length=150, blank=True)
    tasima2_gelen_fatura_tutari = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tasima2_elden_verilen_avans = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tasima2_yapilan_odeme = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    gemi_adi = models.CharField(max_length=150, blank=True)
    gemi_kalkis_tarihi = models.DateTimeField(null=True, blank=True)
    gemi_yanasma_tarihi = models.DateTimeField(null=True, blank=True)
    limandan_cikis_tarihi = models.DateTimeField(null=True, blank=True)

    liman_ucretsiz_saat = models.IntegerField(choices=UCRETSIZ_SAAT_SECENEKLERI, default=24)
    liman_bekleme_ucreti = models.CharField(max_length=20, choices=BEKLEME_UCRETI_SECENEKLERI, default="100 USD")
    liman_bekleme_diger_tutar = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    elektronka_bedeli = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    liman_masrafi = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    aktarma_masrafi = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    dozvola_masrafi = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    gelen_fatura_numarasi = models.CharField(max_length=150, blank=True)
    gelen_fatura_tutari = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    esya_cinsi = models.CharField(max_length=250, blank=True)
    kap = models.CharField(max_length=100, blank=True)
    kg = models.CharField(max_length=100, blank=True)
    gtip = models.CharField(max_length=100, blank=True)

    fatura_tutari = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    hesaplanan_teminat = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fatura_edilecek_teminat_tutari = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    teminat_satisa_dahil_mi = models.CharField(max_length=10, choices=EVET_HAYIR, default="Evet")
    teminat_ayri_fatura_no = models.CharField(max_length=150, blank=True)

    satis_faturasi = models.CharField(max_length=150, blank=True)
    satis_faturasi_tutari = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    gelen_gemi_faturasi = models.CharField(max_length=150, blank=True)
    gemi_faturasi_tutari = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    yukleme_evraklari = models.FileField(upload_to="evraklar/yukleme/", null=True, blank=True)
    gumruk_evraklari = models.FileField(upload_to="evraklar/gumruk/", null=True, blank=True)
    yurtdisi_evraklari = models.FileField(upload_to="evraklar/yurtdisi/", null=True, blank=True)
    bosaltma_evraklari = models.FileField(upload_to="evraklar/bosaltma/", null=True, blank=True)

    notlar = models.TextField(blank=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    def ucret_rakam(self, secim, diger):
        if secim == "Diğer":
            return Decimal(diger or 0)
        try:
            return Decimal(str(secim).split()[0])
        except Exception:
            return Decimal("0")

    def saat_farki(self, baslangic, bitis):
        if not baslangic or not bitis:
            return 0
        fark = bitis - baslangic
        return max(fark.total_seconds() / 3600, 0)

    def bekleme_gunu(self, baslangic, bitis, ucretsiz_saat):
        saat = self.saat_farki(baslangic, bitis)
        bekleme_saat = max(saat - int(ucretsiz_saat or 0), 0)
        if bekleme_saat <= 0:
            return 0
        return ceil(bekleme_saat / 24)

    def yukleme_bekleme_gunu(self):
        return self.bekleme_gunu(self.planlanan_yukleme_zamani, self.gerceklesen_yukleme_zamani, self.yukleme_ucretsiz_saat)

    def yukleme_bekleme_tutari(self):
        return Decimal(self.yukleme_bekleme_gunu()) * self.ucret_rakam(self.yukleme_bekleme_ucreti, self.yukleme_bekleme_diger_tutar)

    def bosaltma_bekleme_gunu(self):
        return self.bekleme_gunu(self.bosaltma_evrak_teslim_zamani, self.bosaltma_zamani, self.bosaltma_ucretsiz_saat)

    def bosaltma_bekleme_tutari(self):
        return Decimal(self.bosaltma_bekleme_gunu()) * self.ucret_rakam(self.bosaltma_bekleme_ucreti, self.bosaltma_bekleme_diger_tutar)

    def ikinci_yukleme_bekleme_gunu(self):
        return self.bekleme_gunu(self.ikinci_planlanan_yukleme_zamani, self.ikinci_gerceklesen_yukleme_zamani, self.ikinci_yukleme_ucretsiz_saat)

    def ikinci_yukleme_bekleme_tutari(self):
        return Decimal(self.ikinci_yukleme_bekleme_gunu()) * self.ucret_rakam(self.ikinci_yukleme_bekleme_ucreti, self.ikinci_yukleme_bekleme_diger_tutar)

    def ikinci_bosaltma_bekleme_gunu(self):
        return self.bekleme_gunu(self.ikinci_bosaltma_evrak_teslim_zamani, self.ikinci_bosaltma_zamani, self.ikinci_bosaltma_ucretsiz_saat)

    def ikinci_bosaltma_bekleme_tutari(self):
        return Decimal(self.ikinci_bosaltma_bekleme_gunu()) * self.ucret_rakam(self.ikinci_bosaltma_bekleme_ucreti, self.ikinci_bosaltma_bekleme_diger_tutar)

    def liman_bekleme_gunu(self):
        return self.bekleme_gunu(self.gemi_yanasma_tarihi, self.limandan_cikis_tarihi, self.liman_ucretsiz_saat)

    def liman_bekleme_tutari(self):
        return Decimal(self.liman_bekleme_gunu()) * self.ucret_rakam(self.liman_bekleme_ucreti, self.liman_bekleme_diger_tutar)

    def toplam_bekleme_tutari(self):
        return (
            self.yukleme_bekleme_tutari()
            + self.bosaltma_bekleme_tutari()
            + self.ikinci_yukleme_bekleme_tutari()
            + self.ikinci_bosaltma_bekleme_tutari()
            + self.liman_bekleme_tutari()
        )

    def toplam_maliyet(self):
        return (
            self.toplam_bekleme_tutari()
            + self.elektronka_bedeli
            + self.liman_masrafi
            + self.aktarma_masrafi
            + self.dozvola_masrafi
            + self.tasima1_gelen_fatura_tutari
            + self.tasima2_gelen_fatura_tutari
            + self.gelen_fatura_tutari
            + self.gemi_faturasi_tutari
        )

    def toplam_satis(self):
        return (
            self.satis_faturasi_tutari
            + self.fatura_edilecek_teminat_tutari
    )

    def net_kar(self):
        return self.toplam_satis() - self.toplam_maliyet()

    def tasima1_kalan_odeme(self):
        return self.tasima1_gelen_fatura_tutari - self.tasima1_elden_verilen_avans - self.tasima1_yapilan_odeme

    def tasima2_kalan_odeme(self):
        return self.tasima2_gelen_fatura_tutari - self.tasima2_elden_verilen_avans - self.tasima2_yapilan_odeme

    def risk_sayisi(self):
        sorgu = Q()

        if self.nakliyeci:
            sorgu |= Q(firma_adi__icontains=self.nakliyeci)
        if self.sofor_adi:
            sorgu |= Q(sofor_adi__icontains=self.sofor_adi)
        if self.plaka:
            sorgu |= Q(plaka__icontains=self.plaka)
        if self.ikinci_nakliyeci:
            sorgu |= Q(firma_adi__icontains=self.ikinci_nakliyeci)
        if self.ikinci_sofor_adi:
            sorgu |= Q(sofor_adi__icontains=self.ikinci_sofor_adi)
        if self.ikinci_plaka:
            sorgu |= Q(plaka__icontains=self.ikinci_plaka)

        if not sorgu:
            return 0

        return RiskKaydi.objects.filter(sorgu).count()

    def risk_seviyesi(self):
        sayi = self.risk_sayisi()

        if sayi >= 3:
            return "RISKLI"

        if sayi > 0:
            return "DIKKAT"

        if self.risk_notu or self.sofor_notu or self.nakliyeci_notu:
            return "DIKKAT"

        return ""

    @property
    def risk_durumu_goster(self):
        return self.risk_seviyesi()

    def toplam_tasima_gunu(self):
        baslangic = self.gerceklesen_yukleme_zamani or self.planlanan_yukleme_zamani

        if self.ikinci_tasima_var_mi == "Evet":
            bitis = self.ikinci_bosaltma_zamani
        else:
            bitis = self.bosaltma_zamani

        if not baslangic or not bitis:
            return 0

        fark = bitis - baslangic
        gun = fark.days

        if fark.seconds > 0:
            gun += 1

        return max(gun, 0)

    def eksik_evrak_sayisi(self):
        sayi = 0
        if not self.yukleme_evraklari:
            sayi += 1
        if not self.gumruk_evraklari:
            sayi += 1
        if not self.yurtdisi_evraklari:
            sayi += 1
        if not self.bosaltma_evraklari:
            sayi += 1
        return sayi

    def evrak_durumu(self):
        if self.eksik_evrak_sayisi() == 0:
            return "Tamam"
        return f"{self.eksik_evrak_sayisi()} evrak eksik"

    def __str__(self):
        kod = self.is_kodu or f"SIRA-{self.sira_no}"
        return f"{kod} - {self.musteri_adi} - {self.isin_adi}"


class RiskKaydi(models.Model):
    SORUN_TIPLERI = [
        ("Gecikme", "Gecikme"),
        ("Evrak Sorunu", "Evrak Sorunu"),
        ("Hasar", "Hasar"),
        ("İletişim Kötü", "İletişim Kötü"),
        ("Ödeme Sorunu", "Ödeme Sorunu"),
        ("Sahte Bilgi", "Sahte Bilgi"),
        ("Diğer", "Diğer"),
    ]

    firma_adi = models.CharField(max_length=200, blank=True)
    sofor_adi = models.CharField(max_length=200, blank=True)
    plaka = models.CharField(max_length=100, blank=True)
    sorun_tipi = models.CharField(max_length=50, choices=SORUN_TIPLERI, default="Diğer")
    aciklama = models.TextField(blank=True)
    tarih = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.firma_adi} - {self.sofor_adi} - {self.plaka} - {self.sorun_tipi}"

class IsGecmisi(models.Model):
    is_kaydi = models.ForeignKey(Is, on_delete=models.CASCADE, related_name="gecmisler")
    kullanici = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    islem = models.CharField(max_length=100)
    aciklama = models.TextField(blank=True)
    tarih = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-tarih", "-id"]

    def __str__(self):
        return f"{self.is_kaydi} - {self.islem} - {self.tarih}"


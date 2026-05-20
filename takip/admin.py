from django.contrib import admin
from .models import Is, RiskKaydi, IsGecmisi


@admin.register(Is)
class IsAdmin(admin.ModelAdmin):
    list_display = ("is_kodu", "sira_no", "musteri_adi", "isin_adi", "durum", "odeme_durumu", "para_birimi")
    search_fields = ("is_kodu", "musteri_adi", "isin_adi", "plaka", "ikinci_plaka")
    list_filter = ("durum", "odeme_durumu", "para_birimi")


@admin.register(RiskKaydi)
class RiskKaydiAdmin(admin.ModelAdmin):
    list_display = ("firma_adi", "sofor_adi", "plaka", "sorun_tipi", "tarih")
    search_fields = ("firma_adi", "sofor_adi", "plaka")
    list_filter = ("sorun_tipi", "tarih")


@admin.register(IsGecmisi)
class IsGecmisiAdmin(admin.ModelAdmin):
    list_display = ("is_kaydi", "kullanici", "islem", "tarih")
    search_fields = ("is_kaydi__is_kodu", "islem", "aciklama")
    list_filter = ("islem", "tarih")

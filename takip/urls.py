from django.urls import path
from . import views

urlpatterns = [
    path("", views.ana_sayfa, name="ana_sayfa"),
    path("ekle/", views.is_ekle, name="is_ekle"),
    path("yedekler/", views.yedek_listesi, name="yedek_listesi"),
    path("yedek-al/", views.yedek_al, name="yedek_al"),
    path("yedek-indir/<str:dosya_adi>/", views.yedek_indir, name="yedek_indir"),
    path("yedek-sil/<str:dosya_adi>/", views.yedek_sil, name="yedek_sil"),
    path("yedek-geri-yukle/", views.yedek_geri_yukle, name="yedek_geri_yukle_yukle"),
    path("yedek-geri-yukle/<str:dosya_adi>/", views.yedek_geri_yukle, name="yedek_geri_yukle"),
    path("duzenle/<int:id>/", views.is_duzenle, name="is_duzenle"),
    path("goster/<int:id>/", views.is_goster, name="is_goster"),
    path("sil/<int:id>/", views.is_sil, name="is_sil"),
    path("kopyala/<int:id>/", views.is_kopyala, name="is_kopyala"),
    path("aktif/<int:id>/", views.aktif_ise_gecir, name="aktif_ise_gecir"),
    path("riskler/", views.risk_listesi, name="risk_listesi"),
    path("cariler/", views.cari_listesi, name="cari_listesi"),
    path("tamamlanan-isler/", views.tamamlanan_isler, name="tamamlanan_isler"),
    path("eksik-evraklar/", views.eksik_evraklar, name="eksik_evraklar"),
    path("risk/ekle/", views.risk_ekle, name="risk_ekle"),
    path("risk/sil/<int:id>/", views.risk_sil, name="risk_sil"),
    path("cikis/", views.guvenli_cikis, name="guvenli_cikis"),

    path("excel/sablon/", views.excel_sablon, name="excel_sablon"),
    path("excel/import/", views.excel_import, name="excel_import"),
    path("excel/musteriler/", views.excel_musteriler, name="excel_musteriler"),
    path("excel/isler/", views.excel_isler, name="excel_isler"),
    path("excel/konumlar/", views.excel_konumlar, name="excel_konumlar"),
]
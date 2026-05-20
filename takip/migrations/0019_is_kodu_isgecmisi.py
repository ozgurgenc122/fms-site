# Generated manually for FMS panel improvements

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def kodlari_doldur(apps, schema_editor):
    Is = apps.get_model("takip", "Is")
    for kayit in Is.objects.all().order_by("id"):
        if not kayit.is_kodu:
            yil = kayit.olusturma_tarihi.year if kayit.olusturma_tarihi else 2026
            kayit.is_kodu = f"FMS-{yil}-{kayit.id:04d}"
            kayit.save(update_fields=["is_kodu"])


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("takip", "0018_is_risk_durumu"),
    ]

    operations = [
        migrations.AddField(
            model_name="is",
            name="is_kodu",
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.RunPython(kodlari_doldur, migrations.RunPython.noop),
        migrations.CreateModel(
            name="IsGecmisi",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("islem", models.CharField(max_length=100)),
                ("aciklama", models.TextField(blank=True)),
                ("tarih", models.DateTimeField(auto_now_add=True)),
                ("is_kaydi", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="gecmisler", to="takip.is")),
                ("kullanici", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-tarih", "-id"]},
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-04 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ArkencoApi", "0008_alter_usuario_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="cliente",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ArkencoApi.usuario",
            ),
        ),
    ]

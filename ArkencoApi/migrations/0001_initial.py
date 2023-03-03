# Generated by Django 4.1.7 on 2023-03-03 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                ("nombre_empresa", models.CharField(max_length=200)),
                (
                    "rut",
                    models.CharField(max_length=12, primary_key=True, serialize=False),
                ),
                ("direccion", models.CharField(max_length=200)),
                ("telefono", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Estado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("Abierto", "Abierto"),
                            ("Perdido", "Perdido"),
                            ("Ganado", "Ganado"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Etapa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "etapa",
                    models.CharField(
                        choices=[
                            ("En conversacion", "En conversacion"),
                            ("Conseguido", "Conseguido"),
                            ("Perdido", "Perdido"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=50, unique=True)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Prospecto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("telefono", models.IntegerField()),
                ("fecha_ingreso", models.DateField()),
                ("sexo", models.CharField(max_length=20)),
                (
                    "cliente_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ArkencoApi.cliente",
                    ),
                ),
                (
                    "estado_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ArkencoApi.estado",
                    ),
                ),
                (
                    "estapa_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ArkencoApi.etapa",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cliente",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ArkencoApi.usuario"
            ),
        ),
    ]

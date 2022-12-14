# Generated by Django 4.0.4 on 2022-09-19 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apparm', '0003_remove_proveedor_seleccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms', models.BooleanField(verbose_name='Tienes esta responsabilidad ')),
                ('user', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('option', models.CharField(choices=[('Me pasó a mi', 'Me pasó a mi'), ('Ya era asi', 'Ya era asi')], max_length=100)),
                ('reason', models.CharField(choices=[('Borrar proveedor', 'Borrar proveedor'), ('Problema del sistema', 'Problema del sistema'), ('Otros', 'Otros')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('situation', models.CharField(choices=[('Done', 'Done'), ('Pending', 'Pending')], default='Pending', max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nota',
            field=models.TextField(blank=True),
        ),
    ]

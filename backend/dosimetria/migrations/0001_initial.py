# Generated by Django 3.1.7 on 2021-02-23 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='organisation_info', to='core.client')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Номер')),
                ('begin', models.DateField(verbose_name='Начало')),
                ('end', models.DateField(verbose_name='Конец')),
            ],
            options={
                'verbose_name': 'Квартал',
                'verbose_name_plural': 'Кварталы',
                'ordering': ['year', 'number'],
                'get_latest_by': ['year', 'number'],
                'unique_together': {('year', 'number')},
            },
        ),
        migrations.CreateModel(
            name='TransmittedDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование')),
                ('is_returned', models.BooleanField(verbose_name='Статус')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transmitted_documents', to='dosimetria.client', verbose_name='Клиент')),
                ('quarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosimetria.quarter', verbose_name='Квартал')),
            ],
            options={
                'verbose_name': 'Переданный документ',
                'verbose_name_plural': 'Переданные документы',
            },
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16, unique=True, verbose_name='Номер')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='protocols', to='dosimetria.client', verbose_name='Клиент')),
                ('quarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosimetria.quarter', verbose_name='Квартал')),
            ],
            options={
                'verbose_name': 'Протокол',
                'verbose_name_plural': 'Протоколы',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16, unique=True, verbose_name='Номер')),
                ('is_returned', models.BooleanField(default=False, verbose_name='Статус')),
                ('total', models.PositiveIntegerField(verbose_name='Сумма')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoices', to='dosimetria.client', verbose_name='Клиент')),
                ('quarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosimetria.quarter', verbose_name='Квартал')),
                ('returned_at', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='returned_invoices', to='dosimetria.quarter', verbose_name='Квартал возврата')),
            ],
            options={
                'verbose_name': 'Счет/акт',
                'verbose_name_plural': 'Счета/акты',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64, null=True)),
                ('patronymic', models.CharField(max_length=64, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='dosimetria.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='ActualAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.PositiveSmallIntegerField()),
                ('region', models.CharField(max_length=64)),
                ('area', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=64)),
                ('building', models.CharField(max_length=16)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actual_addresses', to='dosimetria.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Физический адрес',
                'verbose_name_plural': 'Физические адреса',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('CON', 'Контракт'), ('AGR', 'Договор')], max_length=8, verbose_name='Тип')),
                ('number', models.CharField(max_length=32, verbose_name='Номер')),
                ('begin', models.DateField(verbose_name='Заключен')),
                ('end', models.DateField(verbose_name='Истекает')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contracts', to='dosimetria.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Контракт/договор',
                'verbose_name_plural': 'Контракты/договора',
                'ordering': ['end'],
                'get_latest_by': ['end'],
                'unique_together': {('category', 'number')},
            },
        ),
    ]
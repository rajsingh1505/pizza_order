# Generated by Django 2.0.1 on 2018-01-16 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_auto_20180113_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(choices=[(30, '30cm'), (50, '50cm')], default=30)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_address', models.TextField()),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Pizza')),
            ],
        ),
    ]
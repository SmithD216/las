# Generated by Django 2.0 on 2017-12-28 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('las_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
        migrations.AddField(
            model_name='comment',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='las_site.Entry'),
        ),
    ]
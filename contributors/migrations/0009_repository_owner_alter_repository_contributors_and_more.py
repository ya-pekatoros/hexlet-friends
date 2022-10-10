# Generated by Django 4.0.7 on 2022-09-09 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0008_merge_20220714_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='contributors.contributor', verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='contributors',
            field=models.ManyToManyField(related_name='contributors', through='contributors.Contribution', to='contributors.contributor', verbose_name='contributors'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contributors.organization', verbose_name='organization'),
        ),
    ]

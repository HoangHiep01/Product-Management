# Generated by Django 4.2.3 on 2023-07-28 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(null=True, upload_to='Product/img/'),
        ),
    ]

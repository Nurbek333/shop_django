# Generated by Django 5.0.6 on 2024-06-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0005_remove_product_name_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categoryy',
            field=models.CharField(default=0.0004269854824935952, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

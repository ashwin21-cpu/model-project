# Generated by Django 3.1.7 on 2021-04-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='uploads/products_img/-')),
            ],
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='age',
            field=models.IntegerField(),
        ),
    ]
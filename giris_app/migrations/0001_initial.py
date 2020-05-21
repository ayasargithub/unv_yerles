from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='universite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(max_length=1000)),
                ('sehir', models.CharField(max_length=50)),
                ('ulke', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='universite',
        ),
    ]

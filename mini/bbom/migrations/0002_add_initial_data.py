from django.db import migrations


def add_initial_data(apps, schema_editor):
    Univ = apps.get_model('bbom', 'Univ')
    Summary = apps.get_model('bbom', 'Summary')

    korea = Univ.objects.create(name='Korea')
    Summary.objects.create(name='Bengaluru', univ=korea)
    Summary.objects.create(name='Mumbai', univ=korea)
    Summary.objects.create(name='Chennai', univ=korea)
    Summary.objects.create(name='Hyderabad', univ=korea)
    Summary.objects.create(name='New Delhi', univ=korea)

    yonsei = Univ.objects.create(name='Yonsei')
    Summary.objects.create(name='New York', univ=yonsei)
    Summary.objects.create(name='San Francisco', univ=yonsei)
    Summary.objects.create(name='Los Angeles', univ=yonsei)
    Summary.objects.create(name='Chicago', univ=yonsei)
    Summary.objects.create(name='Seattle', univ=yonsei)


class Migration(migrations.Migration):

    dependencies = [
        ('bbom', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
from django.db import migrations


def add_initial_data(apps, schema_editor):
    Univ = apps.get_model('bbom', 'Univ')
    Summary = apps.get_model('bbom', 'Summary')
    Menu = apps.get_model('bbom', 'Menu')
    Category = apps.get_model('bbom', "Category")

    korea = Univ.objects.create(name='고려대학교')
    Summary.objects.create(name='GS고대역점', univ=korea)
    Summary.objects.create(name='GS안암역점', univ=korea)
    Summary.objects.create(name='CU정대후문', univ=korea)
    Summary.objects.create(name='GS고대정문', univ=korea)

    yonsei = Univ.objects.create(name='연세대학교')
    Summary.objects.create(name='GS신촌역점', univ=yonsei)
    Summary.objects.create(name='CU신촌역점', univ=yonsei)
    Summary.objects.create(name='GS서문', univ=yonsei)
    Summary.objects.create(name='CU서문', univ=yonsei)

    busan = Univ.objects.create(name='부산대학교')
    Summary.objects.create(name='GS부대역점', univ=busan)
    Summary.objects.create(name='GS부대정문', univ=busan)
    Summary.objects.create(name='CU부대역점', univ=busan)
    Summary.objects.create(name='CU부대정문', univ=busan)

    inha = Univ.objects.create(name='인하대학교')
    Summary.objects.create(name='GS인하대정문', univ=inha)
    Summary.objects.create(name='CU인하대정문', univ=inha)
    Summary.objects.create(name='CU인천역점', univ=inha)
    Summary.objects.create(name='GS인천역점', univ=inha)

    Menu.objects.create(name='피자', slug='pizza')
    Menu.objects.create(name='치킨', slug='chicken')
    Menu.objects.create(name='보쌈', slug='bossam')
    Menu.objects.create(name='떡볶이', slug='tteok')
    Menu.objects.create(name='족발', slug='jok')
    Menu.objects.create(name='닭발', slug='dak')
    Menu.objects.create(name='삽겹살', slug='sap')
    Menu.objects.create(name='마라샹궈', slug='mara')
    Menu.objects.create(name='찜닭', slug='jjim')

    Category.objects.create(name='야식', slug='Food')
    Category.objects.create(name='생필품', slug='Nec')
    Category.objects.create(name='식재료', slug='Material')

class Migration(migrations.Migration):

    dependencies = [
        ('bbom', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
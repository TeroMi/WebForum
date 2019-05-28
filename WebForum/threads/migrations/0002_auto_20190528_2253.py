# Generated by Django 2.2.1 on 2019-05-28 19:53

from django.db import migrations

def addCategories(apps, schema_editor):
    Category = apps.get_model('threads', 'Category')
    sports = "Sports"
    tech = "Tech"
    general = "General"
    if Category.objects.filter(Name=sports) or Category.objects.filter(Name=tech) or Category.objects.filter(Name=general):
       print("One of the categories were added already")
    else:
        Category.objects.create(Name=sports)
        Category.objects.create(Name=tech)
        Category.objects.create(Name=general)

class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(addCategories)
    ]

from django.db import migrations
import uuid

def copy_data(apps, schema_editor):
    OldModel = apps.get_model('main', 'Jersey')
    NewModel = apps.get_model('main', 'NewJersey')

    for old_instance in OldModel.objects.all():
        NewModel.objects.create(
            id=uuid.uuid4(),  # Generate a new UUID for the primary key
            name=old_instance.name,
            price=old_instance.price,
            description=old_instance.description,
            image=old_instance.image,
            quantity=old_instance.quantity,
            # Copy other fields as needed
        )

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_newjersey'),  # Replace with your last migration
    ]

    operations = [
        migrations.RunPython(copy_data),
    ]

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def assign_author_to_existing_plugins(apps, schema_editor):
    Plugin = apps.get_model('pages', 'Plugin')
    User = apps.get_model('auth', 'User')
    superuser = User.objects.filter(is_superuser=True).order_by('pk').first()
    if superuser is None:
        superuser = User.objects.order_by('pk').first()
    if superuser is None:
        return
    Plugin.objects.filter(author_id__isnull=True).update(author_id=superuser.pk)


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0003_alter_plugin_options_alter_plugin_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='plugin',
            name='author',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='plugins',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.RunPython(assign_author_to_existing_plugins, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='plugin',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='plugins',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

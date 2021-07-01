# Generated by Django 3.2.4 on 2021-07-01 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_user_friends'),
        ('book', '0004_comment_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='record_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='update_time',
            new_name='updated',
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='books/'),
        ),
        migrations.AddField(
            model_name='book',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='likes', to='user.User'),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='user.user'),
            preserve_default=False,
        ),
    ]

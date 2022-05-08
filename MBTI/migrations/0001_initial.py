# Generated by Django 3.2.9 on 2022-05-08 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mbti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbti_name', models.TextField()),
                ('title', models.TextField()),
                ('mbti_type', models.TextField()),
                ('best_mbti', models.IntegerField(default=0)),
                ('worst_mbti', models.IntegerField(default=0)),
                ('top_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('view_cnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('choice_right', models.TextField()),
                ('choice_left', models.TextField()),
                ('question_category', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Howto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('mbti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='how_to', to='MBTI.mbti')),
            ],
        ),
        migrations.CreateModel(
            name='BaseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('mbti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base_info', to='MBTI.mbti')),
            ],
        ),
        migrations.CreateModel(
            name='AnotherInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('mbti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='another_info', to='MBTI.mbti')),
            ],
        ),
    ]

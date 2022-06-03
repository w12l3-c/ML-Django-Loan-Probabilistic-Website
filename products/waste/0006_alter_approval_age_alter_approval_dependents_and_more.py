# Generated by Django 4.0.2 on 2022-05-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_approval_age_alter_approval_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='approval',
            name='dependents',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='approval',
            name='monthly_debt',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='approval',
            name='monthly_income',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='approval',
            name='ninety_days_late',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='approval',
            name='open_credit_lines_and_loans',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='approval',
            name='real_estate_loans',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='approval',
            name='revolving_utilization',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='approval',
            name='sixty_to_eighty_nine_days_late',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='approval',
            name='thirty_to_fifty_nine_days_late',
            field=models.FloatField(),
        ),
    ]

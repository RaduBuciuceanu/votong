# Generated by Django 2.2.16 on 2020-11-07 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0034_auto_20201104_1207"),
    ]

    operations = [
        migrations.RemoveConstraint(model_name="candidatevote", name="unique_candidate_domain_vote",),
        migrations.AddField(model_name="domain", name="seats", field=models.PositiveSmallIntegerField(default=0),),
    ]

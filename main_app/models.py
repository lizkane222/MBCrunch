from django.db import models

# Create your models here.

BINTYPES = (
    ('WA','waste'),
    ('CA','cardboard'),
    ('EW','e-waste'),
    ('GL','glass'),
    ('ME','metal'),
    ('PA','paper'),
    ('PL','plastic'),
    ('OR','organic'),
)

VERIFYBIN = (
    ('UV','unverified'),
    ('VE','verified'),
    ('AC','accurate bin type'),
    ('IN','inaccurate bin type'),
    ('EX','exists'),
    ('NO','does not exist'),
    ('GO','good condition'),
    ('PO','poor condition'),
)

class Bin(models.Model):
    type = models.CharField(
        max_length = 2,
        choices=BINTYPES,
        default=BINTYPES[0][0]
    )
    location = models.CharField(max_length = 200)
    delivery_date = models.DateField()
    delivery_location = models.CharField(max_length=200)
    verified = models.BooleanField(True == 'accurate bin type', False =='inaccurate bin type')
    gives_rewards = models.IntegerField()
    collection_market = models.TextField(max_length=550)
    sponsor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.get_type_display()} is at {self.location}."


class Investor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    deposits_made = models.IntegerField()
    verifications = models.CharField(
        max_length = 2,
        choices=VERIFYBIN,
        default=VERIFYBIN[0][0]
    )
    current_location = models.CharField(max_length=200)
    identify_new_bin = models.CharField(max_length=200)
    gives_rewards = models.IntegerField()
    community_contributions = models.IntegerField()
    sponsor = models.CharField(max_length=200)

    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: Total Deposits: {self.deposits_made} Community Contribution:{self.community_contribution_points}!  Verified: {self.get_verifications_display} bins!{self.current_location} Sponsoring {self.sponsor} bins. Rewards:{self.gives_rewards}"


class Collection_Market(models.Model):
    name = models.CharField(max_length=200)
    dates = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    assoc_bins = models.Bin
    assoc_investors = models.Investor




# Ways to create data:
# 1. Through forms in the app
# 2. Through the Django/Python shell (python3 manage.py shell)
# 3. Through the psql shell
# 4. Through the admin panel at /admin
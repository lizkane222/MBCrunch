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
    gives_rewards = models.IntegerField(default="0")

    def __str__(self):
        return f"{self.get_type_display()} is at {self.location}."



class Person(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    deposits_made = models.IntegerField(default="0")
    verifications = models.CharField(
        max_length = 2,
        choices=VERIFYBIN,
        default=VERIFYBIN[0][0]
    )
    current_location = models.CharField(max_length=200)
    identify_new_bin = models.CharField(max_length=200)
    rewards = models.IntegerField(default="0")
    community_contributions = models.IntegerField(default="0")


    bins = models.ManyToManyField(Bin)


    def __str__(self):
        return f"{self.name}: Total Deposits: {self.deposits_made} Community Contribution:{self.community_contributions}!  Verified: {self.get_verifications_display()} bins!{self.current_location} Sponsoring {self.bins} bins. Rewards:{self.rewards}"


class Investor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    deposits_made = models.IntegerField(default="0")
    verifications = models.CharField(
        max_length = 2,
        choices=VERIFYBIN,
        default=VERIFYBIN[0][0]
    )
    community_contributions = models.IntegerField(default="0")
    current_location = models.CharField(max_length=200)
    identify_new_bin = models.CharField(max_length=200)
    gives_rewards = models.IntegerField(default="0")

    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: Total Deposits: {self.deposits_made} Community Contribution:{self.community_contributions}!  Verified: {self.get_verifications_display()} bins!{self.current_location} Rewards:{self.gives_rewards}"



class Collection_Market(models.Model):
    name = models.CharField(max_length=200)
    dates = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    location = models.TextField(max_length=250, default="Address:")
    market_description = models.TextField(max_length=300, default="Community Centered Market")

    # many to many relationship with investor
    investors = models.ManyToManyField(Investor)
    # many to many relationship (IMPORT ALL BINS ASSOCIATED WITH INVESTOR)
    # bins = models.ManyToManyField(Investor)


    def __str__(self):
        return f"{self.name}{self.dates}{self.time_start}{self.time_end}{self.investors.name}"

# self.investors.bin.type

# Ways to create data:
# 1. Through forms in the app
# 2. Through the Django/Python shell (python3 manage.py shell)
# 3. Through the psql shell
# 4. Through the admin panel at /admin
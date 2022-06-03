from django.db import models
from django.conf import settings


# Create your models here.
User = settings.AUTH_USER_MODEL


class MLAlgorithm(models.Model):
    Gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    Married_choices = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    Education_choices = (
        ('Graduated', 'graduated'),
        ('Not_Graduate', 'not_graduated')
    )
    Employed_choices = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    LoanStatus_choices = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    PropertyArea_choices = (
        ('Urban', 'Urban'),
        ('Rural', 'Rural')
    )

    firstname = models.CharField(max_length=15, default='Firstname')
    lastname = models.CharField(max_length=15, default='Lastname')
    gender = models.CharField(max_length=15, choices=Gender_choices)
    married = models.CharField(max_length=15, choices=Married_choices)
    dependents = models.IntegerField(default=0)
    education = models.CharField(max_length=15, choices=Education_choices)
    self_employed = models.CharField(max_length=15, choices=Employed_choices)
    applicant_income = models.FloatField(default=0)
    coapplicant_income = models.FloatField(default=0)
    loan_amount = models.FloatField(default=0)
    loan_amount_term = models.FloatField(default=0)
    credit_histpry = models.FloatField(default=0)
    loan_status = models.CharField(max_length=15, choices=LoanStatus_choices)
    property_area = models.CharField(max_length=15, choices=PropertyArea_choices)


class MLAlgorithmStatus(models.Model):
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name="status")


class MLEndpoint(models.Model):
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class MLRequest(models.Model):
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)


class Approval(models.Model):
    Gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    Married_choices = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    firstname = models.CharField(max_length=15, null=True)
    lastname = models.CharField(max_length=15, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=15, choices=Gender_choices, null=True)
    married = models.CharField(max_length=15, choices=Married_choices, null=True)
    monthly_income = models.FloatField()
    monthly_debt = models.FloatField()
    amount_loan = models.FloatField()
    loan_ever_delinquent = models.IntegerField()
    revolving_utilization = models.FloatField()
    light_delinquencies = models.FloatField()
    serious_delinquencies = models.FloatField()


class Approval2(models.Model):
    Gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    Married_choices = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    First_time_choices = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    Occupancy_choices = (
        ('Primary Residence', 'Primary Residence'),
        ('Secondary Residence', 'Secondary Residence'),
        ('Investment Property', 'Investment Property'),
    )
    Property_choices = (
        ('Urban', 'Urban'),
        ('Sub Urban', 'Sub Urban'),
        ('Rural', 'Rural'),
    )

    firstname = models.CharField(max_length=15, null=True)
    lastname = models.CharField(max_length=15, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=15, choices=Gender_choices, null=True)
    married = models.CharField(max_length=15, choices=Married_choices, null=True)
    fico = models.FloatField()
    first_time_homebuyer = models.CharField(max_length=20, choices=First_time_choices)
    occupancy_status = models.CharField(max_length=20, choices=Occupancy_choices)
    dti = models.FloatField()
    upb = models.IntegerField()
    ppm = models.CharField(max_length=20)
    property_type = models.CharField(max_length=20)
    loan_purpose = models.CharField(max_length=20)
    original_loan_term = models.IntegerField()
    number_of_borrowers = models.FloatField()

    # things that split: occupancy_status, property_type, loan_purpose



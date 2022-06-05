from django import forms
from django.forms import fields
from django.forms.widgets import Input
from django.forms.utils import ValidationError
from django.utils.translation import gettext_lazy as _
from decimal import Decimal
from .models import Approval
from .models import Approval2


# Usual Model Form
# This file codes for the form of the parameters of our machine learning model and will display it as a form to user

# Ultimately used
class ApprovalForm(forms.ModelForm):
    firstname = forms.CharField(
        label="First Name:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "firstname",
                "id": "firstname",
                "placeholder": "Your first name",
            }
        )
    )
    lastname = forms.CharField(
        label="Last Name:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "lastname",
                "id": "lastname",
                "placeholder": "Your last name",
            }
        )
    )
    age = forms.IntegerField(label='Age:', required=False,
                             widget=forms.NumberInput(attrs={'placeholder': 'Enter Age'}))
    gender = forms.ChoiceField(
        required=False,
        label="Gender:",
        choices=[('Male', 'Male'), ('Female', 'Female')],
    )
    married = forms.ChoiceField(
        required=False,
        label="Married Status:",
        choices=[('Yes', 'Yes'), ('No', 'No')],
    )
    monthly_income = forms.FloatField(label="Monthly Income:",
                                      widget=forms.NumberInput(attrs={'placeholder': 'Enter monthly income'}))
    monthly_debt = forms.FloatField(label="Monthly Debt:",
                                    widget=forms.NumberInput(attrs={'placeholder': 'Enter monthly debt'}))
    amount_loan = forms.FloatField(label="Amount Loans:",
                                   widget=forms.NumberInput(
                                       attrs={'placeholder': 'Enter amount of loan repayments before'}))
    loan_ever_delinquent = forms.IntegerField(label='Loan Ever Delinquent',
                                              widget=forms.NumberInput(
                                                  attrs={'placeholder': 'Enter percentage of loans that have ever been late (should include any record)'}
                                              ))
    revolving_utilization = forms.FloatField(label="Revolving Utilization:",
                                             widget=forms.NumberInput(
                                                 attrs={'placeholder': 'Enter number of debt to credit limit'}))
    light_delinquencies = forms.FloatField(label="Light Delinquencies:",
                                           widget=forms.NumberInput(attrs={
                                               'placeholder': 'Enter number of times when your loans repayments have been less than 90 days'}))
    serious_delinquencies = forms.FloatField(label="Serious Delinquencies:",
                                             widget=forms.NumberInput(attrs={
                                                 'placeholder': 'Enter number of times when your loans repayments have been more than 90 days late'}))

    class Meta:
        model = Approval
        fields = '__all__'


# Another Machine learning form that could be implanted in the future to suit different scenarios better
# Not used
class ApprovalForm2(forms.ModelForm):
    firstname = forms.CharField(
        label="First Name:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "firstname",
                "id": "firstname",
                "placeholder": "Your first name",
            }
        )
    )
    lastname = forms.CharField(
        label="Last Name:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "lastname",
                "id": "lastname",
                "placeholder": "Your last name",
            }
        )
    )
    age = forms.IntegerField(label='Age:', required=False,
                             widget=forms.NumberInput(attrs={'placeholder': 'Enter Age'}))
    gender = forms.ChoiceField(
        required=False,
        label="Gender:",
        choices=[('Male', 'Male'), ('Female', 'Female')],
    )
    married = forms.ChoiceField(
        required=False,
        label="Married Status:",
        choices=[('Yes', 'Yes'), ('No', 'No')],
    )
    fico = forms.FloatField(label="Credit Score:",
                            widget=forms.NumberInput(attrs={'placeholder': 'Enter number of credit score (fico)'}))
    first_time_homebuyer = forms.ChoiceField(label="First Time Homebuyer:",
                                             choices=[('Yes', 'Yes'), ('No', 'No')],
                                             widget=forms.TextInput(attrs={'placeholder': 'Status as first time home buyer'}))
    occupancy_status = forms.ChoiceField(label="Occupancy Status:", choices=[('Primary Residence', 'Primary Residence'), ('Secondary Residence', 'Secondary Residence'), ('Investment Property', 'Investment Property')],
                                         widget=forms.NumberInput(attrs={'placeholder': 'Status of Occupancy'}))
    dti = forms.FloatField(label="Debt to Income Ratio:",
                           widget=forms.NumberInput(
                               attrs={'placeholder': 'Enter number of debt to income ratio'}))
    upb = forms.IntegerField(label="Unpaid Principal Balance:",
                             widget=forms.NumberInput(
                                 attrs={'placeholder': 'Enter number of unpaid principal balance'}))
    ppm = forms.CharField(label="Private Placement Memorandum:",
                          widget=forms.TextInput(attrs={'placeholder': 'Enter your private placement memorandum'}))
    property_type = forms.ChoiceField(label="Type of Property:",
                                      choices=[('Urban', 'Urban'), ('Sub Urban', 'Sub Urban'), ('Rural', 'Rural'),],
                                      widget=forms.TextInput(attrs={'placeholder': 'Enter type of property'}))
    loan_purpose = forms.CharField(label="Loan Purpose:",
                                   widget=forms.TextInput(attrs={'placeholder': 'Enter your loan purpose'}))
    original_loan_term = forms.IntegerField(label="Original Loan Term:",
                                            widget=forms.NumberInput(attrs={'placeholder': 'Enter number of original loan term'}))
    number_of_borrowers = forms.FloatField(label='Number of Borrowers',
                                           widget=forms.NumberInput(attrs={'placeholder': 'Enter the number of borrowers'}))

    class Meta:
        model = Approval2
        fields = '__all__'

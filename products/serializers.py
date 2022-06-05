from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import MLAlgorithm
from .models import MLEndpoint
from .models import MLRequest
from .models import MLAlgorithmStatus
from .models import Approval
from .models import Approval2

# This file is to serialize the parameters defined in the models, which can then be used for REST applications


# Not used
class MLAlgorithmSerializer(serializers.ModelSerializer):
    current_status = serializers.SerializerMethodField(read_only=True)

    def get_current_status(self, mlalgorithm):
        return MLAlgorithmStatus.objects.filter(parent_mlalgorithm=mlalgorithm).latest('created_at').status

    class Meta:
        model = MLAlgorithm
        read_only_fields = (
            'name',
            'gender',
            'married',
            'dependents',
            'education',
            'self_employed',
            'applicant_income',
            'coapplicant_income',
            'loan_amount',
            'loan_amount_term',
            'credit_histpry',
            'loan_status',
            'property_area'
        )
        fields = '__all__'


# Not used
class MLEndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLEndpoint
        read_only_fields = ("id", "name", "owner", "created_at")
        fields = read_only_fields


# Not used
class MLRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLRequest
        read_only_fields = (
            "id",
            "input_data",
            "full_response",
            "response",
            "created_at",
            "parent_mlalgorithm",
        )
        fields =  (
            "id",
            "input_data",
            "full_response",
            "response",
            "feedback",
            "created_at",
            "parent_mlalgorithm",
        )


# Not used
class MLAlgorithmStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLAlgorithmStatus
        read_only_fields = ("id", "active")
        fields = ("id", "active", "status", "created_by", "created_at", "parent_mlalgorithm")


# Ultimately used
class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approval
        fields = '__all__'


# Future implementation
# Not used
class ApprovalSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Approval2
        fields = '__all__'

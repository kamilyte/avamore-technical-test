from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from rest_framework.parsers import JSONParser
import logging
from .redemptionModel import redemption_model as model

@api_view(['POST'])
def redemption_model(request):
    input_data = JSONParser().parse(request)
    total_interest_due = model(float(input_data["facilitya"]), float(input_data["monthlyRate"]), input_data["beginningDefaultPeriod"], input_data["endDefaultPeriod"])
    return Response({'answer': "£" + str(total_interest_due)})





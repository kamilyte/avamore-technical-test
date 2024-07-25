from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .redemptionModel import redemption_model as model

# post request to put header data into the redemption model and returns the value of the total interest due
@api_view(['POST'])
def redemption_model(request):
    input_data = JSONParser().parse(request)
    total_interest_due = model(float(input_data["facilitya"]), float(input_data["monthlyRate"]), input_data["beginningDefaultPeriod"], input_data["endDefaultPeriod"])
    return Response({'answer': "£" + str(total_interest_due)})





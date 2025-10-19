from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timezone
import requests

CAT_FACT_API_URL = "https://catfact.ninja/fact"

@api_view(['GET'])
def get_profile(request):
    profile_data = {
        "name": "Iremide Joseph Adeyanju",
        "email": "iremideadeyanju9@gmail.com",
        "stack": "Python/Django",   
    }
    
    cat_fact = ""

    try:
        response = requests.get(CAT_FACT_API_URL, timeout=5)
        response.raise_for_status()
        cat_fact = response.json().get('fact', 'Could not get a cat fact.')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cat fact: {e}")
        cat_fact = "Failed to fetch the cat fact due to a network error."

    response_data = {
        "status": "success",
        "user": profile_data,
        "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "fact": cat_fact,
    }
    
    return Response(response_data, status=status.HTTP_200_OK)


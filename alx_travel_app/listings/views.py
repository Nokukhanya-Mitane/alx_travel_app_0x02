import os
import uuid
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Payment

CHAPA_SECRET_KEY = os.getenv("CHAPA_SECRET_KEY")
CHAPA_INIT_URL = "https://api.chapa.co/v1/transaction/initialize"
CHAPA_VERIFY_URL = "https://api.chapa.co/v1/transaction/verify/"

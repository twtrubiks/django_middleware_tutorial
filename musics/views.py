from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    # 1/0
    logger.warning('enter index views')
    return HttpResponse("Hello, World!")
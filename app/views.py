from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Fasteignakaup
from .serializers import FasteignakaupSerializer
from .import_kaupskra import import_kaupskra
import Levenshtein
from operator import itemgetter
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.

def home(request):
    return HttpResponse("Vinsamlegast skrifaðu inn virkan endapunkt")



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getData(request):
    items = Fasteignakaup.objects.all() 
    serializer = FasteignakaupSerializer(items, many=True)  
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getFastnumData(request, fastnum):
    items = Fasteignakaup.objects.filter(FASTNUM=fastnum)
    serializer = FasteignakaupSerializer(items, many=True)  
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getByAddress(request, address):
    items = Fasteignakaup.objects.all()
    filtered_items = []
    for item in items:
        distance = Levenshtein.distance(item.HEIMILISFANG, address)
        if distance < 4:
            filtered_items.append((item, distance))
    filtered_items.sort(key=itemgetter(1))  # Sort by Levenshtein distance
    sorted_items = [item[0] for item in filtered_items]  # Extract the items from the sorted list
    serializer = FasteignakaupSerializer(sorted_items, many=True)  
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAveragePrice(request):
    items = Fasteignakaup.objects.all()
    total = 0
    for item in items:
        total += (item.KAUPVERD*1000)
    if len(items) == 0:
        return Response({"message": "No data found"})
    average = total / len(items)
    return Response({"average": str(round(average)) + " kr"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAveragePriceByDate(request, date1, date2):
    items = Fasteignakaup.objects.filter(UTGDAG__range=[date1, date2])
    total = 0
    for item in items:
        total += (item.KAUPVERD*1000)
    if len(items) == 0:
        return Response({"message": "No data found"})
    average = total / len(items)
    return Response({"average": str(round(average)) + " kr"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAveragePriceByTowns(request, town, town2="", town3=""):
    items = Fasteignakaup.objects.filter(SVEITARFELAG__in=[town, town2, town3])
    total = 0
    for item in items:
        total += (item.KAUPVERD*1000)
    if len(items) == 0:
        return Response({"message": "No data found"})
    average = total / len(items)
    return Response({"average": str(round(average)) + " kr"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAveragePriceByPostcodes(request, postcode1, postcode2=0, postcode3=0):
    items = Fasteignakaup.objects.filter(POSTNR__in=[postcode1, postcode2, postcode3])
    total = 0
    for item in items:
        total += (item.KAUPVERD*1000)
    if len(items) == 0:
        return Response({"message": "No data found"})
    average = total / len(items)
    return Response({"average": str(round(average)) + " kr"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAveragePriceByTypeOfHousing(request, typeofhousing, typeofhousing2="", typeofhousing3=""):
    items = Fasteignakaup.objects.filter(TEGUND__in=[typeofhousing, typeofhousing2, typeofhousing3])
    total = 0
    for item in items:
        total += (item.KAUPVERD*1000)
    if len(items) == 0:
        return Response({"message": "No data found"})
    average = total / len(items)
    return Response({"average": str(round(average)) + " kr"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAverageSquareMeter(request):
    items = Fasteignakaup.objects.all()
    total = 0
    for item in items:
        total += item.EINFLM
    if len(items) == 0:
        return Response({"message": "No data found"})   
    average = total / len(items)
    return Response({"average" : str(round(average, 1)) + " fm"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAverageSquareMeterByDate(request, date1, date2):
    items = Fasteignakaup.objects.filter(UTGDAG__range=[date1, date2])
    total = 0
    for item in items:
        total += item.EINFLM
    if len(items) == 0:
        return Response({"message": "No data found"})
    average = total / len(items)
    return Response({"average" : str(round(average, 1)) + " fm"})

@api_view(['GET'])
def getAverageSquareMeterByTowns(request, town, town2="", town3=""):
    items = Fasteignakaup.objects.filter(SVEITARFELAG__in=[town, town2, town3])
    total = 0
    for item in items:
        total += item.EINFLM
    if len(items) == 0:
        return Response({"message": "No data found"})
    average = total / len(items)
    return Response({"average" : str(round(average, 1)) + " fm"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAverageSquareMeterByPostcodes(request, postcode1, postcode2=0, postcode3=0):
    items = Fasteignakaup.objects.filter(POSTNR__in=[postcode1, postcode2, postcode3])
    total = 0
    for item in items:
        total += item.EINFLM
    if len(items) == 0:
        return Response({"message": "No data found"})
    average = total / len(items)
    return Response({"average" : str(round(average, 1)) + " fm"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAverageSquareMeterByTypeOfHousing(request, typeofhousing, typeofhousing2="", typeofhousing3=""): 
    items = Fasteignakaup.objects.filter(TEGUND__in=[typeofhousing, typeofhousing2, typeofhousing3])
    total = 0
    for item in items:
        total += item.EINFLM
    if len(items) == 0:
        return Response({"message": "No data found"})
    average = total / len(items)
    return Response({"average" : str(round(average, 1)) + " fm"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAmountofDeals(request):
    items = Fasteignakaup.objects.all()
    return Response({"amount": len(items)})

@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def getAmountofDealsByDate(request, date1, date2):
    items = Fasteignakaup.objects.filter(UTGDAG__range=[date1, date2])
    return Response({"amount": len(items)})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAmountofDealsByTowns(request, town, town2="", town3=""):
    items = Fasteignakaup.objects.filter(SVEITARFELAG__in=[town, town2, town3])
    return Response({"amount": len(items)})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAmountofDealsByPostcodes(request, postcode1, postcode2=0, postcode3=0):
    items = Fasteignakaup.objects.filter(POSTNR__in=[postcode1, postcode2, postcode3])
    return Response({"amount": len(items)})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAmountofDealsByTypeOfHousing(request, typeofhousing, typeofhousing2="", typeofhousing3=""):
    items = Fasteignakaup.objects.filter(TEGUND__in=[typeofhousing, typeofhousing2, typeofhousing3])
    return Response({"amount": len(items)})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAveragePriceofSquareMeter(request):
    items = Fasteignakaup.objects.all()
    total = 0
    for item in items:
        total += (item.KAUPVERD*1000) / item.EINFLM
    if len(items) == 0:
        return Response({"message": "No data found"})
    average = total / len(items)
    return Response({"average": str(round(average, 1)) + " kr/fm"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAveragePriceofSquareMeterByDate(request, date1, date2):
    items = Fasteignakaup.objects.filter(UTGDAG__range=[date1, date2])
    total = 0
    for item in items:
        total += (item.KAUPVERD*1000) / item.EINFLM
    if len(items) == 0:
        return Response({"message": "No data found"})
    average = total / len(items)
    return Response({"average": str(round(average, 1)) + " kr/fm"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAveragePriceofSquareMeterByTowns(request, town, town2="", town3=""):
    items = Fasteignakaup.objects.filter(SVEITARFELAG__in=[town, town2, town3])
    total = 0
    for item in items:
        total += (item.KAUPVERD*1000) / item.EINFLM
    if len(items) == 0:
        return Response({"message": "No data found"})
    average = total / len(items)
    return Response({"average": str(round(average, 1)) + " kr/fm"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAveragePriceofSquareMeterByPostcodes(request, postcode1, postcode2=0, postcode3=0):
    items = Fasteignakaup.objects.filter(POSTNR__in=[postcode1, postcode2, postcode3])
    total = 0
    for item in items:
        total += (item.KAUPVERD*1000) / item.EINFLM
    if len(items) == 0:
        return Response({"message": "No data found"})   
    average = total / len(items)
    return Response({"average": str(round(average, 1)) + " kr/fm"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAveragePriceofSquareMeterByTypeOfHousing(request, typeofhousing, typeofhousing2="", typeofhousing3=""):
    items = Fasteignakaup.objects.filter(TEGUND__in=[typeofhousing, typeofhousing2, typeofhousing3])
    total = 0
    for item in items:
        total += (item.KAUPVERD*1000) / item.EINFLM
    if len(items) == 0:
        return Response({"message": "No data found"})
    average = total / len(items)
    return Response({"average": str(round(average, 1)) + " kr/fm"})

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateData(request):
    import_kaupskra()
    return Response({"message": "Data updated"})



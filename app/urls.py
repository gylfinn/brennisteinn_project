from django.urls import path, register_converter
from datetime import date, datetime
from . import views

class DateConverter:
    regex = r"\d{4}-\d{1,2}-\d{1,2}"
    format = "%Y-%m-%d"

    def to_python(self, value: str) -> date:
        return datetime.strptime(value, self.format).date()

    def to_url(self, value: date) -> str:
        return value.strftime(self.format)

register_converter(DateConverter, "date")


urlpatterns = [
    path("<int:fastnum>", views.getFastnumData),
    path("", views.home, name="home"),
    path("address/<str:address>", views.getByAddress, name="address"),


    path("averageprice", views.getAveragePrice, name="averageprice"),
    path("averagepricebydates/<date:date1>/<date:date2>", views.getAveragePriceByDate, name="averagepricebydate"),

    path("averagepricebytowns/<str:town>", views.getAveragePriceByTowns, name="averagepricebytown"),
    path("averagepricebytowns/<str:town>/<str:town2>", views.getAveragePriceByTowns, name="averagepricebytowns"),
    path("averagepricebytowns/<str:town>/<str:town2>/<str:town3>", views.getAveragePriceByTowns, name="averagepricebytowns"),

    path("averagepricebypostcode/<int:postcode1>", views.getAveragePriceByPostcodes, name="averagepricebypostcodes"),
    path("averagepricebypostcode/<int:postcode1>/<int:postcode2>", views.getAveragePriceByPostcodes, name="averagepricebypostcodes"),
    path("averagepricebypostcode/<int:postcode1>/<int:postcode2>/<int:postcode3>", views.getAveragePriceByPostcodes, name="averagepricebypostcodes"),

    path("averagepricebytypeofhousing/<str:typeofhousing>", views.getAveragePriceByTypeOfHousing, name="averagepricebytypeofhousing"),
    path("averagepricebytypeofhousing/<str:typeofhousing>/<str:typeofhousing2>", views.getAveragePriceByTypeOfHousing, name="averagepricebytypeofhousing"),
    path("averagepricebytypeofhousing/<str:typeofhousing>/<str:typeofhousing2>/<str:typeofhousing3>", views.getAveragePriceByTypeOfHousing, name="averagepricebytypeofhousing"),




    path("averagesquaremeter", views.getAverageSquareMeter, name="averagesquaremeter"),
    path("averagesquaremeterbydates/<date:date1>/<date:date2>", views.getAverageSquareMeterByDate, name="averagesquaremeterbydate"),

    path("averagesquaremeterbytowns/<str:town>", views.getAverageSquareMeterByTowns, name="averagesquaremeterbytown"),
    path("averagesquaremeterbytowns/<str:town>/<str:town2>", views.getAverageSquareMeterByTowns, name="averagesquaremeterbytowns"),
    path("averagesquaremeterbytowns/<str:town>/<str:town2>/<str:town3>", views.getAverageSquareMeterByTowns, name="averagesquaremeterbytowns"),

    path("averagesquaremeterbypostcode/<int:postcode1>", views.getAverageSquareMeterByPostcodes, name="averagesquaremeterbypostcodes"),
    path("averagesquaremeterbypostcode/<int:postcode1>/<int:postcode2>", views.getAverageSquareMeterByPostcodes, name="averagesquaremeterbypostcodes"),
    path("averagesquaremeterbypostcode/<int:postcode1>/<int:postcode2>/<int:postcode3>", views.getAverageSquareMeterByPostcodes, name="averagesquaremeterbypostcodes"),

    path("averagesquaremeterbytypeofhousing/<str:typeofhousing>", views.getAverageSquareMeterByTypeOfHousing, name="averagesquaremeterbytypeofhousing"),
    path("averagesquaremeterbytypeofhousing/<str:typeofhousing>/<str:typeofhousing2>", views.getAverageSquareMeterByTypeOfHousing, name="averagesquaremeterbytypeofhousing"),
    path("averagesquaremeterbytypeofhousing/<str:typeofhousing>/<str:typeofhousing2>/<str:typeofhousing3>", views.getAverageSquareMeterByTypeOfHousing, name="averagesquaremeterbytypeofhousing"),




    path("amountofdeals", views.getAmountofDeals, name="amountofdeals"),
    path("amountofdealsbydates/<date:date1>/<date:date2>", views.getAmountofDealsByDate, name="amountofdealsbydate"),

    path("amountofdealsbytowns/<str:town>", views.getAmountofDealsByTowns, name="amountofdealsbytown"),
    path("amountofdealsbytowns/<str:town>/<str:town2>", views.getAmountofDealsByTowns, name="amountofdealsbytowns"),
    path("amountofdealsbytowns/<str:town>/<str:town2>/<str:town3>", views.getAmountofDealsByTowns, name="amountofdealsbytowns"),

    path("amountofdealsbypostcode/<int:postcode1>", views.getAmountofDealsByPostcodes, name="amountofdealsbypostcodes"),
    path("amountofdealsbypostcode/<int:postcode1>/<int:postcode2>", views.getAmountofDealsByPostcodes, name="amountofdealsbypostcodes"),
    path("amountofdealsbypostcode/<int:postcode1>/<int:postcode2>/<int:postcode3>", views.getAmountofDealsByPostcodes, name="amountofdealsbypostcodes"),


    path("amountofdealsbytypeofhousing/<str:typeofhousing>", views.getAmountofDealsByTypeOfHousing, name="amountofdealsbytypeofhousing"),
    path("amountofdealsbytypeofhousing/<str:typeofhousing>/<str:typeofhousing2>", views.getAmountofDealsByTypeOfHousing, name="amountofdealsbytypeofhousing"),
    path("amountofdealsbytypeofhousing/<str:typeofhousing>/<str:typeofhousing2>/<str:typeofhousing3>", views.getAmountofDealsByTypeOfHousing, name="amountofdealsbytypeofhousing"),
    



    path("averagepriceofsquaremeter", views.getAveragePriceofSquareMeter, name="averagepriceofsquaremeter"),
    path("averagepriceofsquaremeterbydates/<date:date1>/<date:date2>", views.getAveragePriceofSquareMeterByDate, name="averagepriceofsquaremeterbydate"),

    path("averagepriceofsquaremeterbytowns/<str:town>", views.getAveragePriceofSquareMeterByTowns, name="averagepriceofsquaremeterbytown"),
    path("averagepriceofsquaremeterbytowns/<str:town>/<str:town2>", views.getAveragePriceofSquareMeterByTowns, name="averagepriceofsquaremeterbytowns"),
    path("averagepriceofsquaremeterbytowns/<str:town>/<str:town2>/<str:town3>", views.getAveragePriceofSquareMeterByTowns, name="averagepriceofsquaremeterbytowns"),

    path("averagepriceofsquaremeterbypostcode/<int:postcode1>", views.getAveragePriceofSquareMeterByPostcodes, name="averagepriceofsquaremeterbypostcodes"),
    path("averagepriceofsquaremeterbypostcode/<int:postcode1>/<int:postcode2>", views.getAveragePriceofSquareMeterByPostcodes, name="averagepriceofsquaremeterbypostcodes"),
    path("averagepriceofsquaremeterbypostcode/<int:postcode1>/<int:postcode2>/<int:postcode3>", views.getAveragePriceofSquareMeterByPostcodes, name="averagepriceofsquaremeterbypostcodes"),

    path("averagepriceofsquaremeterbytypeofhousing/<str:typeofhousing>", views.getAveragePriceofSquareMeterByTypeOfHousing, name="averagepriceofsquaremeterbytypeofhousing"),
    path("averagepriceofsquaremeterbytypeofhousing/<str:typeofhousing>/<str:typeofhousing2>", views.getAveragePriceofSquareMeterByTypeOfHousing, name="averagepriceofsquaremeterbytypeofhousing"),
    path("averagepriceofsquaremeterbytypeofhousing/<str:typeofhousing>/<str:typeofhousing2>/<str:typeofhousing3>", views.getAveragePriceofSquareMeterByTypeOfHousing, name="averagepriceofsquaremeterbytypeofhousing"),

    path("updatedata", views.updateData, name="update"),
]   

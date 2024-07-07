from city.models import City


class CitySelector:

    @staticmethod
    def get_cities():
        return City.objects.all()

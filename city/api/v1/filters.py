import django_filters


class CityFilter(django_filters.FilterSet):
    csv_file_id = django_filters.CharFilter(field_name="csv_file_id")
    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains"
    )
    description = django_filters.CharFilter(
        field_name="description", lookup_expr="icontains"
    )
    population = django_filters.CharFilter(field_name="population")
    population_range = django_filters.RangeFilter(field_name="population")
    established = django_filters.DateFromToRangeFilter(
        field_name="established_at",
        label="use established_after and established_before",
    )
    established_at = django_filters.DateFilter(
        field_name="established_at"
    )

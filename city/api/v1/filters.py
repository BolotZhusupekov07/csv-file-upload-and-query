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
    established_at = django_filters.DateFromToRangeFilter(
        field_name="established_at",
        label="use established_at_after and established_at_before",
    )

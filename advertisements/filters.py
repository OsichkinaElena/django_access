from django_filters import rest_framework as filters, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter()
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['id', 'status', 'creator', 'created_at', 'title']

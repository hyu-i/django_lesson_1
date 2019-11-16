from django.db.models import Q
from django.views import generic
from .models import Driver


class IndexView(generic.ListView):
    model = Driver
    paginate_by = 15

    def get_queryset(self):
        queryset = Driver.objects.all()
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(name__icontains=keyword)| Q(company__name__icontains=keyword)
            )

        return queryset


class DetailView(generic.DetailView):
    model = Driver
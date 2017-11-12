
from .models import Slider


def get_defaults(request):
    context = {}

    context['slider'] = Slider.objects.all()


    return context
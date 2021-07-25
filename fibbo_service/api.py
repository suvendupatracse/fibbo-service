from rest_framework.views import APIView
from rest_framework.response import Response

from .utility import get_n_fibbo


class Fibbo(APIView):    

    def get(self, request):
        try:
            n_fibbo = get_n_fibbo(int(request.GET["n"]))
        except ValueError:
            return Response({"errors": "Invalid number"}, status=404)
        return Response(n_fibbo)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Livro
from ..serializers import LivrosSerializer

@api_view()
def livro_api_list(request):
    livros = Livro.objects.get_published()[:10]
    serializers = LivrosSerializer(instance=livros, many=True)
    
    return Response(serializers.data)
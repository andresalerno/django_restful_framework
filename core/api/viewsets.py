from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.filters import SearchFilter


class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', '^endereco__linha1') # eu posso buscar um dado especifico de uma outra classe, no caso endereco, no campo linha 1
    
    # http_method_names = ['DELETE',] # para que a function destroy funcione de fato
    
    # def get_queryset(self):
    #     return PontoTuristico.objects.filter(aprovado=True) # filtrado os aprovados
    
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
            
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
            
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)
            
        return queryset
    
    
    # uma vez definida elas redefinem as actions padrões do django restframework
    def list(self, request, *args, **kwargs): # essa função subscreve a função GET nativa do Django
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs): # para subscrever o método POST
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs): # para subscrever o método POST
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs): # diferemte do list que lista todos os registros, aqui você precisa dizer qual o registro
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)
    
    def parcial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).parcial_update(request, *args, **kwargs)
    
    # @action(detail=True, methods=['GET', 'POST']) # personalizar uma action
    # def denunciar(self, request, pk=None):
    #     pass
    
    # @action(detail=False, methods=['GET']) # detail false eu não preciso identificar o recurso (pk)
    # def teste(self, request):
    #     pass
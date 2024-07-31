from rest_framework import viewsets
from apps.generic_tables.api.serializers.attributes_serializer import AttributesSerializer
from django.shortcuts import get_object_or_404
from apps.generic_tables.models import Attributes
from apps.helper.api_response_generic import api_response
from rest_framework import status


class AttributesViewSet(viewsets.GenericViewSet):
    serializer_class = AttributesSerializer
    Attributes = Attributes
    queryset = None
    
    def get_object(self, pk):
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk)
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
                            
    
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            attributes_serializer = self.get_serializer(page, many=True)
            paginated_response = {
                'count': self.paginator.page.paginator.count,
                'next': self.paginator.get_next_link(),
                'previous': self.paginator.get_previous_link(),
                'results': attributes_serializer.data
            }
            return api_response(paginated_response, 'Atributis Obtenidos Exitosamente!', status.HTTP_200_OK, None)
        attributes_serializer = self.get_serializer(queryset, many=True)
        if queryset.exists():
            return api_response(attributes_serializer.data, 'Atributis Obtenidos Exitosamente!', status.HTTP_200_OK, None)
        return api_response([], None, status.HTTP_404_NOT_FOUND, 'No se encontraron registros')

    
    def create(self, request):
        attributes_serializer= self.serializer_class(data = request.data)
        if attributes_serializer.is_valid():
            attributes_serializer.save()
            return api_response(attributes_serializer.data,'Atributo Creado Exitosamente!', status.HTTP_201_CREATED,None )
        return api_response([],None, status.HTTP_400_BAD_REQUEST,attributes_serializer.errors )
    
    def retrieve(self, request, pk=None):
        attributes = self.get_object(pk)
        attributes_serializer = self.serializer_class(attributes)
        return api_response(attributes_serializer.data,'Atributo Obtenido Exitosamente!',status.HTTP_200_OK,None)
    
    def update(self,request, pk=None):
        attributes = self.get_object(pk)
        attributes_serializer = self.serializer_class(attributes, data=request.data)
        if attributes_serializer.is_valid():
            attributes_serializer.save()
            return api_response(attributes_serializer.data,"Atributo Actualizado Correctamente",status.HTTP_200_OK,None)           
        return api_response([],None,status.HTTP_200_OK,attributes_serializer.errors)           


    def destroy(self, request, pk=None):
        attribute_destroy = self.Attributes.objects.filter(id = pk).update(state= False)
        if attribute_destroy == 1:
            return api_response([], 'Atributo Eliminado Correctamente',status.HTTP_200_OK,None)
        return api_response([], None,status.HTTP_404_NOT_FOUND,'El Atributo Que Desea Eliminar No Fue Encontrado')
    
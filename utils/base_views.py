from rest_framework.views import APIView, Response, Request, status
from django.shortcuts import get_object_or_404
class ListBaseView:
    def list(self, request: Request) -> Response:
        queryset = self.view_queryset.all()
        serializer = self.view_serializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
class CreateBaseView:
    def create(self, request: Request) -> Response:
       
        serializer = self.view_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class RetrieveBaseView:
    def retrieve(self, request: Request, pk: int, *args: tuple, **kwargs: dict) -> Response:
        url_param = kwargs.get(self.url_param_name)
        obj = get_object_or_404(self.view_queryset, pk=url_param)
        self.check_object_permissions(request, obj)
        serializer = self.view_serializer(obj)

        return Response(serializer.data, status.HTTP_200_OK)
class UpdateBaseView:
    def update(self, request: Request, pk: int, *args: tuple, **kwargs: dict) -> Response:
        url_param = kwargs.get(self.url_param_name)
        obj = get_object_or_404(self.view_queryset, pk=url_param)
        self.check_object_permissions(request, obj)
        serializer = self.view_serializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

class RemoveBaseView:
    def remove(self, request: Request, pk: int, *args: tuple, **kwargs: dict) -> Response:
        url_param = kwargs.get(self.url_param_name)
        obj = get_object_or_404(obj, pk=url_param)
        self.check_object_permissions(request, obj)
        obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

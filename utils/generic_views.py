from rest_framework.views import APIView, Request, Response
from .base_views import ListBaseView, CreateBaseView, RetrieveBaseView, UpdateBaseView, RemoveBaseView
class GenericBaseView(APIView):
    view_queryset = None
    view_serializer = None
   
class ListGenericView(ListBaseView,GenericBaseView):
    def get(self, request: Request) -> Response:
        return super().list(request)
class CreateGenericView(CreateBaseView, GenericBaseView):
    def post(self, request: Request) -> Response:
        return super().create(request)
class RetrieveGenericView(RetrieveBaseView, GenericBaseView):
    def get(self, request: Request,  *args: tuple, **kwargs: dict) -> Response:
        return super().retrieve(request, *args, **kwargs)
class UpdateGenericView(UpdateBaseView, GenericBaseView):
    def patch(self, request: Request,  *args: tuple, **kwargs: dict) -> Response:
        return super().update(request, *args, **kwargs)
class RemoveGenericView(RemoveBaseView, GenericBaseView):
    def delete(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().destroy(request, *args, **kwargs)
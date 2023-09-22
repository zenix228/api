from rest_framework import generics, mixins, response, status, permissions
from rest_framework.response import Response
from app.models import Client, Blog, Sponsor
from .serializers import ClientSerializer, BlogSerializer, SponsorSerializer

# клиент 

class ClientList(generics.ListAPIView):   # Get List
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
class ClientDetail(generics.RetrieveAPIView): # Get Detail
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
class ClientPost(generics.CreateAPIView): # Post
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
class ClientPut(generics.UpdateAPIView): # Put
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
class ClientDelete(generics.DestroyAPIView): # Delete
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# блог

class BLogList(generics.ListAPIView):   # Get List
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
class BlogDetail(generics.RetrieveAPIView): # Get Detail
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
class BlogPost(generics.CreateAPIView): # Post
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
class BlogPut(generics.UpdateAPIView): # Put
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
class BlogDelete(generics.DestroyAPIView): # Delete
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# sponsor

class SponsorList(generics.ListAPIView):   # Get List
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
class SponsorDetail(generics.RetrieveAPIView): # Get Detail
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
class SponsorPost(generics.CreateAPIView): # Post
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
class SponsorPut(generics.UpdateAPIView): # Put
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
class SponsorDelete(generics.DestroyAPIView): # Delete
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

class ClientAPI(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return []
    
    def get(self, request, *args, **kwargs):
        menu = self.get_queryset().all()
        serializer = self.get_serializer(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class ClientDetailAPI(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        elif self.request.method == ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return []
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class BlogAPI(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return []
    
    def get(self, request, *args, **kwargs):
        menu = self.get_queryset().all()
        serializer = self.get_serializer(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class BlogDetailAPI(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        elif self.request.method == ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return []
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class SponsorAPI(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    
    queryset = Sponsor.objects.all()
    serializer_class = BlogSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        elif self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return []
    
    def get(self, request, *args, **kwargs):
        menu = self.get_queryset().all()
        serializer = self.get_serializer(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class SponsorDetailAPI(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    
    queryset = Sponsor.objects.all()
    serializer_class = BlogSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return []
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
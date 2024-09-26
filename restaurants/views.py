from rest_framework import viewsets
from .models import Restaurant, Menu, Employee, Vote
from .serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import date
from rest_framework.permissions import IsAuthenticated, AllowAny

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [AllowAny] # Has to be IsAuthenticated

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny] # Has to be IsAuthenticated

    @action(detail=False, methods=['get'])
    def today(self, request):
        today = date.today()
        menus_today = self.queryset.filter(date=today)
        serializer = self.get_serializer(menus_today, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        menu = self.get_object()
        user = request.user

        try:
            employee = Employee.objects.get(user=user)
        except Employee.DoesNotExist:
            return Response({'detail': 'Employee not found for this user.'}, status=404)

        if Vote.objects.filter(employee=employee, menu=menu).exists():
            return Response({'detail': 'You have already voted for this menu.'}, status=400)

        Vote.objects.create(employee=employee, menu=menu)
        return Response({'detail': 'Vote recorded successfully.'}, status=201)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]
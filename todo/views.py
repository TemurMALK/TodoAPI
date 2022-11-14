from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *




class PlanlarAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request):
        planlar = Plan.objects.filter(user=request.user)
        serializer = PlanSerializer(planlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        plan = request.data
        serializer = PlanSerializer(data=plan)
        if serializer.is_valid():
            serializer.save(user=request.user)
            natija = {"Succes":"True",
                      "Yangi plan":serializer.data}
            return Response(natija)
        return Response({"xabar": "Ma'lumotda xatolik bor!"})
class PlanAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request, pk):
        plan = Plan.objects.get(id=pk)
        serializer = PlanSerializer(plan)
        return Response(serializer.data)

    def put(self, request, pk):
        plan = Plan.objects.get(id=pk)
        serializer = PlanSerializer(plan, data = request.data)
        if serializer.is_valid():
            serializer.save()
            natija = {"xabar":"Saqlandi!",
                      "qo'shilgan malumot": serializer.data}
            return Response(natija, status = status.HTTP_201_CREATED)
        return Response({"xabar":"Ma'lumotda xatolik bor!", "detail":serializer.errors})

    def delete(self, request, pk):
        plan = Plan.objects.get(id=pk)
        plan.delete()
        return Response({"xabar":"Ma'lumot o'chdi!"})


from django.shortcuts import render
from rest_framework import viewsets
from .models import Candidate
from .serializers import CandidateSerializer

class CandidateView(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
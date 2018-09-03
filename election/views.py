from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Candidate, Election
from .serializers import CandidateSerializer, ElectionSerializer
from .permissions import CanCreateOrUpdateElectionPermission


class CandidateView(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ElectionView(viewsets.ModelViewSet):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes = (permissions.IsAuthenticated, CanCreateOrUpdateElectionPermission)

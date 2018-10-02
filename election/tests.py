from django.test import TestCase

import json

from model_mommy import mommy
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse

from shared.tests import BaseTestCase
from election.models import Election
from election.serializers import ElectionSerializer


class ElectionViewSetTest(BaseTestCase):
    """
    ElectionViewSet tests
    """

    def setUp(self):
        super(ElectionViewSetTest, self).setUp()

        self.valid_election = {
            "label": "Eleição para Presidência do Brasil",
            "start_date": "2018-02-12",
            "end_date": "2018-02-12",
            "candidates": [
                1,
                2
            ]
        }

    @classmethod
    def setUpTestData(cls):
        cls.election = mommy.make('election.Election')

    # CREATE

    def test_it_is_not_possible_to_create_a_election(self):
        """
        Ensure we can't create a election
        """
        url = reverse('election-list')
        response = self.client.post(url, self.valid_election, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # UPDATE

    def test_it_is_not_possible_to_update_a_election(self):
        """
        Ensure we can update a election
        """
        url = reverse('election-detail', kwargs={'pk': self.election.pk})
        response = self.client.put(url, self.valid_election, format='json')

        self.assertEqual(response.status_code,
                         status.HTTP_403_FORBIDDEN)

    # DELETE

    def test_it_is_not_possible_to_delete_a_election(self):
        """
        Ensure we can't delete a election
        """
        url = reverse('election-detail', kwargs={'pk': self.election.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code,
                         status.HTTP_204_NO_CONTENT)

    # READ LIST

    def test_it_is_possible_to_read_all_election(self):
        """
        Ensure we can read all election
        """
        url = reverse('election-list')
        response = self.client.get(url)

        elections = Election.objects.all()
        serializer = ElectionSerializer(elections, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)

    # READ DETAIL

    def test_it_is_possible_to_read_election(self):
        """
        Ensure we can read a election detail
        """
        url = reverse('election-detail', kwargs={'pk': self.election.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ElectionSerializer(self.election).data)
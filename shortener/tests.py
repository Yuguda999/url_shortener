from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ShortURL

class URLShortenerTests(APITestCase):
    def setUp(self):
        self.create_url = reverse("create_short_url")  # POST to create short URL
        self.test_url = "https://www.example.com/test-url"
        self.short_url = ShortURL.objects.create(
            url=self.test_url,
            short_code="abc123"
        )

    def test_create_short_url(self):
        """Test creating a new short URL"""
        data = {"url": "https://www.example.com/some/long/url"}
        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("short_code", response.data)

    def test_retrieve_original_url(self):
        """Test retrieving the original URL from a short URL"""
        url = reverse("retrieve_original_url", kwargs={"short_code": self.short_url.short_code})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["url"], self.test_url)

    def test_update_short_url(self):
        """Test updating an existing short URL"""
        update_url = reverse("update_short_url", kwargs={"short_code": self.short_url.short_code})
        new_url = "https://www.example.com/updated-url"
        response = self.client.put(update_url, {"url": new_url}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["url"], new_url)

    def test_delete_short_url(self):
        """Test deleting a short URL"""
        delete_url = reverse("delete_short_url", kwargs={"short_code": self.short_url.short_code})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ShortURL.objects.filter(short_code=self.short_url.short_code).exists())

    def test_url_statistics(self):
        """Test retrieving access statistics for a short URL"""
        stats_url = reverse("url_stats", kwargs={"short_code": self.short_url.short_code})
        response = self.client.get(stats_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["access_count"], 0)

    def test_invalid_short_code(self):
        """Test retrieving, updating, and deleting with an invalid short code"""
        invalid_short_code = "invalid123"
        retrieve_url = reverse("retrieve_original_url", kwargs={"short_code": invalid_short_code})
        update_url = reverse("update_short_url", kwargs={"short_code": invalid_short_code})
        delete_url = reverse("delete_short_url", kwargs={"short_code": invalid_short_code})
        stats_url = reverse("url_stats", kwargs={"short_code": invalid_short_code})

        # Retrieve
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Update
        response = self.client.put(update_url, {"url": "https://www.example.com/new-url"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Delete
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Stats
        response = self.client.get(stats_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

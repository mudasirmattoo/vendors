from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Vendor, PurchaseOrder

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.superuser = Vendor.objects.create_superuser(username='admin', email='admin@example.com', password='admin123')

    def test_vendor_management(self):
        # Test creating a vendor
        response = self.client.post('/api/vendors/', {'name': 'Test Vendor', 'contact_details': 'test@example.com', 'address': '123 Test St', 'vendor_code': 'ABC123'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test retrieving all vendors
        response = self.client.get('/api/vendors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # Test retrieving a specific vendor
        vendor_id = response.data[0]['id']
        response = self.client.get(f'/api/vendors/{vendor_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test updating a vendor
        response = self.client.put(f'/api/vendors/{vendor_id}/', {'name': 'Updated Vendor'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test deleting a vendor
        response = self.client.delete(f'/api/vendors/{vendor_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_purchase_order_tracking(self):
        # Create a vendor
        vendor = Vendor.objects.create(name='Test Vendor', contact_details='test@example.com', address='123 Test St', vendor_code='ABC123')

        # Test creating a purchase order
        response = self.client.post('/api/purchase_orders/', {'vendor': vendor.id, 'po_number': 'PO123', 'order_date': '2024-05-10', 'delivery_date': '2024-05-20', 'items': {}, 'quantity': 1, 'status': 'pending'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test retrieving all purchase orders
        response = self.client.get('/api/purchase_orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # Test retrieving a specific purchase order
        po_id = response.data[0]['id']
        response = self.client.get(f'/api/purchase_orders/{po_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test updating a purchase order
        response = self.client.put(f'/api/purchase_orders/{po_id}/', {'status': 'completed'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test deleting a purchase order
        response = self.client.delete(f'/api/purchase_orders/{po_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

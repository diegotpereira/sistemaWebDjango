from django.test import TestCase
from django.test.client import Client
 
from supplier.models import Supplier

# Create your tests here.

class SupplierTestCase(TestCase):
    fixtures = ['supplier.json']
 
    def setUp(self):
       self.client = Client()
 
    def test_list_supplier_no_phone(self):
       expected = Supplier.objects.exclude(phone__isnull=True).exclude(phone__exact='')
 
       response = self.client.get('/fornecedores/')
       self.failUnlessEqual(response.status_code, 200)
       self.failUnlessEqual(len(response.context['supplier_list']), len(expected))

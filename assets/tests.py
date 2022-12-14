from datetime import date

from django.test import TestCase
from rest_framework.test import APIClient
from assets.models import Asset, DynamicAsset, StaticAsset
from users.tests import create_user
from vendors.tests import create_vendor
from locations.tests import create_location

def get_asset(id):
  return Asset.objects.get(id=id)

def create_asset():
  vendor = create_vendor()
  location = create_location()
  data = {
    'name': 'Asset Main',
    'price': 500000,
    'vendor': vendor,
    'location': location,
    'warrantyYears': 2,
    'usefulLife': 10
  }

  return DynamicAsset.objects.create(**data)

def create_asset_static():
  vendor = create_vendor()
  location = create_location()
  data = {
    'name': 'Asset Main',
    'price':500000,
    'vendor': vendor,
    'location': location,
    'warrantyYears': 2,
    'usefulLife': 10
  }

  return StaticAsset.objects.create(**data)

class AssetTestCase(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.user = create_user()
    self.client.login(username='TestUser', password='TestPassword')

  def test_create_dynamic_asset_create_dynamic_object(self):
    self.assertEqual(Asset.objects.all().count(), 0)
    create_asset()
    self.assertEqual(Asset.objects.all().count(), 1)
    self.assertEqual(StaticAsset.objects.all().count(), 0)

  def test_create_asset_static_create_static_object(self):
    self.assertEqual(Asset.objects.all().count(), 0)
    create_asset_static()
    self.assertEqual(Asset.objects.all().count(), 1)
    self.assertEqual(DynamicAsset.objects.all().count(), 0)

  def test_update_last_inspect(self):
    asset = create_asset()
    asset.update_last_inspect()
    self.assertEqual(Asset.objects.get(id=asset.id).lastInspection, date.today())
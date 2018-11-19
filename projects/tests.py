from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project,UserProfile

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_profile = UserProfile(id=1,user=self.new_user,profile_pic='photos/pic',bio='user-bio')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,UserProfile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = UserProfile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = UserProfile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_update_bio(self):
        self.new_profile.save_profile()
        self.new_profile = UserProfile.objects.get(id=1)
        profile = self.new_profile
        profile.update_bio('updated user-bio')
        self.updated_profile = UserProfile.objects.get(id=1)
        self.assertEqual(self.updated_profile.bio,'updated user-bio')

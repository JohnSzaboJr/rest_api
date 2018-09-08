from django.test import TestCase

def test_api_can_get_a_user(self):
    #testing if api can get a given User
    user = Users.objects.get()
    response = self.client.get(
        reverse('details', kwargs = {'pk': user.uid}), format='json')

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, user)

def test_api_can_update_user(self):
    #testing if api can update a given User
    change_user = {'name': 'Something Else'}
    res = self.client.put(
        reverse('details', kwargs={'pk': user.uid}),
        change_user, format='json')
    self.assertEqual(res.status_code, status.HTTP_200_OK)

def test_api_can_delete_user(self):
    #testing if api can delete a given User
    user = Users.objects.get()
    response = self.client.delete(
        reverse('details', kwargs={'pk': user.uid}),
        format='json', follow=True)
    self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

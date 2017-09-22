from django.test import TestCase, Client


class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_event_endpoint_200(self):
        response = self.client.get("/event/?format=json")
        assert response.status_code, 200

    def test_person_endpoint_200(self):
        response = self.client.get("/person/?format=json")
        assert response.status_code, 200

    def test_usuario_endpoint_200(self):
        response = self.client.get("/usuario/?format=json")
        assert response.status_code, 200

    def test_transaccion_endpoint_200(self):
        response = self.client.get("/transaccion/?format=json")
        assert response.status_code, 200

    def tearDown(self):
        pass

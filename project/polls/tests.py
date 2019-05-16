from django.test import TestCase
from django.http import request
from .models import Statement, Autor
from .views import change_autors

# Create your tests here.


class DataTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        number_of_statements = 5
        for statement_num in range(number_of_statements):
            Statement.objects.create(name='Statement #' + str(statement_num))


    def test_add_data_to_database(self):
        statements = Statement.objects.all();
        k = 0
        for i in statements:
            self.assertEquals(i.name, 'Statement #' + str(k))
            k = k + 1

    def test_changed_autor(self):
        change_autors()
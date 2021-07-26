import pytest
from django.urls import reverse

from fibbo_service.utility import get_n_fibbo


@pytest.mark.parametrize("number, expected", [(0,0),(1,1),(2,1),(3, 2),(4, 3),(26, 121393)])
def test_fibbonaci_service_with_positive_numbers(client, number, expected):
    url = f"{reverse('fibbonaci-number')}?n={number}"
    response = client.get(url)
    assert response.status_code == 200
    data =  response.json()
    assert data == expected

def test_fibbonaci_service_with_negative_numbers(client,):
    url = f"{reverse('fibbonaci-number')}?n=-1"
    response = client.get(url)
    assert response.status_code == 400

def test_fibbonaci_service_with_string(client,):
    url = f"{reverse('fibbonaci-number')}?n=suvendu"
    response = client.get(url)
    assert response.status_code == 400

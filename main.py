import configuration
import data
import requests



def new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
    json=data.order_body)


def order_info(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFO,
     params={"t": track_number})


def track_number_of_order():
    track_number = new_order()
    return track_number.json()["track"]


def test_create_new_order_and_track():
    track_number = track_number_of_order()
    get_response = order_info(track_number)
    assert get_response.status_code == 200
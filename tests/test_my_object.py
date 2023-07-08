import allure
import pytest

from pytest_demo.my_object import MyObject


@pytest.fixture(scope="class")
def my_obj():
    return MyObject()


@pytest.fixture(scope="class")
def data(request):
    yield request.param


@allure.step("Is the default of value property as expected?")
def test_value_default(my_obj):
    assert my_obj.value is None


@pytest.mark.parametrize("data", [1, 2], indirect=True)
@pytest.mark.incremental
class TestNothing:

    @allure.step("Does the setter of the value property work?")
    def test_value_setter(self, my_obj: MyObject, data):
        my_obj.value = data

    @allure.step("Does the getter of the value property work?")
    def test_value_getter(self, my_obj: MyObject, data):
        assert my_obj.value == data

    @allure.step("Does the str magic methods work?")
    def test_str(self, my_obj: MyObject, data):
        assert str(my_obj) == f"MyObject({data})"

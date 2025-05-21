import random
import pytest

@pytest.fixture(params=[random.randint(3, 25) for _ in range(5)])
def random_account_id(request):
    return request.param




import os,sys

sys.path.append(os.getcwd())

import pytest

@pytest.mark.webtest
def test_send_http():
    pass # perform some webtest test for your app
def test_something_quick():
    pass
def test_another():
    pass
class TestClass:
    def test_method(self):
        pass

if __name__ == "__main__":
    pytest.main(["-s", "test_a.py", "-m", "not webtest"])
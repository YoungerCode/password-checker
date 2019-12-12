import pytest
from password_cheker import *

def test_password_is_ok():
    with pytest.raises(Exception):
        assert password_is_valid('Yanga') == Exception('Password has to be longer than 8 characters')
        assert password_is_valid('YANGALUSITI') ==Exception('password should have at least one lowercase letter')
        assert password_is_valid('yangalusiti') ==Exception('password should have at least one uppercase letter')

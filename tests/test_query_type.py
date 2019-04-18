import pytest

import pydig


def _valid_enums():
    """
    Returns a tuple of (value, enum) for use in the test_enum_get_valid test
    """
    for query_type in pydig.QueryType:
        yield query_type.name, query_type
        yield query_type.name.lower(), query_type
        yield query_type.value, query_type
        yield query_type, query_type


@pytest.mark.parametrize('value, result', _valid_enums())
def test_enum_get_valid(value, result):
    """
    Test that the get method can handle names (upper and lowercase) and record ids
    """
    assert pydig.QueryType.get(value) == result


def test_enum_get_invalid_string():
    """
    Tests that when an invalid record type is passed we raise an InvalidQueryType exception
    """
    with pytest.raises(pydig.InvalidQueryType):
        pydig.QueryType.get('INVALID')


def test_enum_get_invalid_int():
    """
    Tests that when an invalid record id is passed we raise an InvalidQueryType exception
    """
    with pytest.raises(pydig.InvalidQueryType):
        pydig.QueryType.get(9999)

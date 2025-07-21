import pytest
from Ternary import Ternary

@pytest.mark.parametrize(
    "input_value,expected_repr",
    [
        (True, "<class 'Ternary(True)'>"),
        (False, "<class 'Ternary(False)'>"),
        (None, "<class 'Ternary(Unknown)'>"),
        (1, "<class 'Ternary(True)'>"),  # Non-bool, truthy value
        (0, "<class 'Ternary(False)'>"), # Non-bool, falsy value
        ("", "<class 'Ternary(False)'>"), # Empty string, falsy
        ("nonempty", "<class 'Ternary(True)'>"), # Non-empty string, truthy
        ([], "<class 'Ternary(False)'>"), # Empty list, falsy
        ([1,2,3], "<class 'Ternary(True)'>"), # Non-empty list, truthy
        ({}, "<class 'Ternary(False)'>"), # Empty dict, falsy
        ({"a": 1}, "<class 'Ternary(True)'>"), # Non-empty dict, truthy
    ],
    ids=[
        "true_value",
        "false_value",
        "none_value",
        "int_truthy",
        "int_falsy",
        "empty_string",
        "nonempty_string",
        "empty_list",
        "nonempty_list",
        "empty_dict",
        "nonempty_dict",
    ]
)
def test_ternary_repr_various_inputs(input_value, expected_repr):

    # Arrange
    t = Ternary(input_value)

    # Act
    result = t.__repr__()

    # Assert
    assert result == expected_repr
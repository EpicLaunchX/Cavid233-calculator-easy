from unittest import mock

import pytest

from src.pytemplate.domain.models import Operands, operands_factory
from src.pytemplate.entrypoints.cli.main import main
from src.pytemplate.service.calculator import Calculator


def test_add_function():
    operands = Operands(5, 6)

    assert Calculator().add(operands) == 11


def test_subtract_function():
    operands = Operands(5, 6)

    assert Calculator().subtract(operands) == -1


def test_multiply_function():
    operands = Operands(5, 6)

    assert Calculator().multiply(operands) == 30


def test_divide_function():
    operands = Operands(35, 6)

    assert Calculator().divide(operands) == 5


def test_set_class_values():
    operands = Operands(5, 6)
    assert operands.first_operand == 5
    assert operands.second_operand == 6


def test_set_empty_second_operand_value():
    with pytest.raises(TypeError) as e:
        operands = Operands(5)


def test_set_empty_second_operand_value():
    with pytest.raises(TypeError) as e:
        operands = Operands(5)


def test_set_empty_all_operand_value():
    with pytest.raises(TypeError) as e:
        operands = Operands()


def test_operands_factory():

    result = operands_factory(5, 6)

    assert isinstance(result, Operands) == True


def test_main_divide():
    with mock.patch("builtins.input", return_value="6,3,divide") as mock_result:
        result = main()
        assert result == 2

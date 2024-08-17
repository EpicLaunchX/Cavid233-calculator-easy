import pytest

from pytemplate.domain.models import Operands, operands_factory


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


def test_operands_factory_function():

    result = operands_factory(5, 6)

    assert isinstance(result, Operands) == True

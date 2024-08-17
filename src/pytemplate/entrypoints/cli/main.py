from pytemplate.domain.models import Operands
from pytemplate.service.calculator import Calculator


def main():

    first_operand, second_operand, action = list(input().split(","))

    first_operand, second_operand = int(first_operand), int(second_operand)

    action_func_dict = {
        "add": Calculator().add,
        "subtract": Calculator().subtract,
        "multiply": Calculator().multiply,
        "divide": Calculator().divide,
    }

    func = action_func_dict[action]

    operands = Operands(first_operand, second_operand)

    return func(operands)

from dataclasses import dataclass


@dataclass
class Operands:
    first_operand: int
    second_operand: int


def operands_factory(first_operand: int, second_operand: int) -> Operands:

    return Operands(first_operand, second_operand)


# class Operands:

#     def __init__(self, first_operand: int, second_operand: int):

#         self.__first_operand = set_value(first_operand, int)
#         self._second_operand = set_value(second_operand, int)

#     @property
#     def first_operand(self):
#         return self.__first_operand

#     @first_operand.setter
#     def first_operand(self, value):

#         if not isinstance(value, int):
#             raise ValueError("Operand must be Integer")

#         self.__first_operand = value

#     @property
#     def second_operand(self):
#         return self._second_operand

#     @second_operand.setter
#     def second_operand(self, value):

#         if not isinstance(value, int):
#             raise ValueError("Operand must be Integer")

#         self.second_operand = value

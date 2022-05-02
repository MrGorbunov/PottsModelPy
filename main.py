import random
from typing import Tuple, List
from copy import deepcopy as cp

from expression import *
from matrix_utils import *
from states import get_states
from test import TestExpression
from partial_ordering import *
from functools import reduce
from poly_utils import *


def main():
    x = Gam()
    x *= 4
    print(x)
    # TestExpression()

    # print(yun_factorization([one_rational, [2, 1], one_rational]))

    # print(get_states(3))
    # for row in generate_transition_matrix(3):
    #     print(" | ".join(fmt_REsum(f) for f in row))
    # for row in generate_transition_matrix(3):
    #     print(fmt_REsum(reduce(add_REsum, row)))
    #
    # print("\n".join(map(str, get_max_partial_ordering(3))))

    # TestExpression()

if __name__ == "__main__":
    main()

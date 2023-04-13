# Copyright 2023 Julien Peloton
# Author: Julien Peloton
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def add_numbers(num1: float, num2: float) -> float:
    """ Add two numbers

    Parameters
    ----------
    num1: numeric
        First number
    num2: numeric
        Second number

    Returns
    ----------
    out: numeric
        The sum of the two input numbers


    Examples
    ----------
    >>> add_numbers(1.0, 1.0)
    3.0
    """
    return num1 + num2


if __name__ == "__main__":
    """Run the unit test suite"""
    import doctest
    import sys

    sys.exit(doctest.testmod())  # type: ignore  # noqa

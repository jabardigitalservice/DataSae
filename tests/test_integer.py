import unittest
from datasae.integer import Integer
import pandas as pd
import numpy as np


class IntegerTest(unittest.TestCase):
    def __init__(self, methodName: str = "TestInteger") -> None:
        super().__init__(methodName)
        self.maxDiff = None

    def test_less_valid(self):
        dummy = pd.DataFrame(
            {
                "columm": np.random.randint(0, 10, 25),
            }
        )
        actual_result = Integer(dummy).less(10, "columm")
        excepted_result = {
            "score": 1,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }
        self.assertDictEqual(
            actual_result, excepted_result, "Result Not Match"
        )

    def test_less_invalid(self):
        dummy = pd.DataFrame(
            {
                "columm": np.random.randint(0, 10, 20),
            }
        )

        dummy = pd.concat(
            [
                dummy,
                pd.DataFrame(
                    [
                        {"columm": "11"},
                        {"columm": 44},
                        {"columm": 10.2},
                        {"columm": -1},
                    ]
                ),
            ]
        )

        actual_result = Integer(dummy).less(10, "columm")
        excepted_result = {
            "score": 0.875,
            "valid": 21,
            "invalid": 3,
            "warning": {
                20: {
                    "message": "Invalid Data Type",
                    "value": "11",
                    "detail_message": "Value must be of integer data type",
                },
                21: {
                    "message": "Invalid Value",
                    "value": 44,
                    "detail_message": "Value should be less then 10",
                },
                22: {
                    "message": "Invalid Data Type",
                    "value": 10.2,
                    "detail_message": "Value must be of integer data type",
                },
            },
        }

        self.assertDictEqual(
            actual_result, excepted_result, "Result Not Match"
        )


if __name__ == "__main__":
    unittest.main()

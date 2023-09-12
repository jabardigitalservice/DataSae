#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/


class Basic:
    def response(
        self,
        valid: int = 0,
        invalid: int = 0,
        warning: dict = None,
    ) -> dict:
        """
        Calculates a score based on the number of valid and invalid inputs.

        Args:
            valid (int, optional): The number of valid inputs. Defaults to 0.
            invalid (int, optional): The number of invalid inputs.
                Defaults to 0.
            warning (dict, optional): A dictionary containing any
                warning messages. Defaults to None.

        Returns:
            dict: A dictionary containing the calculated score,
                number of valid inputs, number of invalid inputs,
                and any warning messages.
        """
        score = valid / (invalid + valid) if valid + invalid != 0 else 0
        result = {
            "score": score,
            "valid": valid,
            "invalid": invalid,
            "warning": warning,
        }
        return result
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
        """_summary_

        Args:
            valid (int, optional): total valid. Defaults to 0.
            invalid (int, optional): total invalid. Defaults to 0.
            warning (dict, optional): warning response. Defaults to None.

        Returns:
            dict: result response
        """
        score = valid / (invalid + valid) if valid + invalid != 0 else 0
        result = {
            "score": score,
            "valid": valid,
            "invalid": invalid,
            "warning": warning,
        }
        return result

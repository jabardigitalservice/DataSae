#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""Utility library."""

from typing import Any


class Basic:
    """Basic class."""

    def response(
        self,
        valid: int = 0,
        invalid: int = 0,
        warning: dict = {}
    ) -> dict:
        """
        Response method.

        Calculates a score based on the number of valid and invalid inputs.

        Args:
            valid (int, optional): The number of valid inputs. Defaults to 0.
            invalid (int, optional): The number of invalid inputs.
                Defaults to 0.
            warning (dict, optional): A dictionary containing any
                warning messages. Defaults to {}.

        Returns:
            dict: A dictionary containing the calculated score,
                number of valid inputs, number of invalid inputs,
                and any warning messages.
        """
        score = valid / (invalid + valid) if valid + invalid != 0 else 0
        result = {
            'score': score,
            'valid': valid,
            'invalid': invalid,
            'warning': warning
        }
        return result


class WarningDataMessage:
    """WarningDataMessage class."""

    INVALID_VALUE: str = 'Invalid Value'
    INVALID_DATA_TYPE: str = 'Invalid Data Type'


def create_warning_data(
    value: Any,
    detail_message: str,
    message: str = WarningDataMessage.INVALID_VALUE
) -> dict:
    """
    Generate Standard Warning Data's value.

    Args:
        value (Any): The inputs.
        detail_message (str): Warning Detail Message.
        message (str, optional): Warning Message.
            Defaults to WarningDataMessage.INVALID_VALUE.

    Returns:
        dict: _description_
    """
    return {
        'message': message,
        'value': value,
        'detail_message': detail_message
    }

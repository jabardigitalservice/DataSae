<!--
Copyright (C) Free Software Foundation, Inc. All rights reserved.
Licensed under the AGPL-3.0-only License. See LICENSE in the project root
for license information.
-->

# DataSae Column's Function Based on Data Type

## Boolean

| File Location      | Description | Function |
|--------------------|-------------|----------|
| datasae/boolean.py | Is boolean | is_bool  |
| datasae/boolean.py | Is in      | is_in    |

## String

| File Location     | Description               | Function                 |
|-------------------|---------------------------|--------------------------|
| datasae/string.py | contain                   | contain                  |
| datasae/string.py | not contain               | not_contain              |
| datasae/string.py | regex contain             | regex_contain            |
| datasae/string.py | special character contain | special_char_contain     |
| datasae/string.py | is uppercase              | is_uppercase             |
| datasae/string.py | is lowercase              | is_lowecase              |
| datasae/string.py | is capitalize first word  | is_capitalize_first_word |
| datasae/string.py | is capitalize all word    | is_capitalize_all_word   |
| datasae/string.py | exact match               | exact                    |
| datasae/string.py | contain to multiple       | is_in_contain            |
| datasae/string.py | exact match to multiple   | is_in_exact              |

## Timestamp

| File Location        | Description        | Function           |
|----------------------|--------------------|--------------------|
| datasae/timestamp.py | equal              | equal_to           |
| datasae/timestamp.py | Less than          | less_than          |
| datasae/timestamp.py | less than equal    | less_than_equal    |
| datasae/timestamp.py | greater than       | greater_than       |
| datasae/timestamp.py | greater than equal | greater_than_equal |
| datasae/timestamp.py | in range           | in_range           |
| datasae/timestamp.py | is in              | is_in              |
| datasae/timestamp.py | not in             | not_in             |

## Integer

| File Location      | Description        | Function           |
|--------------------|--------------------|--------------------|
| datasae/integer.py | equal              | equal_to           |
| datasae/integer.py | Less than          | less_than          |
| datasae/integer.py | less than equal    | less_than_equal    |
| datasae/integer.py | greater than       | greater_than       |
| datasae/integer.py | greater than equal | greater_than_equal |
| datasae/integer.py | in range           | in_range           |
| datasae/integer.py | is in              | is_in              |
| datasae/integer.py | not in             | not_in             |
| datasae/integer.py | length             | length             |

## Float

| File Location    | Description        | Function           |
|------------------|--------------------|--------------------|
| datasae/float.py | equal              | equal_to           |
| datasae/float.py | Less than          | less_than          |
| datasae/float.py | less than equal    | less_than_equal    |
| datasae/float.py | greater than       | greater_than       |
| datasae/float.py | greater than equal | greater_than_equal |
| datasae/float.py | in range           | in_range           |
| datasae/float.py | is in              | is_in              |
| datasae/float.py | not in             | not_in             |
| datasae/float.py | length             | length             |

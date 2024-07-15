<!--
Copyright (C) Free Software Foundation, Inc. All rights reserved.
Licensed under the AGPL-3.0-only License. See LICENSE in the project root
for license information.
-->

<!-- markdownlint-disable MD033 -->

# DataSae Column's Function Based on Data Type

## Boolean

<table>
    <thead>
        <tr>
            <th rowspan=2>Function Name</th>
            <th colspan=3>Parameter</th>
            <th rowspan=2>Description</th>
        </tr>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Default</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <a href="https://jabardigitalservice.github.io/DataSae/boolean.html#datasae.boolean.Boolean.is_bool">is_bool</a>
            </td>
            <td>column</td>
            <td>String</td>
            <td></td>
            <td>is boolean</td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/boolean.html#datasae.boolean.Boolean.is_in">is_in</a>
            </td>
            <td>is_in</td>
            <td>List</td>
            <td></td>
            <td rowspan=2>is in</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
    </tbody>
</table>

## String

<table>
    <thead>
        <tr>
            <th rowspan=2>Function Name</th>
            <th colspan=3>Parameter</th>
            <th rowspan=2>Description</th>
        </tr>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Default</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/string.html#datasae.string.String.contain">contain</a>
            </td>
            <td>str_contain</td>
            <td>String</td>
            <td></td>
            <td rowspan=2>contain</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/string.html#datasae.string.String.not_contain">not_contain</a>
            </td>
            <td>str_not_contain</td>
            <td>String</td>
            <td></td>
            <td rowspan=2>not contain</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/string.html#datasae.string.String.regex_contain">regex_contain</a>
            </td>
            <td>regex_data</td>
            <td>String</td>
            <td></td>
            <td rowspan=2>regex contain</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/string.html#datasae.string.String.special_char_contain">special_char_contain</a>
            </td>
            <td>char</td>
            <td>String</td>
            <td></td>
            <td rowspan=2>special character contain</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td>
                <a href="https://jabardigitalservice.github.io/DataSae/string.html#datasae.string.String.is_uppercase">is_uppercase</a>
            </td>
            <td>column</td>
            <td>String</td>
            <td></td>
            <td>is uppercase</td>
        </tr>
        <tr>
            <td>
                <a href="https://jabardigitalservice.github.io/DataSae/string.html#datasae.string.String.is_lowecase">is_lowecase</a>
            </td>
            <td>column</td>
            <td>String</td>
            <td></td>
            <td>is lowercase</td>
        </tr>
        <tr>
            <td>
                <a href="https://jabardigitalservice.github.io/DataSae/string.html#datasae.string.String.is_capitalize_first_word">is_capitalize_first_word</a>
            </td>
            <td>column</td>
            <td>String</td>
            <td></td>
            <td>is capitalize first word</td>
        </tr>
        <tr>
            <td>
                <a href="https://jabardigitalservice.github.io/DataSae/string.html#datasae.string.String.is_capitalize_all_word">is_capitalize_all_word</a>
            </td>
            <td>column</td>
            <td>String</td>
            <td></td>
            <td>is capitalize all word</td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/string.html#datasae.string.String.exact">exact</a>
            </td>
            <td>str_exact</td>
            <td>String</td>
            <td></td>
            <td rowspan=2>exact match</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/string.html#datasae.string.String.is_in_contain">is_in_contain</a>
            </td>
            <td>str_is_in_contain</td>
            <td>List</td>
            <td></td>
            <td rowspan=2>contain to multiple</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/string.html#datasae.string.String.is_in_exact">is_in_exact</a>
            </td>
            <td>str_is_in_exact</td>
            <td>List</td>
            <td></td>
            <td rowspan=2>exact match to multiple</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
    </tbody>
</table>

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

<!-- markdownlint-enable MD033 -->

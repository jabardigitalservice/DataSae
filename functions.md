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
                <a href="https://jabardigitalservice.github.io/DataSae/timestamp.html#datasae.timestamp.Timestamp.equal_to">equal_to</a>
            </td>
            <td>value</td>
            <td>Datetime</td>
            <td></td>
            <td rowspan=2>equal</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/timestamp.html#datasae.timestamp.Timestamp.less_than">less_than</a>
            </td>
            <td>value</td>
            <td>Datetime</td>
            <td></td>
            <td rowspan=2>less than</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/timestamp.html#datasae.timestamp.Timestamp.less_than_equal">less_than_equal</a>
            </td>
            <td>value</td>
            <td>Datetime</td>
            <td></td>
            <td rowspan=2>less than equal</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/timestamp.html#datasae.timestamp.Timestamp.greater_than">greater_than</a>
            </td>
            <td>value</td>
            <td>Datetime</td>
            <td></td>
            <td rowspan=2>greater than</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/timestamp.html#datasae.timestamp.Timestamp.greater_than_equal">greater_than_equal</a>
            </td>
            <td>value</td>
            <td>Datetime</td>
            <td></td>
            <td rowspan=2>greater than equal</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=3>
                <a href="https://jabardigitalservice.github.io/DataSae/timestamp.html#datasae.timestamp.Timestamp.in_range">in_range</a>
            </td>
            <td>lower_limit</td>
            <td>Datetime</td>
            <td></td>
            <td rowspan=3>in range</td>
        </tr>
        <tr>
            <td>upper_limit</td>
            <td>Datetime</td>
            <td></td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/timestamp.html#datasae.timestamp.Timestamp.is_in">is_in</a>
            </td>
            <td>value</td>
            <td>List</td>
            <td></td>
            <td rowspan=2>is in</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/timestamp.html#datasae.timestamp.Timestamp.not_in">not_in</a>
            </td>
            <td>value</td>
            <td>List</td>
            <td></td>
            <td rowspan=2>not in</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
    </tbody>
</table>

## Float

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
                <a href="https://jabardigitalservice.github.io/DataSae/float.html#datasae.float.Float.equal_to">equal_to</a>
            </td>
            <td>value</td>
            <td>Float</td>
            <td></td>
            <td rowspan=2>equal</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/float.html#datasae.float.Float.less_than">less_than</a>
            </td>
            <td>value</td>
            <td>Float</td>
            <td></td>
            <td rowspan=2>less than</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/float.html#datasae.float.Float.less_than_equal">less_than_equal</a>
            </td>
            <td>value</td>
            <td>Float</td>
            <td></td>
            <td rowspan=2>less than equal</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/float.html#datasae.float.Float.greater_than">greater_than</a>
            </td>
            <td>value</td>
            <td>Float</td>
            <td></td>
            <td rowspan=2>greater than</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/float.html#datasae.float.Float.greater_than_equal">greater_than_equal</a>
            </td>
            <td>value</td>
            <td>Float</td>
            <td></td>
            <td rowspan=2>greater than equal</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=3>
                <a href="https://jabardigitalservice.github.io/DataSae/float.html#datasae.float.Float.in_range">in_range</a>
            </td>
            <td>lower_limit</td>
            <td>Float</td>
            <td></td>
            <td rowspan=3>in range</td>
        </tr>
        <tr>
            <td>upper_limit</td>
            <td>Float</td>
            <td></td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/float.html#datasae.float.Float.is_in">is_in</a>
            </td>
            <td>value</td>
            <td>List</td>
            <td></td>
            <td rowspan=2>is in</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/float.html#datasae.float.Float.not_in">not_in</a>
            </td>
            <td>value</td>
            <td>List</td>
            <td></td>
            <td rowspan=2>not in</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
    </tbody>
</table>

## Integer

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
                <a href="https://jabardigitalservice.github.io/DataSae/integer.html#datasae.integer.Integer.equal_to">equal_to</a>
            </td>
            <td>value</td>
            <td>Integer</td>
            <td></td>
            <td rowspan=2>equal</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/integer.html#datasae.integer.Integer.less_than">less_than</a>
            </td>
            <td>value</td>
            <td>Integer</td>
            <td></td>
            <td rowspan=2>less than</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/integer.html#datasae.integer.Integer.less_than_equal">less_than_equal</a>
            </td>
            <td>value</td>
            <td>Integer</td>
            <td></td>
            <td rowspan=2>less than equal</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/integer.html#datasae.integer.Integer.greater_than">greater_than</a>
            </td>
            <td>value</td>
            <td>Integer</td>
            <td></td>
            <td rowspan=2>greater than</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/integer.html#datasae.integer.Integer.greater_than_equal">greater_than_equal</a>
            </td>
            <td>value</td>
            <td>Integer</td>
            <td></td>
            <td rowspan=2>greater than equal</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=3>
                <a href="https://jabardigitalservice.github.io/DataSae/integer.html#datasae.integer.Integer.in_range">in_range</a>
            </td>
            <td>lower_limit</td>
            <td>Integer</td>
            <td></td>
            <td rowspan=3>in range</td>
        </tr>
        <tr>
            <td>upper_limit</td>
            <td>Integer</td>
            <td></td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/integer.html#datasae.integer.Integer.is_in">is_in</a>
            </td>
            <td>value</td>
            <td>List</td>
            <td></td>
            <td rowspan=2>is in</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/integer.html#datasae.integer.Integer.not_in">not_in</a>
            </td>
            <td>value</td>
            <td>List</td>
            <td></td>
            <td rowspan=2>not in</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=2>
                <a href="https://jabardigitalservice.github.io/DataSae/integer.html#datasae.integer.Integer.length">length</a>
            </td>
            <td>value</td>
            <td>integer</td>
            <td></td>
            <td rowspan=2>length</td>
        </tr>
        <tr>
            <td>column</td>
            <td>String</td>
            <td></td>
        </tr>
    </tbody>
</table>

<!-- markdownlint-enable MD033 -->

"""
Masih yang hanya untuk dataframe

"""
import json
import pandas as pd



class Completeness:
    def __init__(self, data: pd.DataFrame, table_name: str):
        self.result = []
        self.quality_column = {
            'table_name': str,
            'column_name': str,
            'completeness_type': str,
            'total_rows': int,
            'total_quality_rows': int,
            'data_percentage': float
        }
        self.data = data
        self.quality_column['table_name'] = table_name
        self.quality_column['column_name'] = data.columns.values.tolist()
        self.quality_column['total_rows'] = len(self.data.index)

    def check_empty_value(self):
        self.quality_column['completeness_type'] = 'non_empty_value'
        # check all cells yang valuenya empty or '' or just only space
        null_data = self.data.isnull().value_counts()
        print(null_data)
        return null_data[True]
"""
Masih yang hanya untuk dataframe

"""
import pandas as pd



class Completeness:
    def __init__(self, data: pd.DataFrame, table_name: str):
        self.result = {
            'table_name': str,
            'column_name': str,
            'completeness_type': str,
            'total_rows': int,
            'total_cells': int,
            'total_quality_cells': int,
            'data_percentage': float
        }
        self.data = data
        self.result['table_name'] = table_name
        self.result['column_name'] = data.columns.values.tolist()
        self.result['total_rows'] = len(self.data.index)
        self.result['total_cells'] = len(self.data.index) * len(self.result['column_name'])

    def custom_rules (self) :
        # yg '' atau space doang dan yang lainnya
        self.data = self.data.apply(lambda x: x.str.strip())

        try :
            return self.data.value_counts()['']
        except :
            return 0

    def check_empty_value(self):
        self.result['completeness_type'] = 'non_empty_value'
        # self.result['result'] = self.data.isnull().value_counts()
        # baru yg na
        self.result['total_quality_cells'] = self.data.count()[0]
        self.result['total_quality_cells'] = self.result['total_quality_cells'] - self.custom_rules()
        self.result['data_percentage'] = (self.result['total_quality_cells'] / self.result['total_cells']) * 100

        return self.result
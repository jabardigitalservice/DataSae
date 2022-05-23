"""
Masih yang hanya untuk dataframe

"""
import pandas as pd



class Uniqueness:
    def __init__(self, data: pd.DataFrame, table_name: str):
        self.result = {
            'table_name': str,
            'column_name': str,
            'uniqueness_type': str,
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
        return 0

    def check_duplicate_row(self):
        self.result['uniqueness_type'] = 'non_duplicate_row'

        column_true = []
        for c in self.result['column_name']:
            self.data[c] = self.data[c].apply(lambda x: x.lower() if (isinstance(x, str)) else x)
            self.data[c] = self.data[c].apply(lambda x: x.strip() if (isinstance(x, str)) else x)
            column_true.append(True)

        # get number rows duplicate
        rows_duplicate = self.data.loc[self.data.duplicated()].isin([True]).index.tolist()
        duplicate_unique = self.data.loc[rows_duplicate].drop_duplicates().values.tolist()
        print(duplicate_unique)

        count_duplicate = 0
        for dup in duplicate_unique:
            is_duplicate_lists = self.data.isin(dup).isin(column_true).values.tolist()
            count_duplicate = count_duplicate + len(list(filter(lambda x: x == column_true, is_duplicate_lists)))
        print(count_duplicate)

        self.result['total_quality_cells'] = (self.result['total_rows'] - count_duplicate) * len(self.result['column_name'])
        self.result['total_quality_cells'] = self.result['total_quality_cells'] - self.custom_rules()
        self.result['data_percentage'] = (self.result['total_quality_cells'] / self.result['total_cells']) * 100

        return self.result
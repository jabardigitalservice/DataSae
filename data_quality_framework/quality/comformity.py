"""
Masih yang hanya untuk dataframe

"""
import pandas as pd
from data_quality_framework.connection.postgresql import Connection

class Comformity:
    def __init__(self, data: pd.DataFrame, table_name: str, description: str):
        self.result = {
            'table_name': str,
            'column_name': str,
            'comformity_type': str,
            'total_rows': int,
            'total_cells': int,
            'total_quality_column_name': int,
            'data_percentage': float
        }
        self.data = data
        self.result['table_name'] = table_name
        self.result['column_name'] = data.columns.values.tolist()
        self.result['total_rows'] = len(self.data.index)
        self.result['total_cells'] = len(self.data.index) * len(self.result['column_name'])
        self.result['description'] = description

    def custom_rules (self) :
        return 0

    def kolom_dalam_deskripsi (self):
        total_failed = 0
        for k in self.result['column_name']:
            if k.lower().replace('_',' ').strip() not in self.result['description'].lower().replace('_',' ').strip() and k.lower() != 'id':
                print('==== tidak ada dalam deskripsi : {}'.format(k.lower()))
                total_failed=total_failed+1

        self.result['total_quality_column_name'] = len(self.result['column_name']) - total_failed
        self.result['data_percentage'] = (self.result['total_quality_column_name'] / len(self.result['column_name'])) * 100
        self.result['comformity_type'] = 'kolom_dalam_deskripsi'
        
        return self.result

    def dataset_sesuai_judul(self):
        total_same = 0
        for k in self.result['column_name']:
            if k.lower().strip().replace('_', ' ') in self.result['table_name'].lower().replace('_', ' ').strip():
                total_same = total_same + 1

        self.result['total_quality_column_name'] = total_same
        # nanti mah di tokenize di judul, pengukuran dataset yang masuk kolomnya segimana
        if total_same > 0:
            self.result['data_percentage'] = 100
        else:
            self.result['data_percentage'] = 0
        self.result['comformity_type'] = 'dataset_sesuai_judul'

        return self.result

    def kolom_dalam_baris_data(self):
        return self.result

    def tingkat_penyajian_sesuai_judul(self):
        return self.result

    def cakupan_dataset_sesuai_judul(self):
        return self.result
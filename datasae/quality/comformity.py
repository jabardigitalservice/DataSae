import pandas as pd
import simplejson as json
from claming import Matching
from nltk.tokenize import RegexpTokenizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


class Comformity:
    def __init__(
        self,
        data: pd.DataFrame,
        title: str,
        description: str,
        tag: list,
        metadata: dict,
    ):
        self.data = data.copy()
        self.title = title
        self.description = description
        self.tag = tag
        self.metadata = metadata

    def comformity(
        self,
        comformity_explain_columns: float = 40,
        comformity_measurement: float = 20,
        comformity_serving_rate: float = 20,
        comformity_scope: float = 20
    ):
        comformity_explain_columns = comformity_explain_columns / 100
        comformity_measurement = comformity_measurement / 100
        comformity_serving_rate = comformity_serving_rate / 100
        comformity_scope = comformity_scope / 100

        quality_result = {
            'comformity_explain_columns': self.comformity_explain_columns(),
            'comformity_measurement': self.comformity_measurement(),
            'comformity_serving_rate': self.comformity_serving_rate(),
            'comformity_scope': self.comformity_scope()
        }
        final_result = (comformity_explain_columns * quality_result['comformity_explain_columns']['quality_result']) + \
            (comformity_measurement * quality_result['comformity_measurement']['quality_result']) + \
            (comformity_serving_rate * quality_result['comformity_serving_rate']['quality_result']) + \
            (comformity_scope * quality_result['comformity_scope']['quality_result'])
        quality_result['comformity_result'] = final_result
        return quality_result

    @staticmethod
    def generate_report(
        total_rows: int,
        total_columns: int,
        total_valid: int,
        total_not_valid: int,
        data_not_valid: list
    ):
        quality_result = {
            'total_rows': total_rows if total_rows is not None else None,
            'total_columns': total_columns if total_columns is not None else None,
            'total_cells': total_rows * total_columns if total_rows is not None and total_columns is not None else None,
            'total_valid': total_valid if total_valid is not None else None,
            'total_not_valid': total_not_valid if total_not_valid is not None else None,
            'warning': data_not_valid if data_not_valid is not None else None,
            'quality_result': (((total_valid / total_columns) * 100)) if total_valid is not None else None
        }
        quality_result = json.loads(json.dumps(quality_result, ignore_nan=True))
        return quality_result

    @staticmethod
    def cleansing_text(text):
        text = str.lower(text)
        tokenizer = RegexpTokenizer(r'\w+')
        text = tokenizer.tokenize(text)
        stemmer = StemmerFactory().create_stemmer()
        text = stemmer.stem(str(text))
        return text

    @staticmethod
    def matching_text(text1, text2):
        match = Matching()
        result = match.part_levenshtein_match(
            text1,
            text2
        )
        result = result['score'] / result['max_score']
        result = 1.0 if result > 0.5 else 0
        return result

    def comformity_explain_columns(self):
        dataframe = self.data.copy()
        description = self.description
        columns_valid = []
        columns_not_valid = []
        columns = dataframe.columns.tolist()
        columns.remove('id')
        [
            columns_valid.append(column) if column in description else columns_not_valid.append(column)
            for column in columns
        ]
        total_valid = len(columns_valid)
        total_not_valid = len(columns_not_valid)
        total_rows = len(dataframe.index)
        total_columns = len(columns)
        quality_result = self.generate_report(
            total_rows,
            total_columns,
            total_valid,
            total_not_valid,
            columns_not_valid
        )
        return quality_result

    def comformity_measurement(self):
        dataframe = self.data.copy()
        title = self.cleansing_text(self.title)
        pengukuran_dataset = self.cleansing_text(self.metadata['pengukuran_dataset'])
        # must_word = [
        #     'jumlah',
        #     'persentase',
        #     'daftar',
        #     'indeks',
        #     'tingkat',
        #     'angka',
        #     'jarak',
        #     'lebar',
        #     'luas',
        #     'nilai',
        #     'panjang',
        #     'pertumbuhan',
        #     'populasi',
        #     'produksi',
        #     'rasio',
        #     'rata-rata',
        #     'volume'
        # ]
        hasil = self.matching_text(pengukuran_dataset, title)
        total_rows = len(dataframe.index)
        total_columns = len(dataframe.columns)
        total_valid = 1 if hasil == 1.0 else 0
        total_not_valid = 0 if hasil == 1.0 else 1
        data_not_valid = None
        quality_result = {
            'total_rows': total_rows if total_rows is not None else None,
            'total_columns': total_columns if total_columns is not None else None,
            'total_cells': total_rows * total_columns if total_rows is not None and total_columns is not None else None,
            'total_valid': total_valid if total_valid is not None else None,
            'total_not_valid': total_not_valid if total_not_valid is not None else None,
            'warning': data_not_valid if data_not_valid is not None else None,
            'quality_result': ((float(total_valid) * 100)) if total_valid is not None else None
        }
        quality_result = json.loads(json.dumps(quality_result, ignore_nan=True))
        return quality_result

    def comformity_serving_rate(self):
        dataframe = self.data.copy()
        title = self.cleansing_text(self.title)
        tingkat_penyajian_dataset = self.cleansing_text(self.metadata['tingkat_penyajian_dataset'])
        # must_word = [
        #     'jumlah',
        #     'persentase',
        #     'daftar',
        #     'indeks',
        #     'tingkat',
        #     'angka',
        #     'jarak',
        #     'lebar',
        #     'luas',
        #     'nilai',
        #     'panjang',
        #     'pertumbuhan',
        #     'populasi',
        #     'produksi',
        #     'rasio',
        #     'rata-rata',
        #     'volume'
        # ]
        hasil = self.matching_text(tingkat_penyajian_dataset, title)
        total_rows = len(dataframe.index)
        total_columns = len(dataframe.columns)
        total_valid = 1 if hasil == 1.0 else 0
        total_not_valid = 0 if hasil == 1.0 else 1
        data_not_valid = None
        quality_result = {
            'total_rows': total_rows if total_rows is not None else None,
            'total_columns': total_columns if total_columns is not None else None,
            'total_cells': total_rows * total_columns if total_rows is not None and total_columns is not None else None,
            'total_valid': total_valid if total_valid is not None else None,
            'total_not_valid': total_not_valid if total_not_valid is not None else None,
            'warning': data_not_valid if data_not_valid is not None else None,
            'quality_result': ((float(total_valid) * 100)) if total_valid is not None else None
        }
        return quality_result

    def comformity_scope(self):
        dataframe = self.data.copy()
        title = self.cleansing_text(self.title)
        cakupan_dataset = self.cleansing_text(self.metadata['cakupan_dataset'])
        # must_word = [
        #     'jumlah',
        #     'persentase',
        #     'daftar',
        #     'indeks',
        #     'tingkat',
        #     'angka',
        #     'jarak',
        #     'lebar',
        #     'luas',
        #     'nilai',
        #     'panjang',
        #     'pertumbuhan',
        #     'populasi',
        #     'produksi',
        #     'rasio',
        #     'rata-rata',
        #     'volume'
        # ]
        hasil = self.matching_text(cakupan_dataset, title)
        total_rows = len(dataframe.index)
        total_columns = len(dataframe.columns)
        total_valid = 1 if hasil == 1.0 else 0
        total_not_valid = 0 if hasil == 1.0 else 1
        data_not_valid = None
        quality_result = {
            'total_rows': total_rows if total_rows is not None else None,
            'total_columns': total_columns if total_columns is not None else None,
            'total_cells': total_rows * total_columns if total_rows is not None and total_columns is not None else None,
            'total_valid': total_valid if total_valid is not None else None,
            'total_not_valid': total_not_valid if total_not_valid is not None else None,
            'warning': data_not_valid if data_not_valid is not None else None,
            'quality_result': ((float(total_valid) * 100)) if total_valid is not None else None
        }
        return quality_result

from difflib import SequenceMatcher

import pandas as pd
import simplejson as json
from claming import Matching
from nltk.tokenize import RegexpTokenizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


class Comformity:
    """
    class comformity
    """

    def __init__(
            self,
            data: pd.DataFrame,
            title: str,
            description: str,
            tag: list,
            metadata: dict,
            category: str
    ):
        self.data = data.copy()
        self.title = title
        self.description = description
        self.tag = tag
        self.metadata = metadata
        self.category = category

    def comformity(
            self,
            comformity_explain_columns: float = 40,
            comformity_measurement: float = 20,
            comformity_serving_rate: float = 20,
            comformity_scope: float = 20
    ):
        """

        :param comformity_explain_columns:
        :param comformity_measurement:
        :param comformity_serving_rate:
        :param comformity_scope:
        :return:
        """
        comformity_explain_columns = comformity_explain_columns / 100
        comformity_measurement = comformity_measurement / 100
        comformity_serving_rate = comformity_serving_rate / 100
        comformity_scope = comformity_scope / 100

        quality_result = {
            'comformity_explain_columns': self.comformity_explain_columns(),
            'comformity_measurement': self.comformity_measurement(),
            'comformity_serving_rate': self.comformity_serving_rate(),
            'comformity_scope': self.comformity_scope()
            # 'comformity_check_warning': self.comformity_check_warning()
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
        """

        :param total_rows:
        :param total_columns:
        :param total_valid:
        :param total_not_valid:
        :param data_not_valid:
        :return:
        """
        quality_result = {
            'total_rows': total_rows if total_rows is not None else None,
            'total_columns': total_columns if total_columns is not None else None,
            'total_cells': total_rows * total_columns if total_rows is not None and total_columns is not None else None,
            'total_valid': total_valid if total_valid is not None else None,
            'total_not_valid': total_not_valid if total_not_valid is not None else None,
            'warning': data_not_valid if data_not_valid is not None else None,
            'quality_result': ((total_valid / total_columns) * 100) if total_valid is not None else None
        }
        quality_result = json.loads(json.dumps(quality_result, ignore_nan=True))
        return quality_result

    @staticmethod
    def cleansing_text(text):
        """

        :param text:
        :return:
        """
        text = str.lower(text)
        tokenizer = RegexpTokenizer(r'\w+')
        text = tokenizer.tokenize(text)
        stemmer = StemmerFactory().create_stemmer()
        text = stemmer.stem(str(text))
        return text

    @staticmethod
    def matching_text(text1, text2):
        """

        :param text1:
        :param text2:
        :return:
        """
        match = Matching()
        result = match.part_levenshtein_match(
            text1,
            text2
        )
        result = result['score'] / result['max_score']
        result = 1.0 if result > 0.5 else 0
        return result

    def comformity_explain_columns(self):
        """

        :return:
        """
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
        """

        :return:
        """
        dataframe = self.data.copy()
        title = self.cleansing_text(self.title)
        pengukuran_dataset = self.cleansing_text(self.metadata['pengukuran_dataset'])
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
            'quality_result': (float(total_valid) * 100) if total_valid is not None else None
        }
        quality_result = json.loads(json.dumps(quality_result, ignore_nan=True))
        return quality_result

    def comformity_serving_rate(self):
        """

        :return:
        """
        dataframe = self.data.copy()
        title = self.cleansing_text(self.title)
        tingkat_penyajian_dataset = self.cleansing_text(self.metadata['tingkat_penyajian_dataset'])
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
            'quality_result': (float(total_valid) * 100) if total_valid is not None else None
        }
        return quality_result

    def comformity_scope(self):
        """

        :return:
        """
        dataframe = self.data.copy()
        title = self.cleansing_text(self.title)
        cakupan_dataset = self.cleansing_text(self.metadata['cakupan_dataset'])
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
            'quality_result': (float(total_valid) * 100) if total_valid is not None else None
        }
        return quality_result

    def comformity_check_warning(self):
        """

        :return:
        """
        dataframe = self.data.copy()
        # dimensi
        try:
            dimensi_dataset_from_dataset = dataframe['tahun'].drop_duplicates().sort_values().to_list()
        except Exception as e:
            print(e)
            dimensi_dataset_from_dataset = None
        try:
            dimensi_dataset_awal = int(self.metadata['dimensi_dataset_awal'])
        except Exception as e:
            print(e)
            dimensi_dataset_awal = None
        try:
            dimensi_dataset_akhir = int(self.metadata['dimensi_dataset_akhir'])
        except Exception as e:
            print(e)
            dimensi_dataset_akhir = None

        print('{} == {}'.format(dimensi_dataset_awal, dimensi_dataset_akhir))
        warning = []
        if dimensi_dataset_awal is not None:
            data_from_metadata = []
            for i in range(dimensi_dataset_awal, dimensi_dataset_akhir + 1):
                data_from_metadata.append(i)
            print(data_from_metadata)

            # cast to int
            data_from_db = []
            for d in dimensi_dataset_from_dataset:
                try:
                    data_from_db.append(int(d))
                except Exception as e:
                    print(e)
            if data_from_metadata != data_from_db:
                warning.append('WARNING : dimensi tahun pada metadata dan dataset berbeda')
        else:
            warning.append('WARNING : dimensi pada metadata kosong')

        # satuan
        try:
            satuan_dataset_from_dataset = dataframe['satuan'].drop_duplicates().sort_values().to_list()[0].lower()
        except Exception as e:
            print(e)
            satuan_dataset_from_dataset = None
        try:
            satuan_dataset_from_metadata = self.metadata['satuan_dataset']
        except Exception as e:
            print(e)
            satuan_dataset_from_metadata = None

        print('{} == {}'.format(satuan_dataset_from_metadata, satuan_dataset_from_dataset))
        warning = []
        if satuan_dataset_from_metadata is not None:
            if SequenceMatcher(None, satuan_dataset_from_metadata.lower(),
                               satuan_dataset_from_dataset.lower()).ratio() < 0.7:
                warning.append('WARNING : satuan dataset pada metadata dan dataset berbeda')
        else:
            warning.append('WARNING : satuan pada metadata kosong')

        # tag mengandung kata pengukuran atau topik
        judul = self.title.lower().replace(' ', '_')
        is_tag_topik = False
        ratio = 0
        for d in self.tag:
            d = d.lower().replace(' ', '_')
            if SequenceMatcher(None, judul, d).ratio() > ratio:
                ratio = SequenceMatcher(None, judul, d).ratio()
            if d in judul or ratio > 0.5:
                is_tag_topik = True

        warning = []
        if is_tag_topik is False:
            warning.append('WARNING : tag dataset tidak mengandung topik atau pengukuran')

        # tag kategori
        kategori = self.category.lower().replace(' ', '_')
        is_tag_kategori = False
        ratio = 0
        for d in self.tag:
            d = d.lower().replace(' ', '_')
            if SequenceMatcher(None, kategori, d).ratio() > ratio:
                ratio = SequenceMatcher(None, kategori, d).ratio()
        if kategori in self.tag or ratio > 0.8:
            is_tag_kategori = True

        warning = []
        if is_tag_kategori is False:
            warning.append('WARNING : tag dataset tidak mengandung kategori')

        total_rows = len(dataframe.index)
        total_columns = len(dataframe.columns)
        total_valid = 1
        total_not_valid = 0
        quality_result = {
            'total_rows': total_rows if total_rows is not None else None,
            'total_columns': total_columns if total_columns is not None else None,
            'total_cells': total_rows * total_columns if total_rows is not None and total_columns is not None else None,
            'total_valid': total_valid if total_valid is not None else None,
            'total_not_valid': total_not_valid if total_not_valid is not None else None,
            'warning': warning,
            'quality_result': (float(total_valid) * 100) if total_valid is not None else None
        }

        return quality_result

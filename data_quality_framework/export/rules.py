# exporting all rules result of data quality checking into json.
# from data_quality_framework.quality.completeness import Completeness

import json

class Rules:
    """
        A class to represent collecting all rules (represent by function/method) and transform them into json

        ...

        Attributes
        ----------

        Methods
        -------
        result_to_rules_completeness():
            return json rules of completeness
        result_to_rules_comformity():
            return json rules of comformity
        result_to_rules_uniqueness():
            return json rules of uniqueness

    """
    def __init__(self):
        self.rule = {
            'rules_name' : str,
            'rules_subname_and_function' : dict,
            'columns_involved' : str
        }

    def result_to_rules_completeness (self):
        self.rule['rules_name'] = 'completeness'
        self.rule['rules_subname_and_function'] = {'check_empty_value' : 'data_quality_framework.quality.completeness.Completeness().check_empty_value()'}
        self.rule['columns_involved'] = 'all'

        return self.rule

    def result_to_rules_comformity (self):
        self.rule['rules_name'] = 'comformity'
        self.rule['rules_subname_and_function'] = {
            'pengukuran_dataset_check': 'data_quality_framework.quality.comformity.Comformity().pengukuran_dataset_check()',
            'pengukuran_dataset_sesuai_judul': 'data_quality_framework.quality.comformity.Comformity().pengukuran_dataset_sesuai_judul()',
            'tingkat_penyajian_sesuai_judul': 'data_quality_framework.quality.comformity.Comformity().tingkat_penyajian_sesuai_judul()',
            'cakupan_dataset_sesuai_judul': 'data_quality_framework.quality.comformity.Comformity().cakupan_dataset_sesuai_judul()',

        }
        self.rule['columns_involved'] = 'all'

        return self.rule

    def result_to_rules_uniqueness(self):
        self.rule['rules_name'] = 'uniqueness'
        self.rule['rules_subname_and_function'] = {
            'non_duplicate_row': 'data_quality_framework.quality.uniqueness.Uniqueness().check_duplicate_row()'}
        self.rule['columns_involved'] = 'all'

        return self.rule
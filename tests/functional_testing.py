# import pandas
# from connection.google import GoogleSheet
# from quality.uniqueness import Uniqueness
#
# def check_completeness (dataframe) :
#     # connection_sheet = GoogleSheet('https://docs.google.com/spreadsheets/d/1cx8z0I2xJNPaMSmxU_gzujwjH0fkY8COty_d83_ywxE/',
#     #                                    'MASTER DATA')


# fungsional test completeness check
import unittest, pandas
from data_quality_framework.quality.completeness import Completeness
from data_quality_framework.quality.uniqueness import Uniqueness

class TestQualityMethods(unittest.TestCase):

    def test_completeness(self):
        true_result =  {
            'table_name': 'sampling table',
            'column_name': [0],
            'completeness_type': 'non_empty_value',
            'total_rows': 8,
            'total_cells': 8,
            'total_quality_cells': 6,
            'data_percentage': 75.0
        }
        input = ['Geeks', 'For', 'Geeks', 'is','portal', 'for', None, '     \n']
        data = pandas.DataFrame(input)
        empty_value = Completeness(data, 'sampling table').check_empty_value()

        self.assertEqual(empty_value, true_result)
        # ini untuk test error
        # with self.assertRaises(TypeError):
        #     empty_value

    def test_uniqueness (self):
        true_result = {
            'table_name': 'test_df',
            'column_name': [0,1],
            'completeness_type': 'non_duplicate_row',
            'total_rows': 7,
            'total_cells': 14,
            'total_quality_cells': 4,
            'data_percentage': 28.57142857142857
        }
        lst = [['FOR', 1], ['Geeks', 1], ['Geeks', 1], ['geeks', 1122], ['for', 1], ['geeks', 1], [None, '     \n']]
        data = pandas.DataFrame(lst)
        test = Uniqueness(data, 'test_df')
        print(test.check_duplicate_row())

if __name__ == '__main__':
    unittest.main()
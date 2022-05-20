# fungsional test completeness check
import unittest, pandas
from data_quality_framework.quality.completeness import Completeness

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

if __name__ == '__main__':
    unittest.main()
# fungsional test completeness check
import unittest, pandas
from data_quality_framework.quality.completeness import Completeness
from data_quality_framework.quality.uniqueness import Uniqueness
from data_quality_framework.connection.postgresql import Connection
from data_quality_framework.quality.comformity import Comformity

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
            'uniqueness_type': 'non_duplicate_row',
            'total_rows': 7,
            'total_cells': 14,
            'total_quality_cells': 4,
            'data_percentage': 28.57142857142857
        }
        lst = [['FOR', 1], ['Geeks', 1], ['Geeks', 1], ['geeks', 1122], ['for', 1], ['geeks', 1], [None, '     \n']]
        data = pandas.DataFrame(lst)
        test = Uniqueness(data, 'test_df')
        print(test.check_duplicate_row())
        self.assertEqual(test.check_duplicate_row(), true_result)

    def test_connection(self):

        engine = Connection('satudata').get_engine()
        query = '''SELECT dataset_type_id, sektoral_id, kode_skpd, kode_skpdsub, kode_skpdunit, app_id, app_service_id, name,
                title, "year", image, description, "owner", owner_email, maintainer, maintainer_email, notes, cuid, cdate, is_active,
                is_deleted, dataset_class_id, regional_id, id, muid, mdate, count_column, count_row, count_view, count_access, license_id,
                count_rating, is_permanent, is_validate, count_share_fb, count_share_tw, count_share_wa, count_share_link,
                count_download_xls, count_download_csv, count_download_api, is_realtime, count_view_private, count_access_private,
                count_download_xls_private, count_download_csv_private, count_download_api_private, "schema", "table", json, category,
                "period"
                FROM public.dataset where is_active = true and is_deleted = false  limit 10'''
        dataset = pandas.read_sql(con=engine, sql=query)
        engine_data = Connection('bigdata').get_engine()

        for index, row in dataset.iterrows():
            try:
                query = '''select * from "{}".{} limit 2;'''.format(row['schema'], row['table'])
                data = pandas.read_sql(con=engine_data, sql=query)
                test = Comformity(data, row['title'], row['description'])
                # persen = test.kolom_dalam_deskripsi()['data_percentage']
                result = test.dataset_sesuai_judul()
                if result['data_percentage'] == 100:
                    print(row['title'])
                    print(result['data_percentage'])
                    print(result['column_name'])
                    # print(row['description'])

            except Exception as e:
                print('')

        engine.dispose()
        engine_data.dispose()

if __name__ == '__main__':
    unittest.main()
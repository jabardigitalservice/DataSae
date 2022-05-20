# import pandas
# from connection.google import GoogleSheet
# from quality.completeness import Completeness
#
# def check_completeness (dataframe) :
#     # connection_sheet = GoogleSheet('https://docs.google.com/spreadsheets/d/1cx8z0I2xJNPaMSmxU_gzujwjH0fkY8COty_d83_ywxE/',
#     #                                    'MASTER DATA')
#     # data = connection_sheet.transform_to_dataframe()
#     lst = ['Geeks', 'For', 'Geeks', 'is','portal', 'for', None, '     \n']
#     data = pandas.DataFrame(lst)
#     empty_value = Completeness(data, 'sampling table').check_empty_value()
#
#     return empty_value
#
# print(check_completeness(None))
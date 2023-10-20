import gspread
import pandas as pd


from . import (
    CLIENT_SECRET_FILE,
    get_google_service)


def get_data_spreadsheet(
    sheet_name: str = 'Kantor Desa Cianjur',
    link_sheet: str = '1uC6sV-4RHqqmtPUN7yPU1jRTF87ipd3Kol8Zf8p6g5s',
    client_secret_file: str = CLIENT_SECRET_FILE
):
    _, creds = get_google_service(client_secret_file)
    data = gspread.authorize(creds).open_by_key(
            link_sheet).worksheet(sheet_name)
    
    # default index 0 jadi kolom
    data1 = data.get_all_records()
    data2 = pd.DataFrame(data1)

    print(data2)
    return data2

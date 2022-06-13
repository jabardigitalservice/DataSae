import pandas as pd, json
from datasae import Consistency

# name_file = 'distanhor-od_15762_luas_panen_sayuran_buah_buahan_semusim_sbs__komoditi_data.csv'
# column_name = 'luas_panen'
# column_satuan = 'satuan'
# satuan = ['HEKTAR']
# time_series_type = 'years'
# column_time_series = 'tahun'

# name_file = 'diskominfo-od_17141_jml_pemantauan_bedasarkan_klasifikasi_di_jabar_saber_h_data.csv'
# column_name = 'jumlah_pemantauan'
# column_satuan = 'satuan'
# satuan = ['PEMANTAUAN']
# time_series_type = 'years'
# column_time_series = 'tahun'

name_file = 'disbmpr-od_16339_lebar_rata_rata_ruas_jalan_berdasarkan_nama_jalan_data.csv'
column_name = 'lebar_rata_rata'
column_satuan = 'satuan'
satuan = ['KILOMETER']
time_series_type = 'years'
column_time_series = 'tahun'

raw_data = pd.read_csv(name_file)
consistency = Consistency(data=raw_data, column_name=column_name, column_satuan=column_satuan, satuan=satuan, time_series_type=time_series_type, column_time_series=column_time_series)
result_consistency = consistency.check_consistency()
print(json.dumps(result_consistency, indent=4, sort_keys=False))
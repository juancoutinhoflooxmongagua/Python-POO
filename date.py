from datetime import datetime

data_str_data = "2022/04/20 07:49:23"
data_str_data = "20/04/2022"
data_str_fmt = "%d/%m/%Y"

dat = datetime.now()
# data = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)
print(dat)

import pandas as pd 
import numpy as np

dulieu = pd.read_csv(r'C:\Users\Admin\Desktop\NMHS\TH-BUOI1\1.csv')
#3
print(dulieu.head(10))
print(dulieu.tail(10))
#4
df= dulieu.fillna(0, inplace= False)
#5
print(dulieu['T1'].fillna(dulieu['T1'].mean(), inplace=False))

#7
for i in ["1", "2", "6"]: 
    print("TBM"+i)

# Tính toán TBM cho từng năm lớp và thêm vào DataFrame dulieu
for i in ["1", "2", "6"]:
    dulieu["TBM"+i] = ((dulieu["T"+i]*2 + dulieu["L"+i] + dulieu["H"+i] + dulieu["S"+i] + dulieu["V"+i]*2 + dulieu["X"+i] + dulieu["D"+i] + dulieu["N"+i]) / 10)

# Đổi tên cột TBM6 thành TBM3
dulieu.rename(columns={"TBM6": "TBM3"}, inplace=True)

# Lưu DataFrame dulieu vào file CSV
dulieu.to_csv('1.csv', index=False)

# 8. Tạo các biến xếp loại XL1, XL2, XL3
def xep_loai(TBM):
    if TBM < 5.0:
        return 'Y'
    elif 5.0 <= TBM < 6.5:
        return 'TB'
    elif 6.5 <= TBM < 8.0:
        return 'K'
    elif 8.0 <= TBM < 9.0:
        return 'G'
    else:
        return 'XS'

df['XL1'] = df['TBM1'].apply(xep_loai)
df['XL2'] = df['TBM2'].apply(xep_loai)
df['XL3'] = df['TBM3'].apply(xep_loai)

# Lưu DataFrame vào cùng một file CSV
df.to_csv('1.csv', index=False)
 #9
def min_max_normalization(x):
    return (x - x.min()) / (x.max() - x.min())

dulieu['US_TBM1'] = min_max_normalization(dulieu['TBM1'])
dulieu['US_TBM2'] = min_max_normalization(dulieu['TBM2'])
dulieu['US_TBM3'] = min_max_normalization(dulieu['TBM3'])

# 10. Tạo biến kết quả xét tuyển KQXT
def kqxt(row):
    if row['KT'] in ['A', 'A1']:
        return 1 if ((row['DH1']*2 + row['DH2'] + row['DH3']) / 4) >= 5.0 else 0
    elif row['KT'] == 'B':
        return 1 if ((row['DH1'] + row['DH2']*2 + row['DH3']) / 4) >= 5.0 else 0
    else:
        return 1 if ((row['DH1'] + row['DH2'] + row['DH3']) / 3) >= 5.0 else 0

dulieu['KQXT'] = dulieu.apply(kqxt, axis=1)

#11
# Lưu DataFrame dulieu vào file CSV với tên là 'processed_dulieuxettuyendaihoc.csv'
dulieu.to_csv('processed_dulieuxettuyendaihoc.csv', index=False)



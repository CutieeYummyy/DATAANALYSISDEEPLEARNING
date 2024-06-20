import pandas as pd
import numpy as np

# Load data
file_path = r'/1.csv'
dulieu = pd.read_csv(file_path)

#3
print(dulieu.head(10))
print(dulieu.tail(10))

# Fill missing values with 0 #4
df = dulieu.fillna(0, inplace=False)

# Fill missing 'T1' values with mean #5
print(dulieu['T1'].fillna(dulieu['T1'].mean(), inplace=False))

# Print TBM values for years 1, 2, and 6 #7
for i in ["1", "2", "6"]:
    print("TBM"+i)
# Tính toán TBM cho từng năm lớp và thêm vào dulieuFrame dulieu
dulieu['TBM1'] = (2*dulieu['T1'] + dulieu['L1'] + dulieu['H1'] + dulieu['S1'] + 2*dulieu['V1'] + dulieu['X1'] + dulieu['D1'] + dulieu['N1']) / 10
dulieu['TBM2'] = (2*dulieu['T2'] + dulieu['L2'] + dulieu['H2'] + dulieu['S2'] + 2*dulieu['V2'] + dulieu['X2'] + dulieu['D2'] + dulieu['N2']) / 10
dulieu['TBM3'] = (2*dulieu['T6'] + dulieu['L6'] + dulieu['H6'] + dulieu['S6'] + 2*dulieu['V6'] + dulieu['X6'] + dulieu['D6'] + dulieu['N6']) / 10

# There is no need to rename TBM6 to TBM3, it should be already TBM3.
# dulieu.rename(columns={"TBM6": "TBM3"}, inplace=True)


# Đổi tên cột TBM6 thành TBM3
#dulieu.rename(columns={"TBM6": "TBM3"}, inplace=True)

# Lưu dulieuFrame dulieu vào file CSV
df = dulieu.copy()

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
#9
def min_max_normalization(column):
    return (column - column.min()) / (column.max() - column.min()) * 4

dulieu['US_TBM1'] = min_max_normalization(dulieu['TBM1'])
dulieu['US_TBM2'] = min_max_normalization(dulieu['TBM2'])
dulieu['US_TBM3'] = min_max_normalization(dulieu['TBM3'])

#10. Tạo biến kết quả xét tuyển KQXT
def kqxt(row):
    if row['KT'] in ['A', 'A1']:
        return 1 if ((row['DH1']*2 + row['DH2'] + row['DH3']) / 4) >= 5.0 else 0
    elif row['KT'] == 'B':
        return 1 if ((row['DH1'] + row['DH2']*2 + row['DH3']) / 4) >= 5.0 else 0
    else:
        return 1 if ((row['DH1'] + row['DH2'] + row['DH3']) / 3) >= 5.0 else 0

dulieu['KQXT'] = dulieu.apply(kqxt, axis=1)

#11
# Lưu dulieuFrame dulieu vào file CSV với tên là 'processed_dulieuxettuyendaihoc.csv'
dulieu.to_csv('processed_dulieuxettuyendaihoc.csv', index=False)



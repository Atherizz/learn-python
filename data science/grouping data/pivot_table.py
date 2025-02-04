import pandas as pd
import numpy as np

data = {
    'tanggal': pd.date_range(start='2022-01-01', end='2024-12-31', periods=100),
    'region': np.random.choice(['Jakarta', 'Surabaya', 'Bandung', 'Medan'], 100),
    'kategori': np.random.choice(['Electronics', 'Fashion', 'Food', 'Books'], 100),
    'penjualan': np.random.randint(100, 1000, 100),
    'harga': np.random.randint(100000, 500000, 100)
}

df = pd.DataFrame(data)

df['tahun'] = df['tanggal'].dt.year
df['bulan'] = df['tanggal'].dt.month

pivot1 = pd.pivot_table(
    data=df,
    values='penjualan',
    index='region',
    columns='tahun',
    aggfunc='sum'
)
print("Total Penjualan per Region dan Tahun:")
print(pivot1)

# 2. Pivot table dengan multiple values
pivot2 = pd.pivot_table(
    data=df,
    values=['penjualan', 'harga'],
    index=['region', 'kategori'],
    columns='tahun',
    aggfunc={'penjualan': 'sum', 'harga': 'mean'},
    fill_value=0
)
print("\nAnalisis Detail per Region dan Kategori:")
print(pivot2)

# 3. Pivot table dengan subtotals
pivot3 = pd.pivot_table(
    data=df,
    values='penjualan',
    index=['region', 'kategori'],
    columns=['tahun', 'bulan'],
    aggfunc='sum',
    margins=True,  # Menambahkan total
    margins_name='Total'
)
print("\nPenjualan dengan Subtotal:")
print(pivot3)

# 4. Pivot table dengan multiple aggregations
pivot4 = pd.pivot_table(
    data=df,
    values=['penjualan', 'harga'],
    index='region',
    columns='tahun',
    aggfunc={
        'penjualan': ['sum', 'mean', 'count'],
        'harga': ['mean', 'min', 'max']
    }
)
print("\nAnalisis Komprehensif:")



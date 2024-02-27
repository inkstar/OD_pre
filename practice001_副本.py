import pandas as pd

# 读取Excel文件
excel_file = 'practice.xlsx'
sheets = pd.read_excel(excel_file, sheet_name=None, header=None)

# 合并每个工作表的有效信息并排除特定单元格内容和特定列
filtered_data = []
for sheet_name, sheet_data in sheets.items():
    # 去除前两行
    sheet_data = sheet_data.iloc[2:, :]
    # 过滤特定单元格内容
    sheet_data = sheet_data[~sheet_data[0].isin(['部门负责', '协管领导', '分管领导'])]
    # 过滤包含"意见"的列
    sheet_data = sheet_data.loc[:, ~sheet_data.iloc[0].astype(str).str.contains('意见')]
    filtered_data.append(sheet_data)

# 合并所有过滤后的数据
merged_data = pd.concat(filtered_data)

# 重置索引
merged_data.reset_index(drop=True, inplace=True)

# 保存合并后的数据到新的Excel文件
merged_file = 'merged_data02.xlsx'
merged_data.to_excel(merged_file, index=False)

print("合并完成，数据已保存到", merged_file)

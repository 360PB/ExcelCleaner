import pandas as pd
import os
import sys

# 获取脚本所在的目录
script_directory = os.path.dirname(os.path.abspath(__file__))

# 切换到脚本所在目录
os.chdir(script_directory)

print("Current working directory:", os.getcwd())

# 获取命令行参数，第一个参数为文件名
file_name = None
if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    # 如果没有提供文件名，使用默认值
    file_name = 'default_file.xlsx'
    print("请通过命令行参数指定文件名，例如: python script.py input_file.xlsx")
    print("使用默认文件名:", file_name)

# 读取表格数据
try:
    df = pd.read_excel(file_name, sheet_name='表格视图')
except FileNotFoundError:
    print(f"文件未找到: {file_name}，请确保文件存在于脚本所在目录中！")
    raise

# 找出重复的剧名
duplicates = df[df.duplicated(subset=['剧名'], keep=False)]

# 统计重复剧名的数量
duplicate_counts = df['剧名'].value_counts()

# 打印重复的内容
print("\n重复的剧名及重复次数：")
for name, count in duplicate_counts.items():
    if count > 1:
        print(f"剧名: {name}, 重复次数: {count}")

# 打印重复的行
if not duplicates.empty:
    print("\n重复的行：")
    print(duplicates)
else:
    print("\n没有重复的行！")

# 对“剧名”列进行去重，保留第一条记录
df_deduplicated = df.drop_duplicates(subset=['剧名'], keep='first')

# 保存去重后的数据到新文件
output_file = 'deduplicated_' + file_name
df_deduplicated.to_excel(output_file, index=False)
print(f"\n去重后的数据已保存到文件: {output_file}")
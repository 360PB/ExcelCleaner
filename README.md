# Excel 数据去重工具

一个用于处理 Excel 文件的 Python 脚本，可以对指定列（如“剧名”）进行去重，并打印重复内容及数量。去重后的数据会保存到一个新的 Excel 文件中。

## 功能

1. **读取 Excel 文件**：从指定的 Excel 文件中读取数据。
2. **去重处理**：对指定列（如“剧名”）进行去重，保留第一条记录。
3. **打印重复内容**：显示重复的剧名及其重复次数。
4. **保存结果**：将去重后的数据保存到一个新的 Excel 文件中。

## 使用方法

**整合包:**

https://pan.quark.cn/s/c1f533aa01fd

### 1. 安装依赖

确保你已经安装了以下 Python 模块：

- `pandas`
- `openpyxl`

运行以下命令安装依赖：

bash复制

```bash
pip install pandas openpyxl
```

### 2. 准备 Excel 文件

将需要处理的 Excel 文件放在脚本所在的目录下，或者通过命令行参数指定文件路径。

### 3. 运行脚本

使用以下命令运行脚本：

```bash
python script.py <input_file.xlsx>
```

例如：

```bash
python script.py 16137.xlsx
```

如果未指定文件名，脚本会使用默认文件名 `default_file.xlsx`。

### 4. 查看输出

脚本会输出以下内容：

- 当前工作目录
- 重复的剧名及其重复次数
- 重复的行
- 去重后的数据保存到文件 `deduplicated_<input_file.xlsx>`



## 注意事项

1. **文件格式**：确保输入文件是 `.xlsx` 格式的 Excel 文件。
2. **列名**：脚本假设 Excel 文件中有一列名为“剧名”。如果列名不同，请修改脚本中的列名。
3. **依赖库**：确保已安装 `pandas` 和 `openpyxl` 模块。

## 贡献

如果你有任何改进建议或功能需求，欢迎提交 Issue 或 Pull Request。


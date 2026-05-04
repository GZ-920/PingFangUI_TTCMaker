#!/usr/bin/env python3
“””
PingFangUI.ttc 生成脚本
用法：

1. 将本脚本和 names.json 放在同一目录
1. 将你的替换字体（TTF/OTF）放在同一目录
1. 在 a-Shell 中运行：python3 make.py 你的字体.ttf

生成的 PingFangUI.ttc 会出现在同一目录下。
“””

import sys
import os
import json
import copy

def check_deps():
try:
import fontTools
except ImportError:
print(“正在安装 fonttools，请稍候…”)
os.system(“pip install fonttools -q”)
print(“安装完成”)

check_deps()

from fontTools.ttLib import TTFont
from fontTools.ttLib.ttCollection import TTCollection

def main():
if len(sys.argv) < 2:
print(“用法：python3 make.py 你的字体.ttf”)
sys.exit(1)

```
font_path = sys.argv[1]
script_dir = os.path.dirname(os.path.abspath(__file__))
names_path = os.path.join(script_dir, "names.json")

# 检查文件
if not os.path.exists(font_path):
    print(f"错误：找不到字体文件 {font_path}")
    sys.exit(1)
if not os.path.exists(names_path):
    print(f"错误：找不到 names.json，请确保它和脚本在同一目录")
    sys.exit(1)

# 读取 name 表数据
print("读取 name 表数据...")
with open(names_path, "r", encoding="utf-8") as f:
    names_list = json.load(f)
total = len(names_list)
print(f"共需生成 {total} 个子字体")

# 读取替换字体（支持 TTF/OTF 和 TTC）
print(f"读取替换字体：{font_path}")
try:
    base_font = TTFont(font_path)
except Exception:
    # 如果是 TTC，取第一个子字体
    col_in = TTCollection(font_path)
    base_font = col_in.fonts[0]
    print(f"  检测到 TTC 格式，使用第 1 个子字体")

fonts = []
for i, records in enumerate(names_list):
    print(f"  处理 {i+1}/{total}...", end="\r")

    # 深拷贝字体
    font = copy.deepcopy(base_font)

    # 替换 name 表
    name_table = font['name']
    name_table.names = []
    for rec in records:
        from fontTools.ttLib.tables._n_a_m_e import NameRecord
        nr = NameRecord()
        nr.nameID    = rec["nameID"]
        nr.platformID = rec["platformID"]
        nr.platEncID  = rec["platEncID"]
        nr.langID     = rec["langID"]
        try:
            nr.string = rec["value"].encode("utf-16-be")
        except Exception:
            nr.string = bytes.fromhex(rec["value"])
        name_table.names.append(nr)

    fonts.append(font)

print(f"\n所有子字体处理完毕，正在打包 TTC...")
out_path = os.path.join(script_dir, "PingFangUI.ttc")
col = TTCollection()
col.fonts = fonts
col.save(out_path)

size_mb = os.path.getsize(out_path) / 1024 / 1024
print(f"完成！输出文件：{out_path}（{size_mb:.1f} MB）")
```

if **name** == “**main**”:
main()
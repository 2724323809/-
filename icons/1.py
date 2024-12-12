import os
import json

# 配置
repo_url = "https://github.com/2724323809/XIAOBAIS/tree/main/icons"  # 替换为你的仓库 URL
icons_folder = "icons"  # 图标文件夹路径
output_file = "icons.json"  # 输出的 JSON 文件

# 初始化 JSON 结构
icons_data = {
    "name": "AI&Emby",
    "description": "GitHub: @cc63",
    "icons": []
}

# 遍历图标文件夹
for filename in os.listdir(icons_folder):
    if filename.endswith(".png"):  # 只处理 PNG 文件
        icon_name = filename.replace(".png", "")  # 去掉扩展名
        icon_url = f"{repo_url}/{icons_folder}/{filename}"
        icons_data["icons"].append({
            "name": icon_name,
            "url": icon_url
        })

# 保存 JSON 文件
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(icons_data, f, ensure_ascii=False, indent=4)

print(f"JSON 文件已生成：{output_file}")
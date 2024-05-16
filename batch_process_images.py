from PIL import Image
import os
from tqdm import tqdm

# 定义输入和输出文件夹路径
input_folder = r'C:\Nathat_work\pchuli\input'
output_folder = r'C:\Nathat_work\pchuli\output'

# 检查输出文件夹是否已设定，如果未设定则使用默认路径
if not output_folder:
    output_folder = os.path.join(os.getcwd(), 'output')
    print(f"输出文件夹未设定，使用默认路径：{output_folder}")

# 如果输出文件夹不存在，创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取输入文件夹中的所有文件名
files = [f for f in os.listdir(input_folder) if f.endswith('.png')]
total_files = len(files)

# 使用 tqdm 创建一个进度条
with tqdm(total=total_files, desc="处理进度", unit="file") as pbar:
    # 遍历输入文件夹中的所有文件
    for filename in files:
        # 打开图片
        img = Image.open(os.path.join(input_folder, filename))
        
        # 创建一个白色背景的新图像
        background = Image.new('RGB', img.size, (255, 255, 255))
        
        # 将你的图片粘贴到白色背景上
        background.paste(img, (0, 0), img)
        
        # 保存结果图片到输出文件夹
        output_path = os.path.join(output_folder, filename)
        background.save(output_path)
        
        # 更新进度条
        pbar.update(1)

print('批量处理完成！')

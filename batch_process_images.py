from PIL import Image
import os

# 定义输入和输出文件夹路径
input_folder = r'C:\Nathat_work\pchuli\input'
output_folder = r'C:\Nathat_work\pchuli\output'

# 如果输出文件夹不存在，创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        # 打开图片
        img = Image.open(os.path.join(input_folder, filename))
        
        # 创建一个白色背景的新图像
        background = Image.new('RGB', img.size, (255, 255, 255))
        
        # 将你的图片粘贴到白色背景上
        background.paste(img, (0, 0), img)
        
        # 保存结果图片到输出文件夹
        output_path = os.path.join(output_folder, filename)
        background.save(output_path)

print('批量处理完成！')

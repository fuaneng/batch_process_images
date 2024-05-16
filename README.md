# batch_process_images
Transparent image adds white background/background_img

白色背景请使用batch_process_imger.py

固定图片作为背景请使用background_img.py

拉取phthon脚本之后需手动修改本地指向输入和输出路径
# 定义输入和输出文件夹路径
input_folder = r'C:\Nathat_work\pchuli\input' #该路径改为你当前需要处理图片的文件夹

output_folder = r'C:\Nathat_work\pchuli\output' #该路径改为你处理图片后输出的文件夹

background_image_path = r'C:\Nathat_work\pchuli\img\background.png' #该路径改为你固定背景图片的路径和名称
# 依赖库
确保你的 Python 环境已经安装了 Pilow库、 tqdm 库

如果没有安装，可以使用以下命令安装:

pip install pillow

pip install tqdm
# 执行脚本
启动Power Shall,输入以下指令即可执行脚本文件自动批处理

python batch_process_images.py

![image](https://github.com/fuaneng/batch_process_images/assets/136696600/7174fda4-17e8-430c-9a0b-68229ea6193f)


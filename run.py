# 作者：chbxiong
# 单位：CHY
# 开发时间：2020-7-10 21:54
# 文件名称：run.py
# 开发工具：PyCharm
# 功能：提取音乐高潮部分

from pychorus import find_and_output_chorus

chorus_start_sec = find_and_output_chorus("魔鬼中的天使田馥甄.mp3", "test.wav", 40)


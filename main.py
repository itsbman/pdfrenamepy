# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from pdf_reader import extract_pdf_metadata
from pdf_source import AbstractSource

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_path = '/home/abi/Desktop/hdd/literature/unread/2109.13602.pdf'
    pdf_info = extract_pdf_metadata(file_path)
    new_pdf_name = f'/home/abi/Desktop/hdd/literature/unread/{pdf_info.title} ({pdf_info.year}).pdf'
    os.rename(file_path, new_pdf_name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

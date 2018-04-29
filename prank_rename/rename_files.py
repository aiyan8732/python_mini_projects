import os
from string import digits
def rename_files():
    file_list = os.listdir(r"/Users/jiemeizhang/Documents/SelfLearning/Python_mini_projects/prank_rename/prank")
    # print(file_list)
    saved_path = os.getcwd()
    # print("Current dir is "+saved_path)
    os.chdir(r"/Users/jiemeizhang/Documents/SelfLearning/Python_mini_projects/prank_rename/prank")
    
    for file_name in file_list:
        remove_digits = str.maketrans('', '', digits)
        print("Old name of the file is "+file_name)
        print("New name of the file is "+file_name.translate(remove_digits))
        os.rename(file_name, file_name.translate(remove_digits))
    os.chdir(saved_path)

rename_files()
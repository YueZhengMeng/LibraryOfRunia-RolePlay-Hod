"""
过滤出含安吉拉对话的文件
"""
import os
import pandas as pd
import shutil

def move_csv_files(csv_path):
    others_folder = os.path.join(csv_path, 'others')
    angela_included_folder = os.path.join(csv_path, 'angela_included')
    os.makedirs(angela_included_folder,exist_ok=True)
    os.makedirs(others_folder,exist_ok=True)
    for filename in os.listdir(csv_path):
        if filename.endswith('.csv'): 
            file_path = os.path.join(csv_path, filename)
            try:
                df = pd.read_csv(file_path)
                contains_angela = df['Character Name'].str.contains('Angela|安吉拉', case=False, na=False).any()
                if contains_angela:
                    shutil.move(file_path, angela_included_folder)
                    print(f'Moved {filename} to {angela_included_folder}')
                else:
                    shutil.move(file_path, others_folder)
                    print(f'Moved {filename} to {others_folder}')
            except Exception as e:
                print(f'Error processing {filename}: {e}')
        else:
            continue

if __name__ == "__main__":
    
    move_csv_files("raw_data")
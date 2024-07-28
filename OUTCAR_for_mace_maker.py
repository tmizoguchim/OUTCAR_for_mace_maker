import os
import shutil

# 入力フォルダと出力フォルダのパス
input_folder = "/home/***/*** your current folder "
output_folder = "/home/+++/+++/OUTCAR-collection your saving folder "
max_files = 100  # コピーする最大ファイル数 for your safety

# 出力フォルダが存在しない場合は作成
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ファイル数カウンター
file_count = 0

# 入力フォルダ直下のサブフォルダを取得
for subdir in os.listdir(input_folder):
    subdir_path = os.path.join(input_folder, subdir)
#Specifiy folder name for searching. For instance, if you want to search the folders including "Li", then change below to be 'Li'.
    if os.path.isdir(subdir_path) and '****' in subdir:
        print(f"Processing subdir: {subdir_path}")  # デバッグ: 処理中のサブディレクトリ
        # サブフォルダ内の全ファイルとサブフォルダを再帰的に検索
        for root, dirs, files in os.walk(subdir_path):
            poscar_path = os.path.join(root, "POSCAR")
            outcar_path = os.path.join(root, "OUTCAR")
            
            # POSCARファイルが存在するかチェック
            if os.path.exists(poscar_path):
                print(f"POSCAR found in: {root}")  # デバッグ: POSCARファイル発見
                # POSCARファイルから組成を取得
                with open(poscar_path, 'r') as f:
                    lines = f.readlines()
                    elements = lines[5].split()
                    counts = list(map(int, lines[6].split()))
                    composition = ' '.join([f"{elem}{cnt}" for elem, cnt in zip(elements, counts)])
            
            # OUTCARファイルが存在するかチェック
            if os.path.exists(outcar_path):
                print(f"OUTCAR found in: {root}")  # デバッグ: OUTCARファイル発見
                with open(outcar_path, 'r') as f:
                    outcar_lines = f.readlines()
                
                # OUTCAR内の"POSCAR = "を組成情報に置き換える
                with open(os.path.join(root, "OUTCAR_for_mace"), 'w') as f:
                    for line in outcar_lines:
                        if "POSCAR =" in line:
                            f.write(f"POSCAR = {composition}\n")
                        else:
                            f.write(line)
                
                # 修正ファイルを保存
                shutil.copy2(os.path.join(root, "OUTCAR_for_mace"),
                             os.path.join(output_folder, f"OUTCAR_for_mace-{os.path.basename(root)}"))
                print(f"Processed OUTCAR: {outcar_path} with composition {composition}")
                
                # カウントを増やす
                file_count += 1
                if file_count >= max_files:
                    print("Maximum file limit reached. Stopping the copy process.")
                    break
            else:
                print(f"OUTCAR not found in: {root}")  # デバッグ: OUTCARファイルがない
    else:
        print(f"'****' not in subdir name: {subdir_path}")  # デバッグ: '****'がサブディレクトリ名に含まれない
    if file_count >= max_files:
        break

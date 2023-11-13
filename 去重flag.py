def remove_duplicates_from_file(file_path):
    try:
        lines_seen = set()
        with open(file_path, 'r') as file:
            lines = file.readlines()
        with open(file_path, 'w') as file:
            for line in lines:
                if line not in lines_seen:
                    file.write(line)
                    lines_seen.add(line)
        print("重复flag已成功从原文件中去除！")
    except FileNotFoundError:
        print("文件未找到。请确保文件路径正确。")

if __name__ == "__main__":
    file_path = "flag.txt"  # 替换为你的文件路径
    remove_duplicates_from_file(file_path)

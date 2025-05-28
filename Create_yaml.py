import yaml
import os

def create_yaml(dataset_root, train_path, val_path, test_path, class_names_file, output_path='data.yaml'):
    """
    Tạo file YAML cho Ultralytics YOLO với class_names đọc từ file .txt.

    Args:
        dataset_root (str): Đường dẫn gốc của tập dữ liệu (path).
        train_path (str): Đường dẫn tương đối đến thư mục hình ảnh train.
        val_path (str): Đường dẫn tương đối đến thư mục hình ảnh val.
        test_path (str): Đường dẫn tương đối đến thư mục hình ảnh test (có thể là None).
        class_names_file (str): Đường dẫn đến file .txt chứa tên lớp (mỗi dòng một tên).
        output_path (str): Đường dẫn lưu file YAML.
    """
    # Đọc danh sách tên lớp từ file .txt
    try:
        with open(class_names_file, 'r') as f:
            class_names = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file {class_names_file}")

    # Tạo dictionary ánh xạ class_id đến tên lớp
    class_names_dict = {i: name for i, name in enumerate(class_names)}

    # Định nghĩa cấu hình dữ liệu
    data_config = {
        'path': dataset_root,
        'train': train_path,
        'val': val_path,
        'names': class_names_dict
    }
    
    # Thêm test_path nếu có
    if test_path:
        data_config['test'] = test_path
    
    # Đảm bảo thư mục đầu ra tồn tại
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    # Ghi cấu hình vào file YAML với comment
    with open(output_path, 'w') as f:
        f.write("# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]\n")
        yaml.dump(data_config, f, sort_keys=False, allow_unicode=True)
        f.write("\n# Classes\n")
        f.write("names:\n")
        for class_id, class_name in class_names_dict.items():
            f.write(f"  {class_id}: {class_name}\n")
    
    print(f"File YAML đã được tạo tại: {output_path}")

# Ví dụ sử dụng
if __name__ == "__main__":
    create_yaml(
        dataset_root="../datasets/brain-tumor",
        train_path="train/images",
        val_path="valid/images",
        test_path=None,  # Không có thư mục test
        class_names_file="classes.txt",
        output_path="configs/brain_tumor_data.yaml"
    )

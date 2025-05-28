import yaml
import os

def create_yaml(train_path, val_path, test_path, num_classes, class_names_file, output_path='data.yaml'):
    """
    Tạo file YAML cho Ultralytics YOLO dựa trên đầu vào người dùng.

    Args:
        train_path (str): Đường dẫn đến thư mục train.
        val_path (str): Đường dẫn đến thư mục val.
        test_path (str): Đường dẫn đến thư mục test (có thể là None).
        num_classes (int): Số lượng lớp.
        class_names_file (str): Đường dẫn đến file .txt chứa tên lớp (mỗi dòng một tên).
        output_path (str): Đường dẫn lưu file YAML.
    """
    # Đọc danh sách tên lớp từ file .txt
    try:
        with open(class_names_file, 'r') as f:
            class_names = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file {class_names_file}")
    
    # Kiểm tra số lượng lớp
    if len(class_names) != num_classes:
        raise ValueError(f"Số lớp ({num_classes}) không khớp với số tên lớp trong {class_names_file} ({len(class_names)})")

    # Định nghĩa cấu hình dữ liệu
    data_config = {
        'train': train_path,
        'val': val_path,
        'nc': num_classes,
        'names': class_names
    }
    
    # Thêm test_path nếu có
    if test_path:
        data_config['test'] = test_path
    
    # Đảm bảo thư mục đầu ra tồn tại
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    # Ghi cấu hình vào file YAML
    with open(output_path, 'w') as f:
        yaml.dump(data_config, f, sort_keys=False)
    
    print(f"File YAML đã được tạo tại: {output_path}")

# Ví dụ sử dụng
if __name__ == "__main__":
    create_yaml(
        train_path="../dataset/train/images",
        val_path="../dataset/val/images",
        test_path="../dataset/test/images",
        num_classes=2,
        class_names_file="classes.txt",
        output_path="configs/data.yaml"
    )
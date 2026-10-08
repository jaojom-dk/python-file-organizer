import os
import shutil

# 1. กำหนดตำแหน่งโฟลเดอร์ที่ต้องการจัดระเบียบ (เช่น โฟลเดอร์ Downloads ในเครื่องของเรา)
target_dir = r"D:\kai\TestFolder"

# 2. กำหนดประเภทไฟล์และโฟลเดอร์ปลายทาง
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.xlsx', '.pptx', '.txt'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Programs': ['.exe', '.msi']
}

def organize_files():
    # ตรวจสอบว่ามีโฟลเดอร์เป้าหมายอยู่จริงไหม
    if not os.path.exists(target_dir):
        print(f"ไม่พบโฟลเดอร์: {target_dir}")
        return

    # วนลูปอ่านรายชื่อไฟล์ทั้งหมดในโฟลเดอร์
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        
        # ตรวจสอบว่าต้องเป็น 'ไฟล์' ไม่ใช่ 'โฟลเดอร์ซ้อน'
        if os.path.isfile(file_path):
            # แยกนามสกุลไฟล์ออกมาเป็นตัวพิมพ์เล็ก (เช่น .jpg, .pdf)
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension.lower()

            # ตรวจสอบว่านามสกุลไฟล์นี้ตรงกับหมวดหมู่ไหนที่ตั้งไว้
            moved = False
            for folder_name, extensions in file_types.items():
                if file_extension in extensions:
                    # สร้างโฟลเดอร์ปลายทางถ้ายังไม่มี (เช่น โฟลเดอร์ Images)
                    folder_path = os.path.join(target_dir, folder_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    # ย้ายไฟล์เข้าโฟลเดอร์แยกประเภท
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f"ย้ายไฟล์ {filename} ไปยังโฟลเดอร์ {folder_name} เรียบร้อยแล้ว")
                    moved = True
                    break
            
            # ถ้าไม่ตรงกับหมวดหมู่ไหนเลย ให้ย้ายไปไว้ในโฟลเดอร์ Others
            if not moved and file_extension != '':
                others_path = os.path.join(target_dir, 'Others')
                if not os.path.exists(others_path):
                    os.makedirs(others_path)
                shutil.move(file_path, os.path.join(others_path, filename))
                print(f"ย้ายไฟล์ {filename} ไปยังโฟลเดอร์ Others")

if __name__ == '__main__':
    print("--- เริ่มต้นจัดระเบียบไฟล์อัตโนมัติ ---")
    organize_files()
    print("--- จัดระเบียบไฟล์เสร็จสิ้น! ---")
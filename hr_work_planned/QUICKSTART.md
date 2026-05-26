# Quick Start Guide - HR Work Planned Module

## 🎯 Bắt Đầu Nhanh

### Step 1: Cài Đặt Module

#### Cách 1: Dùng Terminal
```bash
# Vào thư mục Odoo
cd c:\Users\rtrttt\Documents\GitHub\odoo

# Chạy lệnh update module
./odoo-bin -d <database_name> -u hr_work_planned --no-http
```

**Chú ý**: Thay `<database_name>` bằng tên database thực tế của bạn.

#### Cách 2: Từ Giao Diện Odoo
1. Vào **Apps**
2. Tìm kiếm "Work Planned"
3. Click **Install**
4. Refresh page (F5)

---

### Step 2: Xác Nhận Cài Đặt

Sau khi cài, bạn sẽ thấy:
- ✓ Menu **Work Planned** xuất hiện trong **Human Resources → Attendances**
- ✓ Tab **"Work Planned"** xuất hiện trong biểu mẫu Employee

---

### Step 3: Tạo Công Ca Đầu Tiên

#### Cách 1: Từ Menu Chính
1. Vào: **Human Resources → Attendances → Work Planned**
2. Click **Create**
3. Điền thông tin:
   - **Employee**: Chọn nhân viên (ví dụ: "John Smith")
   - **Scheduled Start Time**: Chọn ngày giờ bắt đầu
     - Ví dụ: May 23, 2024 08:00 AM
   - **Scheduled End Time**: Chọn ngày giờ kết thúc
     - Ví dụ: May 23, 2024 05:00 PM
   - **Description**: Ghi chú (tùy chọn)
     - Ví dụ: "Regular shift - May 23"
4. Click **Save**

#### Cách 2: Từ Employee Form
1. Vào **Human Resources → Employees**
2. Chọn một nhân viên
3. Chuyển sang tab **"Work Planned"**
4. Ở dưới danh sách, click **Create** (hoặc Edit Line)
5. Điền thông tin tương tự
6. Click **Save**

---

### Step 4: Phê Duyệt Công Ca

#### Phê Duyệt Từ Danh Sách
1. Vào: **Human Resources → Attendances → Work Planned**
2. Chọn công ca (checkbox bên trái)
3. Click nút **Approve** ở trên
4. Xác nhận (nếu cần)
5. Công ca thay đổi thành **Approved** ✅

#### Phê Duyệt Từ Chi Tiết
1. Mở công ca muốn phê duyệt
2. Trong form, click nút **Approve**
3. Xác nhận
4. Status thay đổi thành **Approved** ✅

---

### Step 5: Xem Công Ca Trên Employee

1. Vào **Human Resources → Employees**
2. Chọn nhân viên
3. Chuyển sang tab **"Work Planned"**
4. Xem danh sách công ca đã phê duyệt
5. Click vào bất kỳ hàng nào để xem chi tiết

---

## 📊 Các Thao Tác Cơ Bản

### Xem Danh Sách

| Thao Tác | Bước |
|----------|------|
| **Xem tất cả** | Vào Menu → Work Planned |
| **Xem chi tiết** | Click vào bất kỳ hàng nào |
| **Xem của employee** | Vào Employee → Tab "Work Planned" |

### Lọc & Tìm Kiếm

| Loại Lọc | Cách Thực Hiện |
|----------|---|
| **Theo trạng thái** | Click "Approved" / "Rejected" / "Draft" |
| **Theo thời gian** | Click "Today" / "This Week" / "This Month" |
| **Tìm nhân viên cụ thể** | Dùng search box, gõ tên nhân viên |
| **Lọc tùy chỉnh** | Search → Add Custom Filter |

### Nhóm Dữ Liệu

1. Click **Search** → **Group By**
2. Chọn một trong các tuỳ chọn:
   - **By Employee**: Nhóm theo nhân viên
   - **By Date**: Nhóm theo ngày
   - **By Department**: Nhóm theo phòng ban
   - **By Status**: Nhóm theo trạng thái

---

## 🔄 Quy Trình Tiêu Chuẩn

```
1. Tạo Công Ca (Draft)
           ↓
2. Phê Duyệt (Approved) ← ← ← ← 
           ↓              ↑    ↑
3. Sử Dụng Công Ca      ↑    ↑
           ↓              ↑    ↑
4. Reset (Nếu Cần) ← ← → Từ Chối (Rejected)
```

---

## 🎓 Ví Dụ Thực Tế

### Ví Dụ 1: Giáo Viên Kiểm Tra Công Ca

**Tình Huống**: Giáo viên muốn xem công ca đã phê duyệt cho tháng này

**Các Bước**:
1. Vào **Human Resources → Employees**
2. Tìm chính mình
3. Click vào Employee Form
4. Chuyển sang tab **"Work Planned"**
5. Xem danh sách công ca tháng này
6. Chỉ trong các thời gian này mới check-in/out được ghi nhận

### Ví Dụ 2: Quản Lý Phê Duyệt Công Ca

**Tình Huống**: Quản lý muốn phê duyệt công ca của nhân viên dưới quản lý

**Các Bước**:
1. Vào **Human Resources → Attendances → Work Planned**
2. Click **Search** → **Filter** → **Draft** (xem công ca chưa phê duyệt)
3. Xem danh sách công ca của nhân viên
4. Chọn những công ca cần phê duyệt
5. Click **Approve**
6. Công ca đó trở thành Approved ✅

### Ví Dụ 3: Lọc Công Ca Tuần Này

**Tình Huống**: Xem tất cả công ca được phê duyệt trong tuần này

**Các Bước**:
1. Vào **Human Resources → Attendances → Work Planned**
2. Click **Search**
3. Click **This Week**
4. Click **Approved**
5. Xem kết quả

---

## ⚙️ Cài Đặt Quyền Hạn

Module tự động thiết lập quyền:
- **Nhân viên**: Xem công ca của chính mình
- **Quản lý**: Xem và phê duyệt công ca của nhân viên
- **HR Officer**: Quản lý toàn bộ

❌ Nếu bạn không thấy công ca, kiểm tra:
1. Bạn có phải nhân viên đó không?
2. Công ca có được phê duyệt chưa?
3. Bạn có HR permissions không?

---

## 📞 Hỗ Trợ

### Gặp Vấn Đề?

**Tab không hiển thị:**
- Refresh page (F5)
- Đảm bảo module đã cài đặt
- Đăng xuất → Đăng nhập lại

**Không thể tạo công ca:**
- Kiểm tra bạn có quyền không (phải là HR Employee trở lên)
- Chắc chắn đã chọn Employee
- Start Time và End Time bắt buộc

**Không thể phê duyệt:**
- Phải là HR Manager hoặc Officer
- Công ca phải ở trạng thái Draft
- Click nút Approve ở header hoặc trong Form

---

## 📚 Tài Liệu Thêm

- **README.md**: Mô tả chi tiết module
- **USAGE_GUIDE_VI.md**: Hướng dẫn sử dụng đầy đủ
- **TECHNICAL_DOCS.md**: Tài liệu cho developers

---

## ✅ Checklist Cài Đặt

- [ ] Copy folder `hr_work_planned` vào `addons/`
- [ ] Chạy install command
- [ ] Thấy menu "Work Planned" trong HR
- [ ] Tạo công ca test
- [ ] Phê duyệt công ca
- [ ] Xem trên Employee tab
- [ ] Test các bộ lọc
- [ ] Kiểm tra quyền hạn

---

**Chúc mừng! Bạn đã sẵn sàng sử dụng HR Work Planned Module! 🚀**

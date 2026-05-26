# Hướng Dẫn Sử Dụng Module HR Work Planned

## Tổng Quan

Module `hr_work_planned` cho phép:
- **Giáo viên/Nhân viên** xem lịch làm việc được phê duyệt của họ
- **Quản lý** phê duyệt hoặc từ chối công ca
- **Hệ thống** chỉ ghi nhận attendance trong thời gian công ca được phê duyệt

## Quy Trình Làm Việc

### 1. Tạo Công Ca Mới

#### Cách 1: Từ Menu Chính
1. Vào: **Human Resources → Attendances → Work Planned**
2. Click **Create**
3. Điền thông tin:
   - **Employee**: Chọn nhân viên
   - **Scheduled Start Time**: Giờ bắt đầu
   - **Scheduled End Time**: Giờ kết thúc
   - **Description** (tuỳ chọn): Ghi chú
4. Click **Save**

#### Cách 2: Từ Biểu Mẫu Nhân Viên
1. Vào thông tin nhân viên
2. Chuyển đến tab **Work Planned**
3. Click **Create** hoặc **Edit Line**
4. Điền thông tin và Save

### 2. Phê Duyệt Công Ca

**Từ Danh Sách:**
- Chọn một hoặc nhiều bản ghi
- Click **Approve** (nút xanh)
- Trạng thái sẽ thay đổi từ "Draft" → "Approved"

**Từ Chi Tiết:**
- Mở công ca muốn phê duyệt
- Click nút **Approve** ở phía trên
- Xác nhận khi cần

### 3. Từ Chối Công Ca

**Từ Danh Sách:**
- Chọn một hoặc nhiều bản ghi
- Click **Reject** (nút đỏ)
- Trạng thái sẽ thay đổi từ "Draft" → "Rejected"

**Từ Chi Tiết:**
- Mở công ca muốn từ chối
- Click nút **Reject** ở phía trên
- Xác nhận khi cần

### 4. Sử Dụng Bộ Lọc

#### Lọc Theo Trạng Thái
- Click **Approved**: Xem công ca đã phê duyệt
- Click **Rejected**: Xem công ca bị từ chối
- Click **Draft**: Xem công ca chưa phê duyệt

#### Lọc Theo Thời Gian
- **Today**: Công ca hôm nay
- **This Week**: Công ca tuần này
- **This Month**: Công ca tháng này

#### Lọc Tùy Chỉnh
1. Click **Search** → **Add Custom Filter**
2. Chọn tiêu chí (Employee, Department, Manager, v.v.)
3. Click **Apply**

### 5. Nhóm Dữ Liệu

Để nhóm dữ liệu theo một tiêu chí:
1. Click **Search** → **Group By**
2. Chọn tiêu chí:
   - **By Employee**: Nhóm theo nhân viên
   - **By Date**: Nhóm theo ngày
   - **By Department**: Nhóm theo phòng ban
   - **By Status**: Nhóm theo trạng thái

## Các Trường Dữ Liệu

### Bắt Buộc
- **Employee**: Nhân viên làm công ca này
- **Scheduled Start Time**: Thời điểm bắt đầu
- **Scheduled End Time**: Thời điểm kết thúc

### Tùy Chọn
- **Description**: Ghi chú về công ca (lý do, ghi chú đặc biệt, v.v.)

### Tự Động Tính Toán
- **Planned Hours**: Số giờ (tính từ Start - End)
- **Date**: Ngày làm việc
- **Department**: Lấy từ phòng ban của nhân viên
- **Manager**: Lấy từ quản lý của nhân viên
- **Status**: Mặc định "Draft"

## Xem Thông Tin Chi Tiết

1. Vào danh sách Work Planned
2. Click vào bất kỳ hàng nào để xem chi tiết
3. Xem thông tin đầy đủ, lịch sử thay đổi
4. Có thể chỉnh sửa description hoặc đổi trạng thái

## Tích Hợp với Attendance

**Quy Tắc Ghi Nhận:**
- ✅ Check-in/out **trong** thời gian công ca được phê duyệt → **Ghi nhận**
- ❌ Check-in/out **ngoài** thời gian công ca được phê duyệt → **Không ghi nhận**
- ❌ Không có công ca được phê duyệt → **Không ghi nhận bất kỳ check-in/out nào**

## Hạn Chế và Quy Định

1. Chỉ nhân viên và quản lý của họ có thể xem công ca
2. Chỉ HR Manager hoặc Officer có thể phê duyệt/từ chối
3. Không thể xóa công ca (chỉ có thể đặt lại Draft)
4. Không thể chỉnh sửa sau khi phê duyệt (phải đặt lại Draft trước)

## Mẹo Sử Dụng

1. **Lập Kế Hoạch Hàng Tuần**: Tạo công ca cho cả tuần vào đầu tuần
2. **Sử Dụng Mô Tả**: Ghi chú các thay đổi hoặc lý do đặc biệt
3. **Xem Lịch Sử**: Click **History** tab để xem ai đã phê duyệt/từ chối
4. **Bộ Lọc Lưu**: Sử dụng "Save Current Search" để lưu bộ lọc thường dùng

## Khắc Phục Sự Cố

### Không Thấy Tab "Work Planned"
- Đảm bảo module `hr_work_planned` đã được cài đặt
- Refresh page (F5)
- Đăng xuất và đăng nhập lại

### Không Thể Phê Duyệt
- Kiểm tra quyền hạn (phải là HR Manager hoặc Officer)
- Công ca phải ở trạng thái "Draft"

### Attendance Không Được Ghi Nhận
- Kiểm tra công ca được phê duyệt chưa
- Kiểm tra thời gian check-in/out có nằm trong thời gian công ca
- Kiểm tra nhân viên có được gán công ca không

## Liên Hệ Hỗ Trợ

Nếu có vấn đề, vui lòng:
1. Kiểm tra lại công ca (xem từng trường chi tiết)
2. Xem lịch sử thay đổi
3. Liên hệ IT Team hoặc HR Manager

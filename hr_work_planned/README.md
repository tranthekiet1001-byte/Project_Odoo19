# HR Work Planned Module

## Mô tả

Module `hr_work_planned` được phát triển dựa trên module `hr_attendance` nhằm quản lý lịch làm việc đã phê duyệt của nhân viên.

## Chức năng

### 1. Quản lý Lịch Làm Việc Đã Phê Duyệt
- Tạo và quản lý các công ca làm việc được phê duyệt
- Chỉ những công ca được phê duyệt mới được ghi nhận trong hệ thống check-in/out
- Nếu nhân viên check-in/out ngoài thời gian công ca được phê duyệt, sẽ không được ghi nhận

### 2. Trạng Thái Công Ca
- **Draft (Nháp)**: Công ca vừa được tạo, chưa phê duyệt
- **Approved (Phê duyệt)**: Công ca được phê duyệt, được ghi nhận trong attendance
- **Rejected (Từ chối)**: Công ca bị từ chối

### 3. Tab "Work Planned" trên Biểu Mẫu Nhân Viên
- Hiển thị danh sách tất cả công ca đã phê duyệt của nhân viên
- Cho phép xem chi tiết, phê duyệt, hoặc từ chối công ca

### 4. Xem Danh Sách Chi Tiết
Truy cập qua: **Human Resources → Attendances → Work Planned**

#### Các Cột Hiển Thị:
- **Employee (Nhân viên)**: Tên nhân viên
- **Start Time (Giờ Bắt Đầu)**: Thời gian bắt đầu công ca
- **End Time (Giờ Kết Thúc)**: Thời gian kết thúc công ca
- **Hours (Số Giờ)**: Tổng số giờ làm việc
- **Status (Trạng Thái)**: Trạng thái công ca (Draft/Approved/Rejected)

#### Các Bộ Lọc:
- Lọc theo nhân viên, ngày tháng, phòng ban, quản lý
- Lọc theo trạng thái: Phê duyệt, Từ chối, Nháp
- Lọc theo thời gian: Hôm nay, Tuần này, Tháng này

#### Nhóm Dữ Liệu:
- Nhóm theo: Nhân viên, Ngày, Phòng ban, Trạng thái

### 5. Các Thao Tác
- **Approve (Phê Duyệt)**: Phê duyệt một hoặc nhiều công ca
- **Reject (Từ Chối)**: Từ chối một hoặc nhiều công ca
- **Reset to Draft**: Đặt lại trạng thái về Nháp

## Cách Sử Dụng

### Cho Giáo Viên/Nhân Viên:
1. Vào biểu mẫu thông tin cá nhân
2. Chuyển đến tab "Work Planned"
3. Xem danh sách công ca được phê duyệt
4. Chỉ check-in/out trong thời gian công ca được phê duyệt

### Cho Quản Lý:
1. Vào **Human Resources → Attendances → Work Planned**
2. Tạo công ca mới hoặc chỉnh sửa công ca hiện tại
3. Phê duyệt hoặc từ chối công ca
4. Sử dụng bộ lọc để xem công ca theo tiêu chí cụ thể

## Tích Hợp với HR Attendance
- Module này tích hợp seamlessly với `hr_attendance`
- Chỉ những công ca được phê duyệt mới được xem xét trong tính toán attendance
- Giúp đảm bảo attendance accuracy và compliance

## Quyền Hạn
- **HR Employee**: Xem công ca của chính họ
- **HR Manager**: Quản lý công ca của nhân viên dưới quản lý
- **HR Attendance Officer**: Quản lý toàn bộ công ca

## Tính Năng Chi Tiết

### Tự Động Tính Toán:
- **Planned Hours**: Tự động tính từ Start Time và End Time
- **Date**: Tự động lấy từ Start Time

### Theo Dõi Thay Đổi:
- Tất cả thay đổi được ghi lại (Mail Thread)
- Có thể xem lịch sử thay đổi trong từng bản ghi

## Yêu Cầu
- Odoo 19
- Module `hr` được cài đặt
- Module `hr_attendance` được cài đặt

## Tác Giả
Module được tạo dựa trên Odoo Framework

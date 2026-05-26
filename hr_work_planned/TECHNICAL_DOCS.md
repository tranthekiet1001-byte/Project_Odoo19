# Technical Documentation - HR Work Planned Module

## Architecture Overview

### Model Structure

```
hr.work.planned (Main Model)
├── employee_id (M2O → hr.employee)
├── department_id (M2O → hr.department) [related]
├── manager_id (M2O → hr.employee) [related]
├── date_start (Datetime) - Scheduled start time
├── date_end (Datetime) - Scheduled end time
├── date (Date) - Computed from date_start
├── planned_hours (Float) - Computed duration
├── status (Selection) - draft/approved/rejected
├── description (Text)
└── color (Integer) - Computed for UI decoration

hr.employee (Extended Model)
└── work_planned_ids (O2M ← hr.work.planned)
```

### Module Dependencies

```
hr_work_planned
├── depends: ['hr', 'hr_attendance']
├── inherits:
│   ├── hr.employee
│   └── mail.thread (for hr.work.planned)
└── security groups:
    ├── hr.group_hr_employee
    ├── hr.group_hr_manager
    └── hr_attendance.group_hr_attendance_officer
```

## File Structure

```
hr_work_planned/
├── __init__.py                          # Package initialization
├── __manifest__.py                      # Module manifest
├── README.md                            # Module description
├── USAGE_GUIDE_VI.md                   # Vietnamese user guide
├── models/
│   ├── __init__.py
│   ├── hr_work_planned.py             # Main model definition
│   └── hr_employee.py                 # Employee extension
├── views/
│   ├── hr_work_planned_view.xml       # List/Form/Search views
│   └── hr_employee_view.xml           # Employee form extension
├── security/
│   └── ir.model.access.csv           # Record rules & access rights
└── data/
    └── (future data files)
```

## Key Features

### 1. Computed Fields

#### `_compute_date`
- **Purpose**: Extract date from date_start
- **Trigger**: `@api.depends('date_start')`
- **Store**: Yes (precompute=True)
- **Used for**: Date-based filtering

#### `_compute_planned_hours`
- **Purpose**: Calculate duration between date_end - date_start
- **Trigger**: `@api.depends('date_start', 'date_end')`
- **Store**: Yes
- **Formula**: `(date_end - date_start).total_seconds() / 3600.0`

#### `_compute_is_manager`
- **Purpose**: Check if current user is the employee's manager
- **Trigger**: `@api.depends('employee_id')`
- **Store**: No
- **Usage**: UI visibility control

#### `_compute_color`
- **Purpose**: Decoration color based on status
- **Trigger**: None (computed on read)
- **Values**: 
  - `10` (green) for approved
  - `1` (red) for rejected
  - `0` (default) for draft

### 2. Business Methods

#### `action_approve()`
- **Purpose**: Approve pending work shifts
- **Permission**: HR Manager / Officer
- **State Change**: draft → approved
- **Side Effects**: Triggers tracking

#### `action_reject()`
- **Purpose**: Reject pending work shifts
- **Permission**: HR Manager / Officer
- **State Change**: draft → rejected
- **Side Effects**: Triggers tracking

#### `action_reset_to_draft()`
- **Purpose**: Reset approved/rejected shifts back to draft
- **Permission**: HR Manager / Officer
- **State Change**: approved/rejected → draft
- **Usage**: Correct mistakes or update schedules

### 3. Security & Access Control

**Access Rules (ir.model.access.csv):**

| Role | Read | Write | Create | Delete |
|------|------|-------|--------|--------|
| HR Employee | ✓ | ✓ | ✓ | ✗ |
| HR Manager | ✓ | ✓ | ✓ | ✓ |
| HR Attendance Officer | ✓ | ✓ | ✓ | ✓ |

## Views

### 1. List View (`view_work_planned_list`)
- **Features**:
  - Action buttons in header (Approve/Reject/Reset)
  - Status badge with color decoration
  - Optional columns (Manager, Description, etc.)
  - Dual mode: desktop and mobile compatible

### 2. Form View (`view_work_planned_form`)
- **Layout**:
  - Header with status bar and action buttons
  - Title section with employee avatar
  - Main content in sheet (3-column layout)
  - Description field
  - Chatter for discussions

### 3. Search View (`view_work_planned_search`)
- **Search Fields**: Employee, Date, Department, Manager
- **Filters**:
  - Status filters (Approved/Rejected/Draft)
  - Time-based filters (Today/This Week/This Month)
- **Group By Options**: Employee, Date, Department, Status
- **Dynamic Filters**: Uses context_today() for relative dates

### 4. Kanban View (Mobile)
- **Card Layout**: Employee + Time Period + Status badge
- **Sample Data**: Included for demo

### 5. Employee Form Extension (`hr_employee_view.xml`)
- **Integration**: Adds "Work Planned" tab to employee form
- **Display**: Tree view of work_planned_ids
- **Inline Editing**: Disabled (create=false, edit=false, delete=false)
- **Context**: Pre-fills employee_id for new records

## Integration with HR Attendance

### Attendance Validation Logic (To be implemented)

```python
# Pseudo-code for attendance validation
def validate_attendance_in_planned_shift(attendance_record):
    """
    Check if attendance falls within approved work shifts
    """
    employee = attendance_record.employee_id
    check_in = attendance_record.check_in
    
    # Get approved planned shifts for this employee on this date
    approved_shifts = hr.work.planned.search([
        ('employee_id', '=', employee.id),
        ('status', '=', 'approved'),
        ('date_start', '<=', check_in),
        ('date_end', '>=', check_in),
    ])
    
    if approved_shifts:
        return True  # Attendance is valid
    else:
        return False  # Attendance should not be recognized
```

## Extending the Module

### Adding Custom Filters

Edit `hr_work_planned_view.xml`:

```xml
<filter name="custom_filter" string="My Filter" 
    domain="[('status', '=', 'approved'), ('manager_id', '=', uid)]"/>
```

### Adding Custom Fields

1. Extend the model in a new module:

```python
class HrWorkPlannedExtended(models.Model):
    _inherit = 'hr.work.planned'
    
    custom_field = fields.Char("Custom Field")
```

2. Update the view in your extension module.

### Adding Approval Workflow

```python
def action_send_for_approval(self):
    """Send shift for manager approval"""
    self.write({'status': 'pending_approval'})
    # Notify manager via email/notification
```

## Known Limitations

1. **Soft Delete Only**: Records are not truly deleted (set to rejected)
2. **No Recurring Shifts**: Each shift must be created individually
3. **No Automatic Sync**: Manual creation required (no automatic import from calendar)
4. **No Notification System**: Approvals don't auto-notify employees
5. **Simple Status Model**: Only 3 states (could be extended to workflow)

## Future Enhancements

1. **Recurring Schedules**: Support weekly/monthly recurring patterns
2. **Calendar Integration**: View/create shifts from calendar widget
3. **Bulk Import**: Import schedules from Excel/CSV
4. **Notifications**: Email/app notifications for approvals
5. **Overtime Rules**: Automatic overtime detection for shifts > 8 hours
6. **Shift Templates**: Pre-defined shift patterns
7. **Manager Dashboard**: Approval queue and statistics
8. **Mobile App**: Mobile check-in validation against planned shifts

## Performance Considerations

### Database Indexes

- `employee_id`: Many employees → frequent filtering
- `date_start`: Time-range queries common
- `status`: Status-based filtering frequent
- `date`: Date-based grouping

### Optimization Tips

1. **Use domain pre-filters** when searching for employee shifts
2. **Batch operations** for bulk approvals
3. **Limit date ranges** in reports
4. **Archive old records** periodically

## Testing

### Test Cases (to be created)

1. Create work planned record
2. Approve/Reject operations
3. Reset to draft
4. Computed fields accuracy
5. Security/Access control
6. Date filtering
7. Employee view tab display

## Deployment

### Pre-Installation Checklist

1. ✓ `hr` module installed
2. ✓ `hr_attendance` module installed
3. ✓ Database backup created
4. ✓ HR settings configured

### Installation Steps

```bash
# In Odoo shell
./odoo-bin -d database_name -u hr_work_planned
```

### Post-Installation

1. Verify menu appears in HR module
2. Create sample work planned record
3. Test approval workflow
4. Verify employee form tab displays
5. Check security rules

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Tab not visible | Module not installed | Re-install via `odoo-bin -u hr_work_planned` |
| Can't approve | Wrong permission | Grant HR Manager role |
| Hours not calculated | date_end not set | Ensure both date_start and date_end are filled |
| Filter not working | Incorrect syntax | Check filter domain syntax |

## Code Quality

- **Lines of Code**: ~300
- **Models**: 2 (main + extension)
- **Views**: 5 (list, form, kanban, search, employee)
- **Security**: 3 access rules
- **Documentation**: README + Usage Guide + Technical docs

## Version History

- **v1.0** (Initial Release)
  - Basic work planned model
  - Approval workflow
  - Employee form integration
  - Security and access control

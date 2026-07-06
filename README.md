# Odoo Student Management Module

A comprehensive and simple Odoo module designed to manage students and courses effectively within an educational institution.

## 🚀 Features

* **Student Management**: Register students with their details such as Name, Email, Roll Number, and Department.
* **Course Management**: Create and manage courses, including Course Name, Code, and Credit hours.
* **Enrollment System**: Easily enroll students into multiple courses using a many-to-many relationship.
* **Quick Access**: Built-in action buttons to quickly view all courses a specific student is enrolled in directly from the student's profile.
* **Reporting**: Includes a predefined report structure (`student_report.xml`) for generating student data reports.
* **Secure**: Basic security implementations using `ir.model.access.csv` to ensure proper access rights.

## 📂 Module Structure

```text
student_management/
├── models/
│   ├── student.py       # Defines the Student model and fields
│   └── course.py        # Defines the Course model and fields
├── views/
│   ├── student_view.xml # UI views (Tree, Form) for Students
│   └── course_view.xml  # UI views (Tree, Form) for Courses
├── report/
│   └── student_report.xml # PDF report templates for students
├── security/
│   └── ir.model.access.csv # Access rights and security rules
├── __init__.py          # Module initialization
└── __manifest__.py      # Module configuration and metadata
```

## 🛠️ How to Install and Test

1. Place the `student_management` folder inside an `addons` directory for Odoo.
2. Add the path to this `addons` directory in your `odoo.conf` file (e.g., `addons_path = /path/to/odoo/addons,/path/to/your/custom/addons`).
3. Restart the Odoo service to apply the configuration changes.
4. Log into Odoo and activate **Developer Mode** (Settings -> Activate the developer mode).
5. Go to the **Apps** menu and click on **Update Apps List** in the top menu bar.
6. Search for `Student Management` in the apps list. Remove the "Apps" filter if necessary.
7. Click the **Activate** (or Upgrade) button to install the module.
8. Once installed, the **Student Management** menu will appear on the main dashboard, allowing you to start managing your data.

## 👤 Author

* **Mohibur Rahman Sani**

## 📄 License

This project is licensed under the Odoo Proprietary License v1.0. Please refer to Odoo's standard licensing policies for more details.

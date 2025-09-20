# Odoo Student Management Module
## How to Install and Test
1.  Place the `student_management` folder inside an `addons` directory for Odoo.
2.  Add the path to this `addons` directory in your `odoo.conf` file.
3.  Restart the Odoo service.
4.  In Odoo, activate developer mode.
5.  Go to the "Apps" menu and select "Update Apps List".
6.  Search for "Student Management" and click the "Activate" / "Upgrade" button.
7.  The "Student Management" menu will appear on the main dashboard.

## Challenges Faced

A key challenge was understanding Odoo's security layer. The module failed to install initially due to missing access rights. I solved this 
by creating the `security/ir.model.access.csv` file to grant the base user group permissions to read, write, create, and delete records for 
the new Student and Course models. This taught me that defining model permissions is a mandatory and critical step in Odoo development.

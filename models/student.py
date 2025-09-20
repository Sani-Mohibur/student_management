from odoo import models, fields

class Student(models.Model):
    _name = 'student.management.student'
    _description = 'Student Information'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    roll_no = fields.Char(string='Roll No')
    department = fields.Char(string='Department')

    # Many2many relation with Course model
    course_ids = fields.Many2many(
        'student.management.course',
        string='Enrolled Courses'
    )

    def action_show_enrolled_courses(self):
        return {
            'name': 'Enrolled Courses',
            'type': 'ir.actions.act_window',
            'res_model': 'student.management.course',
            'view_mode': 'tree,form',
            'target': 'current',
            'domain': [('id', 'in', self.course_ids.ids)],
        }
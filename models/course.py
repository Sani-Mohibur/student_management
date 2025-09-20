from odoo import models, fields

class Course(models.Model):
    _name = 'student.management.course'
    _description = 'Course Information'

    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Course Code')
    credit = fields.Float(string='Credit')

    student_ids = fields.Many2many(
        'student.management.student',
        string='Students'
    )
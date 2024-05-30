from odoo import fields, models


class QueueJobFunction(models.Model):
    _inherit = "queue.job.function"

    is_web_notify_done_enabled = fields.Boolean(
        string="Notify on Done",
        help="Display a notification in the user interface when the job done.",
        default=False,
    )

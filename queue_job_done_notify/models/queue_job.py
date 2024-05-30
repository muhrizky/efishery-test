# Copyright 2024 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, models


class QueueJob(models.Model):
    _inherit = "queue.job"

    def write(self, vals):
        if vals.get("state") == "done":
            self._message_post_on_done()
        return super(QueueJob, self).write(vals)

    def _get_web_notify_done_title(self):
        self.ensure_one()
        return _("Job Done")

    def _get_web_notify_done_message(self):
        self.ensure_one()
        return self.display_name

    def _message_post_on_done(self):
        for job in self:
            if not job.job_function_id.is_web_notify_done_enabled:
                continue
            notification_title = job._get_web_notify_done_title()
            notification_message = job._get_web_notify_done_message()
            job.user_id.notify_success(
                message=notification_message, title=notification_title, sticky=True
            )

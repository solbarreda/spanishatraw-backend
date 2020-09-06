"""Email sender."""

from django.core.mail import send_mail
from django.template.loader import render_to_string


class EmailSender:
    """Email sender."""

    def __init__(self, html_template, text_template):
        """Email sender."""
        self.html_template = html_template
        self.text_template = text_template

    def send_email(
            self, subject, sender, recipient, email_context={}):
        """Send email to a recipient.

        :param subject: Email subject.
        :param message: Message
        :param sender: Sender
        :param recipient: Recipient
        :param email_context: email template context, defaults to {}
        """
        text = render_to_string(self.text_template, email_context)
        html = render_to_string(self.html_template, email_context)

        send_mail(
            subject=subject,
            message=text,
            from_email=sender,
            recipient_list=[recipient],
            html_message=html,
            fail_silently=False,
        )

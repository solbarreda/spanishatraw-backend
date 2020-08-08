from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Testimonial(models.Model):
    """
    Testimonials model.

    :cvar user: User related.
    :cvar content: Testimonial content.
    :cvar timestamp: Testimonial creation time.
    """

    user = models.ForeignKey(
        verbose_name='User', to=get_user_model(), on_delete=models.DO_NOTHING)
    content = models.TextField(
        verbose_name='Content', blank=False, null=False)
    timestamp = models.DateTimeField(
        verbose_name='Timestamp', auto_now_add=True, null=False)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        """Testimonial name."""
        return f'{self.user.email} Testimonial.'


class ContactUs(models.Model):
    """
    Contact Us model.

    :cvar user: User related.
    :cvar subject: Message subject.
    :cvar description: Message description.
    """

    user = models.ForeignKey(
        verbose_name='User', to=get_user_model(), on_delete=models.DO_NOTHING)
    description = models.TextField(
        verbose_name='Description', blank=False, null=False)
    subject = models.CharField(
        verbose_name='Subject', max_length=256, null=False, blank=False)

    class Meta:
        verbose_name = 'Contact us'
        verbose_name_plural = 'Contact us'

    def __str__(self):
        """Contact us name."""
        return f'{self.user.email} - {self.subject.title()}'


class Feature(models.Model):
    """
    Feature model.

    :cvar name: Feature name.
    :cvar description: Feature description.
    """

    name = models.CharField(
        verbose_name='Name', max_length=256, null=False, blank=False)
    description = models.TextField(
        verbose_name='Description', blank=False, null=False)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        """Feature name."""
        return self.name.title()


class EvidenceGallery(models.Model):
    """
    Evidence gallery.

    :cvar name: Feature name.
    :cvar description: Feature description.
    :cvar :
    """

    name = models.CharField(
        verbose_name='Name', max_length=256, null=False, blank=False)
    description = models.TextField(
        verbose_name='Description', blank=False, null=False)
    image = models.ImageField(
        verbose_name='Evidence image', upload_to='evidence', max_length=256,
        null=False)

    class Meta:
        verbose_name = 'Evidence Gallery'
        verbose_name_plural = 'Evidences Gallery'

    def __str__(self):
        """Evidence Gallery name."""
        return self.name.title()

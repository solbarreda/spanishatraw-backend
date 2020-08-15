from django.db import models


class GradeRange(models.Model):
    """
    Grade ranges for each service.

    :cvar min: Minimum age.
    :cvar max: Maximum age.
    """

    min = models.CharField(verbose_name='Minimum',
                           max_length=64, null=False, blank=False)
    max = models.CharField(verbose_name='Maximum',
                           max_length=64, null=False, blank=False)

    class Meta:
        verbose_name = 'Grade range'
        verbose_name_plural = 'Grade ranges'

    def __str__(self):
        """Grade range."""
        return f'From {self.min} to {self.max}'


class Homework(models.Model):
    """
    Homeworks associated to services.

    :cvar file: File associated.
    :cvar description: Description of the homework.
    :cvar name: Homework name.
    :cvar service: Service associated.
    """

    file = models.FileField(
        verbose_name='Homework file', upload_to='homeworks')
    description = models.TextField(
        verbose_name='Description', blank=False, null=False)
    name = models.CharField(
        verbose_name='Name', max_length=128, null=False, blank=False)
    service = models.ForeignKey(
        verbose_name='Service', to='services.Service',
        related_name='homeworks', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Homerwork'
        verbose_name_plural = 'Homeworks'

    def __str__(self):
        """Homework name."""
        return self.name.title()


class ServiceLevel(models.Model):
    """
    Service level

    :cvar description: Charfield, level description
    """

    description = models.CharField(
        verbose_name='description', max_length=128, null=False, blank=False)

    class Meta:
        verbose_name = 'Service Level'
        verbose_name_plural = 'Service Levels'

    def __str__(self):
        """Service level."""
        return f'{self.description}'


class ServiceType(models.Model):
    """
    Service Type

    :cvar description: Charfield, type description
    """

    description = models.CharField(
        verbose_name='description', max_length=128, null=False, blank=False)

    class Meta:
        verbose_name = 'Service Type'
        verbose_name_plural = 'Service Types'

    def __str__(self):
        """Service Type."""
        return f'{self.description}'


class Service(models.Model):
    """
    Service offered.

    :cvar name: Service name.
    :cvar timestamp: Creation date.
    :cvar image: Image associated.
    :cvar schedule: Schedule of service.
    :cvar price: Service price.
    :cvar age_range: Service age range.
    :cvar homeworks: homeworks associated.
    """

    name = models.CharField(
        verbose_name='Name', max_length=128, null=False, blank=False)
    timestamp = models.DateTimeField(
        verbose_name='Timestamp', auto_now_add=True, null=False)
    image = models.ImageField(
        verbose_name='Service image', upload_to='services', max_length=256,
        null=False)
    schedule = models.JSONField(verbose_name='Schedule', null=False)
    price = models.ForeignKey(
        verbose_name='Price', to='payment.Price', on_delete=models.CASCADE)
    grade_range = models.ForeignKey(
        verbose_name='Grade range', to='services.GradeRange',
        on_delete=models.CASCADE)
    level = models.ForeignKey(
        verbose_name='Service level', to='services.ServiceLevel',
        on_delete=models.CASCADE)
    type = models.ForeignKey(
        verbose_name='Service type', to='services.ServiceType',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        """Service name."""
        return self.name.title()

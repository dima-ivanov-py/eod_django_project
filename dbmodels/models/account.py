from django.db import models


class Account(models.Model):
    class Types(models.TextChoices):
        SELLER = 'seller'
        CUSTOMER = 'customer'

    user = models.ForeignKey(
        to='auth.User',
        on_delete=models.CASCADE,
        related_name='accounts',
    )
    type = models.CharField(
        max_length=255,
        choices=Types.choices,
    )

    class Meta:
        unique_together = ('user', 'type')

    def __str__(self):
        return f'{self.user.username}: {self.type}'

from django.db import models


class UniqueToken(models.Model):
    token = models.CharField(
        max_length=255,
        unique=True,
    )
    ut_from = models.ForeignKey(
        to="self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="unique_tokens_from",
    )
    ut_main = models.ForeignKey(
        to="self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="unique_tokens_main",
    )
    owner = models.OneToOneField(
        to="auth.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="unique_token",
    )

    def __str__(self) -> str:
        return self.token

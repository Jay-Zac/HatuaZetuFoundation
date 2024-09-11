from django.db import models


class Donation(models.Model):
    objects = None  # For unresolved attribute referencing
    name = models.CharField(max_length=100)  # The name of the donor
    email = models.EmailField()  # The donor's email address
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # The amount donated
    message = models.TextField(blank=True, null=True)  # An optional message from the donor
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the donation was created

    class Meta:
        ordering = ('-created_at',)  # Order by creation date (newest first)

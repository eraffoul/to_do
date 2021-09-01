from django.db import models


class ToDo(models.Model):
    # The description of the to-do
    description = models.CharField(max_length=200, blank=False)
    # The date that the to-do item was registered
    created_at = models.DateTimeField(auto_now_add=True)
    # Primary key of the object
    id = models.IntegerField(primary_key=True)


    """ 
    I thought to add an order field, but given that the id is auto incremental
    and no new to-do item could be added on a date before an existing one, it would
    be the same behavior to order by date or by id, which is implicitly done by the
    primary_key constraint
    """


    # An echo of the object should return the description itself
    def __str__(self):
        return self.description


    # No blank description should be allowed on the list
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.description == '':
            raise ValidationError('The description can not be empty')
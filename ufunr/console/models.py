from django.db import models

# Create your models here.
class User(models.Model):
    account_id = models.CharField(max_length=20)
    valid_days = models.IntegerField(default=375)
    data_left = models.FloatField(default=10240)

    YES = 'YES'
    NO = 'NO'
    
    IS_DELETED = (
       (YES, 'YES'),
       (NO, 'NO')
    )
    is_deleted = models.CharField(max_length=10,
                                choices=IS_DELETED,
                                default=NO)

    def __str__(self):
        return self.account_id

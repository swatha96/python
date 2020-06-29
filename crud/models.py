from django.db import models
class EmployeeModel(models.Model):
    eid = models.CharField(max_length=10)
    ename = models.CharField(max_length=30)
    email = models.EmailField( max_length=254)
    emobile = models.BigIntegerField()
    class Meta:
        db_table="emp"
    

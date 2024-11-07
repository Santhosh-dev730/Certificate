from djongo import models

class certificate(models.Model):
    _id = models.ObjectIdField(primary_key=True) 
    reg_no=models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    email=models.EmailField(max_length=20)
    course=models.TextField()
    trainer=models.CharField(max_length=20)
    
    
    @property
    def mongo_id(self):
        return str(self._id) 
    
    def __str__(self):
        return self.name
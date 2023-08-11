from django.db import models

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=128) #строковое поле, используется для строк НЕБОЛЬШИХ размеров
    description = models.TextField("Описание") #строковое поле, используется для строк БОЛЬШИХ размеров
    price = models.DecimalField("цена", max_digits=10, decimal_places=2) #числовое поле, которое может содержать десятичное число с фиксированной точностью
    # 999.99 max_digits = 5, decimal_places = 2
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен") #True and False 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Advertisements_up(models.Model):
    def __str__(self): 
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
    id = models.CharField("id", max_length=64, primary_key=True)
    title = models.CharField("заголовок", max_length=128) #строковое поле, используется для строк НЕБОЛЬШИХ размеров
    description = models.TextField("Описание") #строковое поле, используется для строк БОЛЬШИХ размеров
    price = models.DecimalField("цена", max_digits=10, decimal_places=2) #числовое поле, которое может содержать десятичное число с фиксированной точностью
    # 999.99 max_digits = 5, decimal_places = 2
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен") #True and False 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    class Meta: 
        db_table = 'advertisements'
        


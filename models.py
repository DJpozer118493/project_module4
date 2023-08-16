from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=100) #строковое поле, используется для строк НЕБОЛЬШИХ размеров
    description = models.TextField("Описание") #строковое поле, используется для строк БОЛЬШИХ размеров
    price = models.DecimalField("цена", max_digits=10, decimal_places=2) #числовое поле, которое может содержать десятичное число с фиксированной точностью
    # 999.99 max_digits = 5, decimal_places = 2
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен") #True and False 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:$S')
            return format_html(
                "<span style='color:green; font-weight: bold'>Сегодня в {}</span>",
                created_time
            )
        return self.created_at.strftime('%d.%m.%Y at %H:%M:%S')
    

    @admin.display(description='дата дата обновления')
    def update_date(self):
        if self.updated_at.date() == timezone.now().date():
            update_time = self.created_at.time().strftime('%H:%M:$S')
            return format_html(
                "<span style='color:blue; font-weight: bold'>Сегодня в {}</span>",
                update_time
            )
        return self.updated_at.strftime('%d.%m.%Y at %H:%M:%S')
    
#http://127.0.0.1:8000/admin
    
    

        


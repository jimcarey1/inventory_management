from django.db import models
from item.models import Item

class Stock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='stock')
    quantity = models.PositiveIntegerField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    
    def __str__(self):        
        return f"Stock of {self.item.name}"
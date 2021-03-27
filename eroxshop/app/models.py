from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.
STATE_CHOICES = (('KA', 'Karnataka'),
 ('AP', 'Andhra Pradesh'), ('KL', 'Kerala'), ('TN', 'Tamil Nadu'), ('MH', 'Maharashtra'), ('UP', 'Uttar Pradesh'),
  ('GA', 'Goa'), ('GJ', 'Gujarat'), ('RJ', 'Rajasthan'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), 
  ('TG', 'Telangana'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chattisgarh'), 
  ('HR', 'Haryana'), ('JH', 'Jharkhand'), ('MP', 'Madhya Pradesh'), ('MN', 'Manipur'), ('ML', 'Meghalaya'),
   ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Orissa'), ('PB', 'Punjab'), ('SK', 'Sikkim'), ('TR', 'Tripura'), 
   ('UA', 'Uttarakhand'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar'), ('CH', 'Chandigarh'),
    ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('LD', 'Lakshadweep'),
    ('PY', 'Pondicherry'))

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES=(('M','MOBILE'),
                  ('L','LAPTOP'),
                  ('TW','TOPWEAR'),
                  ('BW','BOTTOMWEAR'))

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

STATUS_CHOICES=(('Accepted','Accepted'),
                ('Packed','Packed'),
                ('On The Way','On The Way'),
                ('Delievered','Delievered'),
                ('Cancel','Cancel'))

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS_CHOICES,max_length=50,default='Pending')



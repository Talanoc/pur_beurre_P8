from django.db import models

# Create your models here.

class User_db(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    user_pw = models.CharField(max_length=50)



class Db_product(models.Model):
    code = models.IntegerField
    url =  models.URLField()   #url fiche article 
    product_name = models.CharField(max_length=200)
    categories = models.CharField(max_length=200)
    nutriscore_grade = models.CharField(max_length=2)
    image_url = models.URLField()



class Favorite_db(models.Model):
    id_product = models.ForeignKey(Db_product , on_delete=models.CASCADE)
    id_user = models.ForeignKey(User_db ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
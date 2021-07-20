from django.db import models

class TimesModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User_db(TimesModel):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    user_pw = models.CharField(max_length=50)

    def __str__(self):
        return self.name,self.email,self.user_pw,self.created_at,self.updated_at

class Category_db(models.Model):
    category = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.category

class Db_product(models.Model):
    code = models.IntegerField()
    url =  models.URLField()   #url fiche article 
    product_name = models.CharField(max_length=200)
    nutriscore_grade = models.CharField(max_length=2)
    image_url = models.URLField()
    image_small_url = models.URLField()
    categories = models.ManyToManyField(Category_db)

    def __str__(self):
        return self.code,self.url,self.product_name,self.category_id,self.nutriscore_grade,self.image_url

class Favorite_db(TimesModel):
    id_product = models.ForeignKey(Db_product , on_delete=models.CASCADE)
    id_user = models.ForeignKey(User_db ,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.id_product,self.id_user,self.created_at,self.updated_at






    

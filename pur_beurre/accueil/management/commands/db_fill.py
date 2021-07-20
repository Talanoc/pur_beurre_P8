# -*- coding: utf-8 -*-
from accueil.models import Category_db,Db_product
from django.core.management.base import BaseCommand
import requests,json

categories = [
    "Laits",
    "Poissons",
    "Viandes",
    "Desserts",
    "Plats préparés surgelés",
    "Fromages de France",
    "Bonbons",
    "Pains"
    ]

chosen_fields = [
    "url",
    "product_name_fr",
    "nutriscore_grade",
    "image_url",
    "image_small_url",
    "code",
    "categories"
    ]

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        Command.fill_cat()
        Command.import_data()
        #cat=Category_db.objects.filter(id=5)
        #cat2=Category_db.objects.count()
        #cat3=Category_db.objects.all()
        # print (cat,cat2)        
    def fill_cat():     
        for cat in categories:
            try:                   
                Category_db.objects.create(category=cat)
                print(cat + ' ajoutée à la table !!')
            
            except :
                print(cat + ' déjà dans la table !!')
                pass
    
    def import_data():
        categories=Category_db.objects.all()
        #print(categories)
        search_url = "https://fr.openfoodfacts.org/cgi/search.pl?"
        headers = {"User-Agent": "P8_PurBeurre - Version 1.0"}

        for category in categories:

            i = 1
            products_resu = []
            for i in range(1, 2):
                payload = {"action": "process",
                           "tagtype_0": "categories",
                           "tag_contains_0": "contains",
                           "tag_0": category,
                           "tagtype_1": "countries",
                           "tag_contains_1": "contains",
                           "tag_1": "france",
                           "tagtype_2": "categories_lc",
                           "tag_contains_2": "contains",
                           "tag_2": "fr",
                           # Sort by popularity
                           "sort_by": "unique_scans_n",
                           "page": 1,
                           "page_size": 5,
                           "json": True}

                req = requests.get(search_url, params=payload, headers=headers)
                results_json = req.json()
                products_json = results_json["products"]
                o=0
                for product in products_json:
                    o+=1
                    print(o)
                    product_resu = {
                                key: value for key, value in product.items()
                                if key in chosen_fields and value != " "
                             } 
                    try: 
                        print (product_resu["url"],product_resu["product_name_fr"])      
                        Db_product.objects.create(
                            code=product_resu["code"],
                            url=product_resu["url"],
                            product_name_fr=product_resu["product_name_fr"],nutriscore_grade=product_resu["nutriscore_grade"],image_url=product_resu["image_url"],
                            image_small_url=product_resu["image_small_url"])                            
                    except :
                        next
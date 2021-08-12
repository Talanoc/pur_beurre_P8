# -*- coding: utf-8 -*-
from accueil.models import Category, Product
from django.core.management.base import BaseCommand
import requests
import json
from django.db import IntegrityError


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
    "categories",
    "tag_0"
    ]


class Command(BaseCommand):

    def handle(self, *args, **options):
        Command.fill_cat()
        Command.import_data()

    def fill_cat():
        for cat in categories:
            try:
                Category.objects.update_or_create(category=cat)
                print(cat + ' ajoutée à la table !!')

            except:
                print(cat + ' déjà dans la table !!')

    def import_data():
        cat = Category.objects.all()
        search_url = "https://fr.openfoodfacts.org/cgi/search.pl?"
        headers = {"User-Agent": "P8_PurBeurre - Version 1.0"}

        for category in cat:
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
                           "page": i,
                           "page_size": 50,
                           "json": True}

                req = requests.get(search_url, params=payload, headers=headers)
                results_json = req.json()
                products_json = results_json["products"]

                for product in products_json:
                    product_resu = {
                                key: value for key, value in product.items()
                                if key in chosen_fields and value != " "
                             }
                    cats = product_resu['categories'].split(',')
                    try:

                        for cat in cats:
                            Category.objects.update_or_create(category=cat)

                            product=Product.objects.update_or_create(
                                code=product_resu["code"],
                                url=product_resu["url"],
                                product_name=product_resu["product_name_fr"],
                                nutriscore_grade=product_resu["nutriscore_grade"],
                                image_url=product_resu["image_url"],
                                image_small_url=product_resu["image_small_url"]
                            )

                            cate = Category.objects.get(category=cat)
                            Product.objects.get(code=product_resu["code"]).categories.add(cate)
                    except:
                        print('erreur de chargement')

from django.shortcuts import render,redirect
from accueil.models import Product,Category
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.db.models import Count
# Create your views here.


def search_product(request):

    if request.method == "GET":
        search1 = request.GET.get("search1")
        replacement=[]
        if search1 != "":
            search = list(Product.objects.filter(product_name__contains=search1))[:1]


            for x in search:
                search_id = x.id
                print(search_id)
                categories = Product.objects.get(id=search_id).categories.all()
                #print(categories)

            for category in categories:
                category_id = list(Category.objects.filter(category__contains=category))
               

                for categorie_id in category_id:
                    print("il y a ", (len(category_id)), "articles dans la ",category)
                    if (len(category_id)) >= 6:
                        print(category)
                        categories = categorie_id.id
                        print(categorie_id, categories)
                        replacement = (Product.objects.filter(categories=categories).order_by("nutriscore_grade").values())[:6]
                        print(replacement)
                        print(len(replacement))
                        break
                    else:
                        pass
                        #print("la"+ category +"ne contient pas assez d'articles")

            context = {
                
                "product": search,
                "replacement": replacement
                
            }
            return render(request, "search_product.html", context)       
    else:

        return(redirect("index.html"))


def index(request):

    return render(request, "search_product.html")





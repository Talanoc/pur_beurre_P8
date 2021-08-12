from django.shortcuts import render

# Create your views here.
def user(request):
    return render(request, "user.html")

def user_identification(request):
    if request.method == "POST":
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_password=request.POST.get("password")

        print(user_name,user_email,user_password)

        context= (user_name,user_email,user_password)
        
        if name != "":

            return render(request, "index")
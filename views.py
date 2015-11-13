#from django.shortcuts import render
from models import People,User
# Create your views here.
from django.template import Context
from django.shortcuts import render_to_response 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def addr_book(request):
    if request.POST:
        post = request.POST
        new_people = People(
            user=request.user,
            name = post["name"],
            number = post["number"],
            phone = post["phone"],
            email = post["email"],
            qq = post["qq"],
            birth = post["birth"],
            address = post["address"])    
        if post["sex"] == 'M':
            new_people.sex = True
        else:
            new_people.sex = False       
        new_people.save()
    return render_to_response("import.html")        
        
        
def table(request):
    count = People.objects.filter(user=request.user).count()
    people_list = People.objects.filter(user=request.user)
    c = Context({"people_list":people_list,"count":count})    
    return render_to_response("scanf.html", c)
def delete(request):
    delete_id  =request.GET["id"]
    People.objects.filter(id = delete_id).delete()
    people_list= People.objects.filter(user=request.user)
    c = Context({"people_list":people_list}) 
    return render_to_response("scanf.html",c)
    
def change(request):
    change_id  =request.GET["id"]
    new_people=People.objects.get(id = change_id)
    if request.POST:
        post = request.POST 
        user=request.user
        new_people.name = post["name"]
        new_people.number = post["number"]
        new_people.phone = post["phone"]
        new_people.email = post["email"]
        new_people.qq = post["qq"]
        new_people.birth = post["birth"]
        new_people.address = post["address"]    
        if post["sex"] == 'M':
            new_people.sex = True
        else:
            new_people.sex = False       
        new_people.save()
    c = Context({"new_people":new_people,})
    return render_to_response("change.html",c)  
def search(request):

    
    post=request.POST['search']
    user = request.user
    print post
    p=People.objects.filter(user=request.user,name = post)
    print len(p)
    if len(p)==0:
        return render_to_response("no_result.html")  
    c=Context({"people_list":p})
    return render_to_response("scanf.html",c)  
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/login/")
    else:
        form = UserCreationForm()
    return render_to_response("create.html", {
        'form': form,
    })
def changepass(request):
    if request.POST:
        get_secret=request.POST["new_secret"]
        user=User.objects.get(username=request.user.username)
        user.set_password(get_secret)
        user.save()
    return render_to_response("changepass.html")
    
     
    
    
    
    
    













    
    

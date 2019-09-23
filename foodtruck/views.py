from django.shortcuts import render, get_object_or_404, redirect
from .models import Foodtruck, FoodtruckComment
from .forms import FoodtruckCommentForm
from django.db.models import Avg
from django.db import models

# Create your views here.

def foodtruck(request):
    foodtrucks = Foodtruck.objects.all
    return render(request, "foodtruck/foodtruck.html", {'foodtrucks' : foodtrucks})

def foodtruck_detail_korean(request):
    categorized = Foodtruck.objects.filter(ftCategory='korean')
    comments = FoodtruckComment.objects.all
    return render(request, "foodtruck/foodtruck_detail_korean.html", {'categorized':categorized, 'comments':comments})

def foodtruck_review_korean(request, index):
    this_foodtruck = get_object_or_404(Foodtruck, pk=index)
    if request.method == 'POST':
        form = FoodtruckCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.foodtruck = this_foodtruck
            comment.save()
            i = 0
            sum = 0
            for ftr in FoodtruckComment.objects.filter(foodtruck=this_foodtruck):
                ftr = ftr.ftRating
                i = i+1
                sum = sum + ftr
            average = sum/i
            this_foodtruck.generalRating = average
            this_foodtruck.save()
            return redirect("foodtruck:foodtruck_detail_korean")
    else:
        form = FoodtruckCommentForm()
        # this_foodtruck.generalRating =  FoodtruckComment.objects.all().aggregate(avg_rate = Avg(FoodtruckComment.ftRating, output_field=models.FloatField(),))
    return render(request, 'foodtruck/foodtruck_review.html', {'this_foodtruck':this_foodtruck, 'form':form})

def foodtruck_detail_western(request):
    categorized = Foodtruck.objects.filter(ftCategory='western')
    comments = FoodtruckComment.objects.all
    return render(request, "foodtruck/foodtruck_detail_western.html", {'categorized':categorized, 'comments':comments})

def foodtruck_review_western(request, index):
    this_foodtruck = get_object_or_404(Foodtruck, pk=index)
    if request.method == 'POST':
        form = FoodtruckCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.foodtruck = this_foodtruck
            comment.save()
            i = 0
            sum = 0
            for ftr in FoodtruckComment.objects.filter(foodtruck=this_foodtruck):
                ftr = ftr.ftRating
                i = i+1
                sum = sum + ftr
            average = sum/i
            this_foodtruck.generalRating = average
            this_foodtruck.save()
            return redirect("foodtruck:foodtruck_detail_western")
    else:
        form = FoodtruckCommentForm()
    return render(request, 'foodtruck/foodtruck_review.html', {'this_foodtruck':this_foodtruck, 'form':form})

def foodtruck_detail_dessert(request):
    categorized = Foodtruck.objects.filter(ftCategory='dessert')
    comments = FoodtruckComment.objects.all
    return render(request, "foodtruck/foodtruck_detail_dessert.html", {'categorized':categorized, 'comments':comments})

def foodtruck_review_dessert(request, index):
    this_foodtruck = get_object_or_404(Foodtruck, pk=index)
    if request.method == 'POST':
        form = FoodtruckCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.foodtruck = this_foodtruck
            comment.save()
            i = 0
            sum = 0
            for ftr in FoodtruckComment.objects.filter(foodtruck=this_foodtruck):
                ftr = ftr.ftRating
                i = i+1
                sum = sum + ftr
            average = sum/i
            this_foodtruck.generalRating = average
            this_foodtruck.save()
            return redirect("foodtruck:foodtruck_detail_dessert")
    else:
        form = FoodtruckCommentForm()
    return render(request, 'foodtruck/foodtruck_review.html', {'this_foodtruck':this_foodtruck, 'form':form})

def foodtruck_detail_etc(request):
    categorized = Foodtruck.objects.filter(ftCategory='etc')
    comments = FoodtruckComment.objects.all
    return render(request, "foodtruck/foodtruck_detail_etc.html", {'categorized':categorized, 'comments':comments})

def foodtruck_review_etc(request, index):
    this_foodtruck = get_object_or_404(Foodtruck, pk=index)
    if request.method == 'POST':
        form = FoodtruckCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.foodtruck = this_foodtruck
            comment.save()
            i = 0
            sum = 0
            for ftr in FoodtruckComment.objects.filter(foodtruck=this_foodtruck):
                ftr = ftr.ftRating
                i = i+1
                sum = sum + ftr
            average = sum/i
            this_foodtruck.generalRating = average
            this_foodtruck.save()
            return redirect("foodtruck:foodtruck_detail_etc")
    else:
        form = FoodtruckCommentForm()
    return render(request, 'foodtruck/foodtruck_review.html', {'this_foodtruck':this_foodtruck, 'form':form})



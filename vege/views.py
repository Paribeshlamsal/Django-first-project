from django.shortcuts import render

def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name=data.get('name')
        recipe_description=data.get('description')
        recipe_image=request.FILES.get('image')

        print(recipe_name)
        print(recipe_description)
        print(recipe_image)
    return render(request, 'recipe.html')

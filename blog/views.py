from django.shortcuts import render

# create a hard coded data, a list of dictionary
posts = [
    {
        'author': "Seven",
        'title': 'Blog 1',
        'content': 'First Blog',
        'date_posted': 'August 27, 2022'
    },
    {
        'author': "Elsa",
        'title': 'Blog 2',
        'content': 'First Blog too',
        'date_posted': 'August 28, 2022'
    }
]

def home(request):
    # context is a dictionary, the key of the context is posts, which is accessible from the templates, pass posts data to posts key
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

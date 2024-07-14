from django.shortcuts import render
from django.http import Http404
from .fake_db.pages import FAKE_DB_PAGES

FAKE_DB_CAROUSEL = [
    f"http://picsum.photos/id/{id}/600/400" for id in range(51,55)
]

def home(request):
    context = dict(
        page_title = "Home",
        FAKE_DB_CAROUSEL = FAKE_DB_CAROUSEL,
    )
    return render(request, "page/home.html", context)

def page(request, slug):
    result = list(filter(lambda x: (x["url"] == slug), FAKE_DB_PAGES))
    if result:    
        title = result[0]["title"]
        context = dict(
            page_title = title,
            hero_title = title,
            content = result[0]["content"],
        )
        return render(request, "page/page_temp.html", context)
    raise Http404()
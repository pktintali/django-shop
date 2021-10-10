from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Product
from tags.models import TaggedItem


def say_hello(request):
    # collection = Collection.objects.get(pk=11)
    # #Update Carefully
    # collection.featured_product=None
    # collection.save()

    Collection.objects.filter(pk=11).update(featured_product=None)
    return render(
        request, "hello.html", {"name": "Pradeep Kumar",}
    )

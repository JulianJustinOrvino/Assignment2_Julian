from django.shortcuts import render
from mywatchlist.models import MyWatchListItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_watchlist = MyWatchListItem.objects.all()
    times = 0
    for x in data_watchlist:
        if("yes" == x.watched):
            times += 1
    if(times > 4):
        msg_bonus = "Congratulations, you have watched movies a lot!"
    else:
        msg_bonus = "Woah, you have not much watched movies!"

    context = {
        'list_item': data_watchlist,
        'name': 'Julian Justin Orvino',
        'NPM': '2106720903',
        'msg_bonus': msg_bonus,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request,id):
    data = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

from django.shortcuts import render

from mywatchlist.models import myWatchListItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_watchlist = myWatchListItem.objects.all()
    berapa_kali = 0
    belum_nonton = 0
    for x in data_watchlist:
        if x.watched =="yes":
            berapa_kali += 1
            if x.watched == "no":
                belum_nonton+=1
    if(berapa_kali >= belum_nonton):
        msg_bonus = "Congratulations, you have watched movies a lot!"
    else:
        msg_bonus = "Woah, you have not much watched movies!"

    context = {
        'list_item': data_watchlist,
        'name': 'Julian Justin Orvino',
        'npm': '2106720903',
        'msg_bonus': msg_bonus,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = myWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = myWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = myWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request,id):
    data = myWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


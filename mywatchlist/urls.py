
from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import show_xml #customize to the name of the function created
from mywatchlist.views import show_json # adjust the name of the function created
from mywatchlist.views import show_json_by_id #customise the name of the function created
from mywatchlist.views import show_xml_by_id #customise the name of the function created


app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'), #customize the name of the function created
    path('json/', show_json, name='show_json'), #customise the name of the function created
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), #customise the name of the function created
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'), #customise the name of the function created
    path('html/', show_mywatchlist, name='show_mywatchlist'),
]

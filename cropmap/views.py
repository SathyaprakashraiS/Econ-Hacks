
from django.shortcuts import render

from .models import *

import folium


# Create your views here.

def map(request): 
    # name = geocoder.osm('Tamil Nadu')
    # print(name.lat)

    cp = Croplist.objects.all()

 
    cp_list = Croplist.objects.values_list('lat','log','state','crop','crop_img')
    # print(cp_list[0][0+1])
    new = list(cp_list)
    # print(new)
    
    # for cpl in cp_list:
    #     print(cpl["lat"])
    #     print(cpl['log'])


    map1 = folium.Map(location=[20, 78], zoom_start=5)
    for i in new:
        lat = i[0]
        log = i[1]
        state = i[2]
        crop = i[3]
        icon_url = i[4]
        icon = folium.features.CustomIcon(icon_url,icon_size=(40, 40))
        print(lat,log)
        folium.Marker([lat,log],popup=crop,tooltip=state,icon=icon).add_to(map1)
    
    map1 = map1._repr_html_()
    context={
        "map1":map1
    }
    return render(request, 'map.html',context)

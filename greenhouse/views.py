from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


def index(request):
    return render(request, 'greenhouse/gchart.html', {})


class JsonView(APIView):

    def get(self, request, v_id):
        tables = {
            'v0': AtmosphericPressure,
            'v1': Temperature,
            'v2': Humidity,
            'v3': SoilTemperature,
            'v4': SoilMoisture,
            'v5': Light,
            'v6': OutsideTemperature,
            'v7': HumidityOutside,
            'v8': ComfortIndicator,
        }
        # url = "http://194.126.183.219:8080/pvliXzHfH3f2a92cQ6ACtDgVw5-_r8tW/get/" + v_id
        # json = r.get(url).json()[0]
        # table = "greenhouse_" + tables[v_id]
        # V = tables[v_id].objects.all()
        # V.create(value_date=timezone.now(), value=json)

        if "start" in v_id:
            V_start = tables[v_id[:-5]].objects.order_by('-value_date')[:1000]
            date = []
            for V in V_start:
                d = V.value_date.strftime("%Y,%m,%d,%H,%M,%S").split(",")
                for i in range(len(d)):
                    d[i] = int(d[i])
                d.append(int(V.value))
                date.insert(0, d)
        else:
            V = tables[v_id].objects.latest('value_date')
            # js_date_list =V.value_date.replace("T", ",")[:V.find(".")].replace(":", ",")
            date = V.value_date.strftime("%Y,%m,%d,%H,%M,%S").split(",")
            for i in range(len(date)):
                date[i] = int(date[i])
            date.append(int(V.value))

        return Response(date)




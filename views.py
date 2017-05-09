from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@require_POST
@csrf_exempt
def check_goods(request):
    import requests
    data = request.POST
    dic = {}
    for key in data.keys():
        if 'ulmart' in data[key]:
            page = requests.get(data[key])
            if "'productAvailability': 'AVAILABLE'" in page.text:
                dic[key] = True
            else:
                dic[key] = False
        elif 'citilink' in data[key]:
            page = requests.get(data[key])
            if '"productAvailability":"available"' in page.text:
                dic[key] = True
            else:
                dic[key] = False
        elif 'wildberries' in data[key]:
            page = requests.get(data[key])
            if '"isSoldOut":false' in page.text:
                dic[key] = True
            else:
                dic[key] = False
        elif 'dns-shop' in data[key]:
            page = requests.get(data[key])
            if 'Нет в наличии' in page.text:
                dic[key] = False
            else:
                dic[key] = True
        elif 'holodilnik' in data[key]:
            page = requests.get(data[key])
            if 'Добавить в корзину' in page.text:
                dic[key] = True
            else:
                dic[key] = False
        elif 'corpcentre' in data[key]:
            page = requests.get(data[key])
            if 'Узнать о поступлении' in page.text:
                dic[key] = False
            else:
                dic[key] = True
    return JsonResponse(dic)

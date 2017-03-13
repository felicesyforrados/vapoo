from random import randrange

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from webpay.normal.api import WebpayNormalAPI


def carro(request):
    buyOrder = randrange(9999)
    sessionId = buyOrder
    webpay = WebpayNormalAPI().initTransaction(
        amount=15000,
        buyOrder=buyOrder,
        sessionId=sessionId,
        urlReturn='http://127.0.0.1:8000/webpay/compra/normal/verificacion/',
        urlFinal='http://127.0.0.1:8000/webpay/compra/normal/termina/')
    return render(
        request, 'carro.html',
        {'webpay_token': webpay.token, 'webpay_url': webpay.url, 'buyOrder': buyOrder}
    )


@csrf_exempt
def carro_final(request):
    return render(request, 'carro_final.html', {})

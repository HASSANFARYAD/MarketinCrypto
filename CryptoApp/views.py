from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    
    #For Price
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,LTC,BNB,USD,USDT,EOS,BSV,XMR,XLM,LEO,ADA,TRX,DASIH,LINK,XTZ,NEO,MIOTTA,ETC,ATOM,MKR,XEM,USDC,CRO,ONT,VSYS,ZEC,DOGR,DCR,VET&tsyms=USD&api_key=5a3a96b032734d6b107f5d5ffcce509f366bf4db220ebae2d344e05a8ce4ba3e")
    price = json.loads(price_request.content)
    api_key = 'https://dashboard.cryptoapis.io/account/api-key=sb557cd307ebba4045e770c311cdf073ee780c88f3c37837c19da97dd27efeced'
    return render(request, 'home.html', {'price': price, 'api_key': api_key})

def news(request):
    import requests
    import json
    #For News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key=5a3a96b032734d6b107f5d5ffcce509f366bf4db220ebae2d344e05a8ce4ba3e")
    api = json.loads(api_request.content)
    return render(request, 'news.html', {'api': api})


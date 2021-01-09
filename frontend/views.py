from django.shortcuts import render
from frontend.forms import ContactForm
import requests, json
def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        data=form.data
        url="http://127.0.0.1:8000/api/contact/"
        api=requests.post(url=url,data=data)
        try:
            resp=json.loads(api.text)

        except:
            resp=None
        print(resp)
    else:
        form=ContactForm()
    return render(request,'contact.html',{'form':form})



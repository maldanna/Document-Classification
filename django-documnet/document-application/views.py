from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
import pickle
import re


# Create your views here.
def home(request):
    return  render(request,'okcoolapp1/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'okcoolapp1/register.html', {'form': form,})

@login_required
def upload(request):
    return render(request, 'okcoolapp1/upload.html')
@login_required
def result(request):
    res=""
    if request.method == 'POST':
        content=request.POST.get('content_name')
        review = re.sub(r'\W', ' ', str(content))
        review = review.lower()
        review = re.sub(r'\s+[a-zA-Z]\s+', ' ', review)
        review = re.sub(r'^[a-zA-Z]\s+', ' ', review)
        review = re.sub(r'\s+', ' ', review)
        print(review)

        with open('/home/maldanna/Desktop/project/vectorizer_pickle', 'rb') as f:
            vet = pickle.load(f)

        with open('/home/maldanna/Desktop/project/model_pickle', 'rb') as k:
            clf = pickle.load(k)

        sample = []
        sample.append(review)
        sample1 = vet.transform(sample).toarray()

        res=clf.predict(sample1)
        number=res[0]
        if(number==0):
            res='cinema-news'
        elif(number==1):
            res='mobile-news'
        elif(number==2):
            res='sprots-news'
        return render(request, 'okcoolapp1/upload.html',{'rr':res})

    else:
        return render(request, 'okcoolapp1/upload.html',{{'rr':res}})




def about(request):
    
    return render(request, 'okcoolapp1/about.html')






from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def click_button(request):
    if 'messages' not in request.session:
        request.session['messages'] = []

    current_list = request.session['messages']
    if request.POST['button'] == 'button1':
        message = "<p class='blue'>First </p>"
    elif request.POST['button'] == 'button2':
        message = "<p class='red'>Second </p>"

    current_list.append(message)
    request.session['messages'] = current_list
    return redirect('/')
    # return render(request, 'show.html')

def reset(request):
    request.session.clear()
    return redirect('/')
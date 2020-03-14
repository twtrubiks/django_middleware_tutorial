from django.template.response import TemplateResponse
# Create your views here.

def index(request):
    # 3/0 # for test process_exception()
    context = {'data': "Hello, world. You're at the musics index."}
    return TemplateResponse(request,'musics/index.html', context)
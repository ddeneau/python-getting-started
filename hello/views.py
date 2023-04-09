from flask import jsonify

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return jsonify({'hello': 'world'})

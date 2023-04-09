from flask import jsonify

# Create your views here.
def index():
    # return HttpResponse('Hello from Python!')
    return jsonify({'hello': 'world'})

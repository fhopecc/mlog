def index(request, response):
    response.out.write('list users')

def show(id, request, response):
    return "list users %d" % id

def destroy(id):
    return "del test %d" % id

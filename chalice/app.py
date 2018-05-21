from chalice import Chalice, Response
from jinja2 import Environment, PackageLoader, select_autoescape

app = Chalice(app_name='syp_frontend')

env = Environment(
    loader=PackageLoader(__name__, 'chalicelib/templates'),
    autoescape=select_autoescape(['html', 'xml']))

def render_template(template_name, context, status_code=200, content_type='text/html', headers=None):
    template = env.get_template(template_name)
    body = template.render(**context)

    if headers is None:
        headers = {}

    headers.update({
        'Content-Type': content_type,
    })

    return Response(body=body, status_code=status_code, headers=headers)



@app.route('/')
def index():
    return render_template('index.html', {'name': 'home'})

@app.route('/personalize', cors=True)
def personalize():
    return render_template('index.html', {
        'name': 'personalize'
    })

@app.route('/personalize/result', cors=True)
def recommend():
    return render_template('result.html', {
        'name': 'result'
    })


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#

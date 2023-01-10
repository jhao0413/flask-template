from flask import Blueprint


hello = Blueprint(
    name="hello",
    import_name=__name__,
    url_prefix="/hello",
)


@hello.route("/", methods=["GET"])
def router_hello():
    """
    hello world
    """
    return 'Hello World!'

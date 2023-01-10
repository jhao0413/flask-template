from flask import Blueprint


word = Blueprint(
    name="word",
    import_name=__name__,
    url_prefix="/word",
)


@word.route("/", methods=["GET"])
def router_word():
    """
    hello world
    """
    return 'World!'

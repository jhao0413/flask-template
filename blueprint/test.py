from flask import Blueprint


test = Blueprint(
    name="test",
    import_name=__name__,
    url_prefix="/test",
)


@test.route("/", methods=["GET"])
def router_test():
    """
    hello world
    """
    return 'test!'

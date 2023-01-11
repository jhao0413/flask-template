import logging
import traceback
from flask import Blueprint, jsonify, request
from data.error import BusinessError
from data.message_carrier import MessageCarrier


test = Blueprint(
    name="test",
    import_name=__name__,
    url_prefix="/test",
)


@test.route("/<string:argument>", methods=["GET"])
def router_test_get(argument: str):
    """
    test
    """
    return jsonify(argument)


@test.route("/", methods=["POST"])
def router_test_post():
    """
    test Post
    """
    carrier = MessageCarrier()
    try:
        data = request.get_json(silent=True)
        carrier.push_succeed_data(data)
    except BusinessError as err:
        logging.error(str(err))
        traceback.print_exc()
        carrier.push_exception(err)
    return jsonify(carrier.dict())

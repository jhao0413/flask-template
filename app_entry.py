"""
flask app对象的入口
"""
import blueprint
from data.settings import FlaskSettings
from factories import create_flask_app, build_abs_path_by_file

flask_app = create_flask_app(
    settings=FlaskSettings(
        build_abs_path_by_file(__file__, "app.toml")
    ),
    blueprint_module=blueprint,
)

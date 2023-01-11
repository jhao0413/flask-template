from typing import Any

from flask import Blueprint, Flask
from data.settings import FlaskSettings
from util.server_helper import (
    scan_types_from_module,
)
from os.path import abspath, dirname, join


def build_abs_path_by_file(related_file, relative_file_path: str) -> str:
    """
    根据传入的文件及文件与其对应的相对路径来获得所在的绝对路径
    :param related_file: 传入文件
    :param relative_file_path: 与传入文件相对应的文件路径
    :return: 所在绝对路径
    """
    cur_path = dirname(abspath(related_file))
    return join(cur_path, relative_file_path)


def create_flask_app(
    settings: FlaskSettings,
    blueprint_module: Any = None,
) -> Flask:
    """
    创建 flask app 对象
    :param settings: 配置项
    :param blueprint_module: 蓝图模块
    :return: flask app对象
    """
    # 根据配置来设置app的静态目录和模板
    app = Flask(
        __name__,
        instance_relative_config=True,
    )

    # 加注蓝图
    if blueprint_module:
        blueprint_list = scan_types_from_module(
            scan_module=blueprint_module, scan_type=Blueprint
        )

        # 按注册顺序遍历所有蓝图。
        values = app.iter_blueprints()
        for blueprint_item in blueprint_list:
            if blueprint_item in values:
                continue
            app.register_blueprint(blueprint_item)

    return app

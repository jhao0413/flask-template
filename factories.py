from typing import Any, Callable

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
    error_handler_func: Callable = None,
    context_processors_func: Callable = None,
    process_before_request_func: Callable = None,
    init_app_func: Callable = None,
    babel_func: Callable = None,
) -> Flask:
    """
    创建 flask app 对象
    :param settings: 配置项
    :param blueprint_module: 蓝图模块
    :param error_handler_func: 错误处理函数，以Exception为参数传入
    :param context_processors_func: 上下文处理函数，不许有参数
    :param process_before_request_func: 请求前处理函数，不许有参数
    :param init_app_func: 初始化应用，以app对象为参数传入
    :param babel_func: 多国语言选择函数
    :param template_filters: 模板过滤器字典
    :param need_init_celery: 是否需要初始化celery
    :return: flask app对象
    """
    print(settings)
    # 根据配置来设置app的静态目录和模板
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder=settings.template_folder,
        static_folder=settings.static_folder,
        static_url_path="/static",
    )

    # 加注蓝图
    if blueprint_module:
        blueprint_list = scan_types_from_module(
            scan_module=blueprint_module, scan_type=Blueprint
        )
        values = app.iter_blueprints()
        for blueprint_item in blueprint_list:
            if blueprint_item in values:
                continue
            app.register_blueprint(blueprint_item)

    return app

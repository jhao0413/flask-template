from ast import List
import importlib
import pkgutil
from types import ModuleType
from typing import Generic, TypeVar


T = TypeVar(
    "T",
)


def scan_types_from_module(
    scan_module: ModuleType, scan_type: Generic[T], result_list: List = None
) -> List:
    """
    扫描模块
    """
    if result_list is None:
        result_list = []
    for _, model_name, is_pkg in pkgutil.iter_modules(
        scan_module.__path__, scan_module.__name__ + "."
    ):
        sub_model = importlib.import_module(model_name)
        if not is_pkg:
            for sub_item in dir(sub_model):
                sub_item = getattr(sub_model, sub_item)
                if isinstance(sub_item, scan_type):
                    result_list.append(sub_item)
        else:
            result_list += scan_types_from_module(
                sub_model, scan_type, result_list
            )
    return result_list

import importlib
import sys
from typing import Any, Dict

try:
    from .__version__ import __version__, __version_info__  # noqa
except Exception:  # pragma: no cover
    pass


__author__ = "Carl Oscar Aaro"  # noqa
__email__ = "hello@carloscar.com"  # noqa

__asahi_module = sys.modules["asahi"]
__available_defs: Dict[str, str] = {
    "extras": "asahi.extras",
}
__imported_modules: Dict[str, Any] = {"asahi": __asahi_module}
__cached_defs: Dict[str, Any] = {}


def __getattr__(name: str) -> Any:
    if name in __cached_defs:  # pragma: no cover
        return __cached_defs[name]

    if name in __available_defs:
        module_name = __available_defs[name]

        if not __imported_modules.get(module_name):
            try:
                __imported_modules[module_name] = importlib.import_module(module_name)
            except ModuleNotFoundError as e:  # pragma: no cover
                missing_module_name = str(getattr(e, "name", None) or "")
                if missing_module_name and missing_module_name == "asahi.extras":
                    raise ModuleNotFoundError("module 'asahi.extras' not found - install package 'asahi-extras' first")
                raise
            except Exception:  # pragma: no cover
                raise

        module = __imported_modules.get(module_name)
        __cached_defs[name] = module

        return __cached_defs[name]

    raise AttributeError("module 'asahi' has no attribute '{}'".format(name))


__all__ = [
    "__version__",
    "__version_info__",
    "__author__",
    "__email__",
    "extras",
]

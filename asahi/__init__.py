from __future__ import annotations

import importlib
from typing import Any, Dict, Tuple, Union
from pkgutil import extend_path
import sys

try:
    from .__version__ import __version__, __version_info__  # noqa
except Exception:
    pass


__author__ = "Carl Oscar Aaro"  # noqa
__email__ = "hello@carloscar.com"  # noqa

__asahi_module = sys.modules["asahi"]
__available_defs: Dict[str, Union[Tuple[str], Tuple[str, str]]] = {
    "extras": ("asahi.extras", None),
}
__imported_modules: Dict[str, Any] = {"asahi": __asahi_module}
__cached_defs: Dict[str, Any] = {}

print(sys.modules["asahi"])
def __getattr__(name: str) -> Any:
    if name in __cached_defs:
        return __cached_defs[name]

    if name in __available_defs:
        module_name = __available_defs[name][0]
        real_name = name if len(__available_defs[name]) < 2 else __available_defs[name][1]

        if not __imported_modules.get(module_name):
            try:
                __imported_modules[module_name] = importlib.import_module(module_name)
            except ModuleNotFoundError:  # pragma: no cover
                raise
            except Exception:  # pragma: no cover
                raise

        module = __imported_modules.get(module_name)

        if real_name is not None:
            __cached_defs[name] = getattr(module, real_name)
        else:
            __cached_defs[name] = module

        return __cached_defs[name]

    raise AttributeError("module 'asahi' has no attribute '{}'".format(name))


__path__ = extend_path(__path__, __name__)

__all__ = [
    "__version__",
    "__version_info__",
    "__author__",
    "__email__",
    "extras",
    "asahi",
]
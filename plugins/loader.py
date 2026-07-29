import importlib
import pkgutil

import plugins


class PluginLoader:

    def __init__(self):
        self.plugins = []

    def load(self, registry):

        package = plugins

        for _, module_name, _ in pkgutil.iter_modules(package.__path__):

            if module_name in ["loader", "base"]:
                continue

            module = importlib.import_module(
                f"plugins.{module_name}"
            )

            if hasattr(module, "plugin"):

                module.plugin.register(registry)

                self.plugins.append(module.plugin)

    def loaded(self):

        return self.plugins


loader = PluginLoader()
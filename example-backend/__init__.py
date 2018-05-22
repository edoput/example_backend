from netjsonconfig.backends.base.backend import BaseBackend
from netjsonconfig.backends.base.renderer import BaseRenderer
from netjsonconfig.backends.base.parser import BaseParser

from netjsonconfig.schema import schema as default_schema


class ExampleBackend(BaseBackend):
    schema = default_schema
    converter = []
    parser = BaseParser
    renderer = BaseRenderer

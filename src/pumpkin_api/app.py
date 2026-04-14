from . import WitWorldImpl, MetadataImpl
from .wit import wit_world

class WitWorld(WitWorldImpl, wit_world.WitWorld):
    pass

class Metadata(MetadataImpl, wit_world.exports.Metadata):
    pass

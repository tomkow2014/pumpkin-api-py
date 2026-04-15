# Pumpkin Plugin API for Python

This package provides everything needed to write a Pumpkin server plugin compiled to WebAssembly using Python.

## Quick start

1. Install `pumpkin-api-py`:

```bash
pip install pumpkin-api-py
```

2. Create your plugin (`main.py`):

```python
from pumpkin_api import (
    Plugin, PluginMetadata, register_plugin, 
    server, event, command, text, context
)

class MyPlugin(Plugin):
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="my-plugin",
            version="0.1.0",
            authors=["you"],
            description="An example plugin.",
            dependencies=[]
        )

    def on_load(self, ctx: context.Context) -> None:
        print("Python plugin loaded!")
        
        # Register an event handler
        self.register_event(ctx, event.EventType.PLAYER_JOIN_EVENT, self.on_player_join)

    def on_player_join(self, srv: server.Server, evt: event.PlayerJoinEventData) -> event.PlayerJoinEventData:
        print(f"Player {evt.player.get_name()} joined!")
        return evt

register_plugin(MyPlugin)
```

3. Build your plugin into a WebAssembly component:

```bash
pumpkin-api-build main -o my_plugin.wasm
```

from pumpkin_api import (
    Plugin, PluginMetadata, register_plugin, 
    server, event, command, text, context
)
from pumpkin_api.app import WitWorld, Metadata

class MyPlugin(Plugin):
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="my-plugin",
            version="0.1.0",
            authors=["you"],
            description="An example python plugin."
        )

    def on_load(self, ctx: context.Context) -> None:
        print("Python plugin loaded!")
        
        # Register an event handler
        self.register_event(ctx, event.EventType.PLAYER_JOIN_EVENT, self.on_player_join)
        
        # Register a command
        # cmd = command.Command(["hello"], "A simple hello command")
        # self.register_command(ctx, cmd, self.hello_command)

    def on_player_join(self, srv: server.Server, evt: event.PlayerJoinEventData) -> event.PlayerJoinEventData:
        print(f"Player {evt.player.get_name()} joined!")
        # We can modify the join message
        # evt.join_message = text.TextComponent_text("Welcome to the server!")
        return evt

    def hello_command(self, sender: command.CommandSender, srv: server.Server, args: command.ConsumedArgs) -> int:
        sender.send_message(text.TextComponent_text("Hello from Python!"))
        return 1

register_plugin(MyPlugin)

from textual.app import App, ComposeResult
from textual.widgets import Footer

from components.databases import Databases


class RedisTerminalViewer(App):
    """A Textual app to view Redis Database."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Footer()
        yield Databases()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = RedisTerminalViewer()
    app.run()
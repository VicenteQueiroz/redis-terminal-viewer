from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Footer, Header

from components.databases import Databases, AddDatabaseScreen

from textual.app import App, ComposeResult


class RedisTerminalViewer(App):
    """A Textual app to view Redis Database."""

    CSS_PATH = "styles.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    TITLE = "Redis Terminal Viewer"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Databases()
        yield Footer()
        # yield Button("+ Add Database", id="add_database")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        print("Add database!")
        self.push_screen(AddDatabaseScreen())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = RedisTerminalViewer()
    app.run()
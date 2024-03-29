from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Label, Input
from textual.screen import ModalScreen
from textual.containers import Grid
from textual.widget import Widget

class LabelledInput(Widget):
    DEFAULT_CSS = """
    LabelledInput {
        height: 4;
    }
    """

    def __init__(self, label):
        super().__init__()
        self.label = label

    def compose(self):
        yield Label(f"{self.label}:")
        yield Input(placeholder=self.label.lower())

class AddDatabaseScreen(ModalScreen):
    """Screen with a dialog to add a Redis Database."""

    def compose(self) -> ComposeResult:
        yield LabelledInput("Host")
        yield LabelledInput("Port")
        yield LabelledInput("Database Alias")
        yield LabelledInput("Username")
        yield LabelledInput("Password")
        # yield Button("Test Connection") // TODO
        yield Button("Cancel", variant="error", id="quit")
        yield Button("Apply Changes", variant="primary", id="cancel")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.app.exit()
        else:
            self.app.pop_screen()


class Databases(Static):
    """A Textual app to view Redis Database."""

    # def on_mount(self) -> None:
        # self.update(f"Hello, [b]World[/b]!")
    

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield Button("+ Add Database", id="add_database")
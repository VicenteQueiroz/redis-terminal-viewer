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

    def __init__(self, label: str, placeholder: str = ""):
        super().__init__()
        self.label = label
        self.placeholder = placeholder

    def compose(self):
        self.input = Input(placeholder=self.placeholder.lower())
        yield Label(f"{self.label}:")
        yield self.input

class AddDatabaseScreen(ModalScreen):
    """Screen with a dialog to add a Redis Database."""

    DEFAULT_CSS = """
    AddDatabaseScreen {
        align: center middle;
    }

    #modal {
        # grid-size: 3 2;
        # grid-gutter: 1 2;
        # grid-rows: 1fr 3;
        # padding: 0 1;
        width: 80;
        # height: 11;
        border: thick $background 80%;
        background: $surface;
    }
    """

    # CSS_PATH = "../styles.tcss"

    def compose(self) -> ComposeResult:
        self.host = LabelledInput("Host", "127.0.0.1")
        self.port = LabelledInput("Port", "6379")
        self.db_alias = LabelledInput("Database Alias")
        self.username = LabelledInput("Username")
        self.password = LabelledInput("Password")

        
        yield Grid(
            self.host,
            self.port,
            self.db_alias,
            self.username,
            self.password,
            # yield Button("Test Connection") // TODO
            Button("Cancel", variant="error", id="cancel"),
            Button("Apply Changes", variant="primary", id="apply_changes"),
            id="modal"
        )


    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cancel":
            self.app.pop_screen()
        elif event.button.id == "apply_changes":
            self.dismiss({"host": self.host.input.value, "port": self.port.input.value,
                          "db_alias": self.db_alias.input.value, "username": self.username.input.value, 
                          "password": self.password.input.value})
    

class Databases(Static):
    """A Textual app to view Redis Database."""

    # def on_mount(self) -> None:
        # self.update(f"Hello, [b]World[/b]!")
    

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield Button("+ Add Database", id="add_database")
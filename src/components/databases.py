from textual.app import ComposeResult
from textual.widgets import Static, Button


class Databases(Static):
    """A Textual app to view Redis Database."""

    # def on_mount(self) -> None:
        # self.update(f"Hello, [b]World[/b]!")

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield Button("Start", id="start", variant="success")
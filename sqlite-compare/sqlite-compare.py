import toga

from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class DatabaseComparatorApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name, size=(600, 200))

        self.db1_path = None
        self.db2_path = None

        self.db1_button = toga.Button("Select Database 1", style=Pack(padding=5))
        self.db1_label = toga.Label("", style=Pack(padding=5, flex=1))

        self.db2_button = toga.Button("Select Database 2", style=Pack(padding=5))
        self.db2_label = toga.Label("", style=Pack(padding=5, flex=1))

        self.compare_button = toga.Button("Compare", style=Pack(padding=5))

        self.progress_bar = toga.ProgressBar(style=Pack(padding=5))

        box = toga.Box(
            children=[
                toga.Box(children=[self.db1_button, self.db1_label], style=Pack(direction=ROW, padding=5)),
                toga.Box(children=[self.db2_button, self.db2_label], style=Pack(direction=ROW, padding=5)),
                self.compare_button,
                self.progress_bar
            ],
            style=Pack(direction=COLUMN, padding=10)
        )

        self.main_window.content = box
        self.main_window.show()


def main():
    return DatabaseComparatorApp(
        'SQLite Database Comparator',
        'net.kasueschke.sqlcompare',
        author='Leif Kasüschke',
        version='0.1',
        home_page='https://github.com/LeifKasueschke/sql-compare')


if __name__ == '__main__':
    main().main_loop()

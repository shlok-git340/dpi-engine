from rich.console import Console
from rich.table import Table


console = Console()


class Reporter:
    @staticmethod
    def print(metrics):
        table = Table(title="DPI ENGINE REPORT")

        table.add_column("Metric")
        table.add_column("Value")

        table.add_row("Total Packets", str(metrics.total_packets))
        table.add_row("Forwarded", str(metrics.forwarded))
        table.add_row("Dropped", str(metrics.dropped))

        console.print(table)
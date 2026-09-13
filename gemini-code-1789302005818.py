import sys
import psutil
from rich.console import Console
from rich.table import Table
import httpx

console = Console()

def get_public_ip():
    try:
        r = httpx.get("https://api.ipify.org?format=json", timeout=3.0)
        return r.json().get("ip", "Unavailable")
    except Exception:
        return "Offline"

def main():
    console.print("\n[bold cyan]System Status Monitor[/bold cyan]", justify="center")
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="dim", width=20)
    table.add_column("Value")

    # Metrics collection
    cpu_usage = f"{psutil.cpu_percent(interval=0.5)}%"
    ram_usage = f"{psutil.virtual_memory().percent}%"
    public_ip = get_public_ip()

    table.add_row("CPU Utilization", cpu_usage)
    table.add_row("Memory Utilization", ram_usage)
    table.add_row("External IP", public_ip)

    console.print(table)
    console.print("[bold green]✓ Diagnostic check completed successfully![/bold green]\n")

if __name__ == "__main__":
    main()
import typer
from scapy.all import sniff
from app.sources.pcap_source import PcapSource
# from app.sources.live_capture import LiveCaptureSource

from app.core.dpi_engine import DPIEngine
from app.core.packet_writer import PacketWriter

from app.stats.reporting import Reporter


app = typer.Typer()


@app.command()
def offline(
    input_pcap: str,
    output_pcap: str
):
    source = PcapSource(input_pcap)

    writer = PacketWriter(output_pcap)

    engine = DPIEngine(writer)

    for packet in source.packets():
        engine.process(packet)

    writer.save()

    Reporter.print(engine.metrics)


@app.command()
def live(interface: str):
    engine = DPIEngine()

    def process(packet):
        engine.process(packet)

    sniff(
        iface=interface,
        prn=process,
        store=False
    )


if __name__ == "__main__":
    app()
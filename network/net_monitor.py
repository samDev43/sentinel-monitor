



import socket
from event import SentinelEvent
from datetime import datetime 

def run_network_monitor():
    events = []

    host = "127.0.0.1"
    ports = range(20, 443)

    for each_port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)

            result = sock.connect_ex((host, each_port))

            if result == 0:
                if each_port == 22:
                    severity = "medium"
                elif each_port in (80, 443):
                    severity = "low"
                elif each_port == 21:
                    severity = "high"
                else:
                    severity = "high"

                event = SentinelEvent(
                    timestamp=datetime.utcnow().isoformat(),
                    event_type="network",
                    source=f"{host}:{each_port}",
                    severity=severity,
                    description=f"Open port detected: {each_port}"
                )

                events.append(event)

    return events
from datetime import datetime
from event import SentinelEvent


def detect_attacks(logs):
    events = []

    patterns = ["SELECT", "DROP", "<script>"]

    for log in logs:
        for pattern in patterns:
            if pattern.lower() in log.lower():
                event = SentinelEvent(
                    "appsec",
                    "attack_detected",
                    8,
                    f"Suspicious log found: {log}",
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
                events.append(event)

    return events
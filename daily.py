from datetime import datetime, timezone

now = datetime.now(timezone.utc)
print(f"Good morning! This script ran at {now:%Y-%m-%d %H:%M} UTC")
print("Reminder: commit your AI project before you let it change things.")

import uuid
from datetime import datetime, timezone

# Generate a UUID
request_id = str(uuid.uuid4())

# Get the current UTC time
utc_time = datetime.now(timezone.utc)

# Format the time as a string in the specified format
formatted_utc_time = utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")

# Print the request_id and the timestamp in the specified format
print(f"Request ID: {request_id}")
print(f"Timestamp (UTC): {formatted_utc_time}")

import uuid
import hmac
import hashlib
import base64

# Generate a unique request ID
unique_request_id = str(uuid.uuid4())

# Your secret key
secret_key = b'XSm+qnpEbIK8FAPQ+sOR+2tVBaJbYzlx4YKOhyK9aOUm0KXROz5ypgImw2g+C3wkVBlRthy3ZacbGW/ZjN6KRA=='

# Encode the unique request ID as bytes
message = unique_request_id.encode('utf-8')

# Generate the HMAC-SHA256 signature
signature = hmac.new(secret_key, message, hashlib.sha256).digest()

# Base64 encode the signature
signature_base64 = base64.b64encode(signature).decode('utf-8')

# Print
print(f"Unique Request ID: {unique_request_id}")
signed_unique_request_id = f"{unique_request_id}.{signature_base64}"
print(f"Signed Unique Request ID: {signed_unique_request_id}")

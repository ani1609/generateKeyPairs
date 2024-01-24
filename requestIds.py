from nacl import encoding, signing
import uuid
import base64

def sign_message(signing_string, private_key):
    # Decode the base64-encoded private key
    private_key_bytes = base64.b64decode(private_key)

    # Create a signing key from the private key
    signing_key = signing.SigningKey(private_key_bytes)

    # Sign the message
    signed_message = signing_key.sign(signing_string.encode())

    # Convert the signature to base64
    signature_base64 = base64.b64encode(signed_message.signature).decode()

    return signature_base64

# Example usage:
private_key_base64 = "pW64Crr8FuDkhY0qO5miDHC2XNXDgoYoFU2GG0T6r3k="
unique_request_id = str(uuid.uuid4())

signature = sign_message(unique_request_id, private_key_base64)
print("Unique Request ID:", unique_request_id)
print("Signed Unique Request ID:", signature)

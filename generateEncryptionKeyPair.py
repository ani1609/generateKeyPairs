from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import x25519
import base64

# Step 1: Random Key Pair Generation
private_key = x25519.X25519PrivateKey.generate()

# Step 2: Export Keys
public_key_bytes = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)
private_key_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PrivateFormat.Raw,
    encryption_algorithm=serialization.NoEncryption()
)

# Step 3: Encode Public Key (optional, if base64 encoding is needed)
public_key_base64 = base64.b64encode(public_key_bytes).decode('utf-8')
private_key_base64 = base64.b64encode(private_key_bytes).decode('utf-8')

# Display or use the keys as needed
print("Encryption Public Key:", public_key_base64)
print("Encryption Private Key:", private_key_base64)

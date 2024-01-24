from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import x25519

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

# Display or use the keys as needed
print("X25519 Public Key:", public_key_bytes.hex())
print("X25519 Private Key:", private_key_bytes.hex())

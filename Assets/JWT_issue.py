import jwt
import datetime
private_key = open("key.pem").read()  # Prefer using OCI Vault via SDK
token = jwt.encode(
    {
        "email": "user@external.org",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
        "aud": "provider2"
    },
    private_key,
    algorithm="RS256"
)

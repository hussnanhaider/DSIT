'''Use OCI KMS Sign API from Python or Go to create a detached JWT signature.'''
import oci
kms_client = oci.key_management.KmsCryptoClient(config)
request = oci.key_management.models.SignDataDetails(
    key_id = "<key-ocid>",
    message = base64.b64encode(message_bytes).decode("utf-8"),
    message_type = "RAW",
    signing_algorithm = "RSASSA_PKCS1_V1_5_SHA_256"
)
response = kms_client.sign_data(request)
signature = base64.b64decode(response.data.signature)

'''Then manually base64url encode and build JWT.'''
Option B - Load key from Vault Secret and sign using PyJWT:
import jwt
from base64 import b64decode
private_key = b64decode(secret_from_oci).decode()
token = jwt.encode(
    {"email": "user@dsit.gov.uk", "aud": "provider2"},
    private_key,
    algorithm="RS256"
)

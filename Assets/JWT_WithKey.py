import jwt
import requests
import oci
import base64
def handler(ctx, data: bytes = None):
    signer = oci.auth.signers.get_resource_principals_signer()
    secrets_client = oci.secrets.SecretsClient(config={}, signer=signer)
    secret_ocid = "ocid1.vaultsecret.oc1.uk-london-1.aaaaaaaaxyz"  # 🔐 Replace with your actual secret OCID
    try:
        secret_bundle = secrets_client.get_secret_bundle(secret_id=secret_ocid).data
        b64_secret_content = secret_bundle.secret_bundle_content.content
        private_key = base64.b64decode(b64_secret_content).decode("utf-8")
        payload = {
            "email": "dsit-user@cabinet.gov.uk",
            "aud": "provider2",
        }
        token = jwt.encode(payload, private_key, algorithm="RS256")
        headers = {
            "Authorization": f"Bearer {token}"
        }
        # 🔁 Call cross-cloud API
        response = requests.get("https://provider2.example.com/api/verify", headers=headers)
        if response.status_code == 200:
            return f"Remote says: {response.text}"
        else:
            return "unknown user"
    except Exception as e:
        return f"Error during signing or request: {str(e)}"

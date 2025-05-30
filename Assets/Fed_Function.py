import requests
# Your OIDC token from resource principal signer
token = "generated-ephemeral-token"
response = requests.post(
    "https://sts.amazonaws.com",  # or Azure federation endpoint
    headers={"Authorization": f"Bearer {token}"},
    data={
        "Action": "AssumeRoleWithWebIdentity",
        "RoleArn": "<aws_role_arn>",
        "RoleSessionName": "dsit-workload"
    }
)
if response.status_code == 200:
    creds = response.json()
else:
    print("unknown user")

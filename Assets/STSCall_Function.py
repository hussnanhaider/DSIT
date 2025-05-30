import requests
resp = requests.post(
    "https://sts.amazonaws.com",
    headers={"Authorization": f"Bearer {oci_ephemeral_token}"},
    data={
        "Action": "AssumeRoleWithWebIdentity",
        "Version": "2011-06-15",
        "RoleArn": "arn:aws:iam::<account-id>:role/<role-name>",
        "RoleSessionName": "dsit-session"
    }
)
creds = resp.text  # Parse and use temporary credentials

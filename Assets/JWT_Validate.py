decoded = jwt.decode(token, public_key, audience="provider2", algorithms=["RS256"])
if decoded["email"] not in allowlist:
    return "unknown user"

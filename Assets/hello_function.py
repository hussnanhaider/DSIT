def handler(ctx, data: bytes = None):
    headers = dict(ctx.Headers())
    user = headers.get("X-USER", "unknown user")
    return f"Hello, {user}"

'''Use the OCI Fn CLI to:
fn init --runtime python hello-fn
fn -v deploy --app dsit-app --create-app
IAM permissions from earlier dynamic groups will authorise function calls via resource principals.'''

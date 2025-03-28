from google_auth_oauthlib.flow import InstalledAppFlow

flow = InstalledAppFlow.from_client_secrets_file(
    'secret.json',
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)

creds = flow.run_local_server(port=8080)

print("\nACCESS TOKEN:")
print(creds.token)

print("\nREFRESH TOKEN (SAVE THIS!):")
print(creds.refresh_token)
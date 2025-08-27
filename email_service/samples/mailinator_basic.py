from email_service import MailinatorClient

client = MailinatorClient("test@mailinator.com")

account = client.create_account()
print(f"Account: {account}")

emails = client.get_emails()
print(f"Found {len(emails)} emails")

for email in emails:
    print(f"Subject: {email.get('subject')}")
    print(f"From: {email.get('from')}")
    
token = client.get_token()
print(f"Token: {token}")

request_id = client.get_request_id()
print(f"Request ID: {request_id}")

registration_details = client.get_registration_details()
print(f"Registration details: {registration_details}")

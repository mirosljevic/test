from email_service import MailHogClient, MailinatorClient, TempMailClient

def test_email_client(client, name):
    print(f"\n=== Testing {name} ===")
    
    account = client.create_account()
    print(f"Account creation: {account}")
    
    emails = client.get_emails()
    print(f"Emails found: {len(emails)}")
    
    if emails:
        first_email = emails[0]
        print(f"First email subject: {first_email.get('subject')}")
        
        message = client.get_message(first_email.get('message_id', ''))
        print(f"Message retrieved: {bool(message)}")
    
    token = client.get_token()
    print(f"Token found: {bool(token)}")
    
    request_id = client.get_request_id()
    print(f"Request ID found: {bool(request_id)}")
    
    registration_details = client.get_registration_details()
    print(f"Registration details: {registration_details}")

clients = [
    (MailHogClient("test@example.com"), "MailHog"),
    (MailinatorClient("test@mailinator.com"), "Mailinator"),
    (TempMailClient(), "TempMail")
]

for client, name in clients:
    test_email_client(client, name)

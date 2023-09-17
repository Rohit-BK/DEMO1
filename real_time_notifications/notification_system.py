import requests

def send_notification(message, recipients):
    for recipient in recipients:
        send_sms_notification(message, recipient)
        send_android_notification(message, recipient)
        # Add more notification methods here if needed

def send_sms_notification(message, recipient):
    # Code to send SMS notification
    pass

def send_android_notification(message, recipient):
    # Code to send Android notification
    pass

if __name__ == "__main__":
    negative_stories = [
        {
            'title': 'Example Negative Story 1',
            'content': 'This is an example negative story about the Government of India.',
            'website': 'https://example1.com'
        },
        {
            'title': 'उदाहरण नकारात्मक कहानी 2',
            'content': 'यह भारत सरकार के बारे में एक उदाहरण नकारात्मक कहानी है।',
            'website': 'https://example2.com'
        },
        # Add more negative stories here
    ]

    recipients = ['pib_officer1@example.com', 'pib_officer2@example.com']

    for story in negative_stories:
        title = story['title']
        content = story['content']
        send_notification(f"Negative story detected: {title}\n{content}", recipients)

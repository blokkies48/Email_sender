import smtplib
import ssl

class Message:
    """
    Message object to use in send_email
    """
    def __init__(self, *,subject='', body=''):
        """Creates message object with content

        Args:
            subject (str, optional): subject of email. Defaults to ''.
            body (str, optional): body of email. Defaults to ''.
        """
        self.subject = subject
        self.body = body

    def message_content(self) -> tuple[str,str]:
        """
        Returns:
            tuple[str,str]: return message tuple with relating content
        """
        return (self.subject, self.body)
        

def send_email(
        *,
        username:str,
        password:str,
        sender:str, 
        recipient:str, 
        message: Message, 
        smtp_server: str, 
        smtp_port: int
        ) -> str:
    """
    Takes in all keyword arguments that connects to a smtp -
    server and send said message to recipient. - 
    By using smtplib and ssl.

    Args:
        username (str): username used for login.
        password (str): password used for login.
        sender (str): email sending from
        recipient (str): email sending to
        message (Message): message as tuple of 2 objects (subject, body)
        smtp_server (str): smtp server
        smtp_port (int): smtp port


    Returns:
        str: success message
    """

    subject, body = message.message_content()
    sent_message = f"From: {sender}\nTo: {recipient}\nSubject: {subject}\n\n{body}"
    context = ssl.create_default_context()
    try:

        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            # Identify yourself to the SMTP server
            server.ehlo()
            # Authenticate with the SMTP server
            server.login(username, password)
            # Send the email
            server.sendmail(sender, recipient, sent_message)
            # Disconnect from the SMTP server
            server.quit()

        return (f'Email sent successfully to {recipient}!')
    except:
        return f"Email failed to send to {recipient}!"
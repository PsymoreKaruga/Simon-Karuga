# Create a file called backends.py in your project
import smtplib
import ssl
from django.core.mail.backends.smtp import EmailBackend

class CustomSSLEmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False
        try:
            context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
            context.minimum_version = ssl.TLSVersion.TLSv1_2

            self.connection = smtplib.SMTP(self.host, self.port, timeout=self.timeout)
            self.connection.ehlo()
            if self.use_tls:
                self.connection.starttls(context=context)
                self.connection.ehlo()
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except Exception as e:
            if self.fail_silently:
                return False
            raise
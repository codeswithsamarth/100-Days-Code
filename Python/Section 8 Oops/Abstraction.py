# The Abstraction is a process of hiding unnecessary data from user

class Email_Server:

    def __connection(self):
        print("Connecting To Server")

    def __authenticate(self):
        print("Authenticating..!")

    def send_email(self):
        self.__connection()
        self.__authenticate()
        print("Sending Email")

    def _disconnect(self):
        print("Disconnecting from email server")

email = Email_Server()
email.send_email()
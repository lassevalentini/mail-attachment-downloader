# -*- coding: utf-8 -*-

import threading
import time
from pprint import pprint


class Maildaemon(threading.Thread):
    def __init__(self, protocol, server, port, username, password):
        self.running = False
        self.protocol = server
        self.port = port
        self.username = username
        self.password = password

    def stop(self):
        self.running = False
        self.interrupt_main()

    def run(self):
        """
        Should not be run. Use start() to start the thread.
        """
        self.running = True
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.running = False


import poplib
import imaplib
import email
from email.header import decode_header


class MailFetcher(object):
    def __init__(self, protocol, server, port, username, password):
        protocol = protocol.lower()
        if "imap" in protocol:
            if "ssl" in protocol:
                self.connection = imaplib.IMAP4_SSL(server, port)
            else:
                self.connection = imaplib.IMAP4(server, port)
            self.connection.login(username, password)
            self.fetch = self.fetch_imap

        elif "pop3" in protocol:
            if "ssl" in protocol:
                self.connection = poplib.POP3_SSL(server, port)
            else:
                self.connection = poplib.POP3(server, port)
            self.connection.user(username)
            self.connection.pass_(password)
            self.fetch = self.fetch_pop

    def fetch(self):
        # Will be overwritten by one of the following two under construction
        pass

    def fetch_pop(self):
        mails = self.connection.list()
        pprint(mails)
        numMessages = len(mails[1])
        for i in range(numMessages):
            text = []
            l = 0
            for line in self.connection.retr(i+1)[1]:
                l+=1
                if l < 50:
                    print line
                text.append(line)

            msg = email.message_from_string("\n".join(text))
            del text

            for part in msg.walk():
                if "image" in part.get_content_type():
                    file_data = part.get_payload(decode=True)
                    if file_data:
                        filename = decode_header(part.get_filename())[0][0]
                        with open(filename, "wb") as f:
                            f.write(file_data)
                            del file_data
            # print "payload"
            # msg.get_payload(decode=True)

    def fetch_imap(self):
        pass


if __name__ == "__main__":
    import getpass
    print "Starting"
    test = MailFetcher("pop3 ssl", "pop.gmail.com", 995, raw_input("Username: "), getpass.getpass("Password: "))
    print "connected, fetching"
    test.fetch()

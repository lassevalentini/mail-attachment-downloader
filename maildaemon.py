# -*- coding: utf-8 -*-

import threading
import time
import os
from poplib import error_proto
from pprint import pprint


def removeNonAscii(s):
    return "".join(i for i in s if ord(i)<128)


class Maildaemon(threading.Thread):
    def __init__(self, protocol, server, port, username, password, destination, error_handler):
        super(Maildaemon, self).__init__()
        self.running = False
        self.fetcher = MailFetcher(protocol, server, port, username, password, destination)
        self.error_handler = error_handler
        # self.port = port
        # self.username = username
        # self.password = password

    def stop(self):
        self.running = False
        super(Maildaemon, self).interrupt_main()

    def run(self):
        """
        Should not be run. Use start() to start the thread.
        """

        self.running = True

        try:
            self.fetcher.connect()
        except error_proto, e:
            self.running = False
            if "-ERR [AUTH]" in e.message:
                self.error_handler("Error connecting to server - check username and password")
            else:
                print e.message
                self.error_handler("Error connecting to server - check server address and port")

        try:
            while self.running:
                self.fetcher.fetch()
                time.sleep(10)
        except KeyboardInterrupt:
            self.running = False


import poplib
import imaplib
import email
from email.header import decode_header


class MailFetcher(object):
    def __init__(self, protocol, server, port, username, password, destination):
        self.protocol = protocol.lower()
        self.server = server
        self.port = port
        self.username = username
        self.password = password
        self.destination = destination

        if "imap" in self.protocol:
            self.fetch = self.fetch_imap
        elif "pop3" in self.protocol:
            self.fetch = self.fetch_pop


    def connect(self):
        print "connecting"
        if "imap" in self.protocol:
            if "ssl" in self.protocol:
                self.connection = imaplib.IMAP4_SSL(self.server, self.port)
            else:
                self.connection = imaplib.IMAP4(self.server, self.port)
            # self.connection.set_debuglevel(10)
            self.connection.login(self.username, self.password)

        elif "pop3" in self.protocol:
            if "ssl" in self.protocol:
                self.connection = poplib.POP3_SSL(self.server, self.port)
            else:
                self.connection = poplib.POP3(self.server, self.port)
            # self.connection.set_debuglevel(10)
            print "logging in"
            self.connection.user(self.username)
            self.connection.pass_(self.password)


    def fetch(self):
        # Will be overwritten by one of the following two under construction
        pass

    def fetch_pop(self):
        print "listing"
        mails = self.connection.list()
        pprint(mails)
        numMessages = len(mails[1])
        print "new messages:",numMessages
        for i in range(numMessages):
            text = []
            # l = 0
            for line in self.connection.retr(i+1)[1]:
                # l+=1
                # if l < 50:
                #     print line
                text.append(line.decode("utf8"))

            msg = email.message_from_string("\n".join(text))
            del text

            from_ = msg.get_header("From")
            print from_
            from_ = u"Åge jensen".decode("utf-8")
            for part in msg.walk():
                if "image" in part.get_content_type():
                    file_data = part.get_payload(decode=True)
                    if file_data:
                        # filename = unicode(decode_header(part.get_filename())[0][0])
                        # print repr(filename)

                        try:
                            dest_file = os.path.join(self.destination,
                                                     u"{time} {filename}".format(time=time.strftime("%y-%m-%d %H:%M:%S"), filename=from_))
                        except:
                            dest_file = os.path.join(self.destination,
                                                     u"{time} {filename}".format(time=time.strftime("%y-%m-%d %H:%M:%S"), filename=removeNonAscii(from_)))


                        with open(dest_file, "wb") as f:
                            f.write(file_data)
                            del file_data
            # print "payload"
            # msg.get_payload(decode=True)

    def fetch_imap(self):
        self._connect()


if __name__ == "__main__":
    import getpass
    print "Starting"
    test = MailFetcher("pop3 ssl", "pop.gmail.com", 995, "fraekkert.mail.dump", getpass.getpass("Password: "), "")
    print "connected, fetching"
    test.fetch()

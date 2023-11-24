import imaplib
import email
import time
import re
import subprocess

# IMAP server connection details
imap_url = 'imapurl'
username = 'user'
password = 'password'
commands = "qm start 100 && qm start 108 && qm start 110"
commands2 = "qm shutdown 100 && shutdown 108 && qm shutdown 110"

try:
    # Establish a connection to the email server
    mail = imaplib.IMAP4_SSL(imap_url)
    mail.login(username, password)
    mail.select('INBOX', readonly=False)  # Set readonly to False to allow changes

    while True:
        try:
            # Search for unseen emails
            typ, uids = mail.search(None, 'UNSEEN')
            uids = uids[0].split()
            if not uids:
                print("No new emails found!")
                time.sleep(30)
                continue

            for uid in uids:
                # Fetch the email
                typ, msg_data = mail.fetch(uid, '(RFC822)')
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        subject = email.header.decode_header(msg['subject'])[0][0]
                        if isinstance(subject, bytes):
                            subject = subject.decode()

                        print(subject)

                        # Check if subject starts with "start"
                        if subject.startswith("start"):
                            try:
                                subprocess.run(commands, shell=True, check=True)
                                print("Commands executed successfully")
                            except subprocess.CalledProcessError as e:
                                print(f"Error running commands: {e}")
                            mail.store(uid, '+FLAGS', '\\Seen')
                        else:
                            print("nop")
                        if subject.startswith("stop"):
                            try:
                                subprocess.run(commands2, shell=True, check=True)
                                print("Commands executed successfully")
                            except subprocess.CalledProcessError as e:
                                print(f"Error running commands: {e}")
                            mail.store(uid, '+FLAGS', '\\Seen')
                          
        except imaplib.IMAP4.error as e:
            print(f"IMAP error occurred: {e}")
            break

        time.sleep(60)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    try:
        mail.close()
    except:
        pass
    try:
        mail.logout()
    except:
        pass

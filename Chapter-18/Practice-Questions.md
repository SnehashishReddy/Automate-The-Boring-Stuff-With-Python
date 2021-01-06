# Solutions for the Practice Questions in Chapter 18

## 1. What is the protocol for sending email? For checking and receiving email?
Simple Mail Transfer Protocol (SMTP) and Internet Message Access Protocol (IAMP) respectively.
## 2. What four smtplib functions/methods must you call to log in to an SMTP server?
1. smtplib.SMTP()
2. smtpObj.ehlo()
3. smtpObj.starttls()
4. smtpObj.login()
## 3. What two imapclient functions/methods must you call to log in to an IMAP server?
imapclient.IMAPClient() and imapObj.login()
## 4. What kind of argument do you pass to imapObj.search()?
A list of strings of IMAP keywords
## 5. What do you do if your code gets an error message that says got more than 10000 bytes?
We can assign imaplib._MAXLINE a bigint value
## 6. The imapclient module handles connecting to an IMAP server and finding emails. What is one module that handles reading the emails that imapclient collects?
The pyzmail module is responsible for reading the emails that imapclient collects
## 7. When using the Gmail API, what are the credentials.json and token.json files?
They're responsible for telling EZGmail what Gmail account is supposed to be used for sending mails
## 8. In the Gmail API, what’s the difference between “thread” and “message” objects?
A message represents a single email. A thread represents a chain of emails. Much like the daily status updates :grin:
## 9. Using ezgmail.search(), how can you find emails that have file attachments?
Pass has:attachment to search()
## 10. What three pieces of information do you need from Twilio before you can send text messages?
1. Twilio Account SID Number
2. The Authentication Token Number
3. Twilio Phone Number
def send_mail(name, fromaddr, msg):
    import smtplib
    import imghdr
    from email.message import EmailMessage
    from email.utils import formatdate

    # host_email_addr is the server that will send the email
    host_email_addr = 'robert@robertdrucker.com'
    password = 'G{IJmA,Ta%ZK' 

    # Create an email object
    email = EmailMessage()
    email['from'] = fromaddr  # email address of the person who submitted the contact form
    email['to'] = host_email_addr # to whom the email will be sent
    email['subject'] = 'Rob\'s Python Lab -- Feedback'
    email["Date"] = formatdate(localtime=True)

    message = 'Name:' + name + '\n' + 'Email: ' + fromaddr + '\n\n' + msg 

    # text, html, images, etc.
    email.set_content(message)

    # The SMTP HELO clause is the stage of the SMTP protocol where a SMTP server
    # introduce them selves to each other. The sending server will identify who
    #  it is and the receiving server will (as per RFC) accept any given name.
    # There is no requirement to give the correct information at this stage.
    with smtplib.SMTP(host='mail.robertdrucker.com', port=587) as smtp:
        smtp.ehlo()
        # tls is an encryption mechanism used for a secure connection to the server.
        smtp.starttls()
        smtp.login(host_email_addr, password)
        smtp.send_message(email)
        
        
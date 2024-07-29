import random
import smtplib


def otp_gen(email):
    otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ujjwalsabharwal75@gmail.com', 'lnzf svlh kmwu zccd')
    server.sendmail('ujjwalsabharwal75@gmail.com', email, otp)
    server.quit()
    return otp


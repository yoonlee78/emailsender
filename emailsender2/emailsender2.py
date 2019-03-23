# 같은 경로에 config.py를 만든다.
# config.py에는 아래 내용이 들어간다.
# EMAIL_ADDRESS = "my email address" <-본인의 이메일 주소
# PASSWORD = "my password" <-  비밀번호

import smtplib
import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = config.EMAIL_ADDRESS  # config.py의 EMAIL_ADDRESS에 할당된 본인의 이메일주소를 불러옴
password = config.PASSWORD  # config.py의 PASSWORD에 할당된 본인의 비밀번호를 불러옴
send_to_email = '수신인 이메일 주소'
subject = 'This is the Subject 1'  # 제목
message = 'This is my message 1'  # 내용

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login(email, password)
text = msg.as_string()
smtp.sendmail(email, send_to_email, text)
smtp.quit()

import smtplib
from email.message import EmailMessage

smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)

# 서버 연결 설정
smtp_gmail.ehlo()

# 서버 연결 암호화
smtp_gmail.starttls()

# 로그인
# AppPassword가 없다면 myaccount.google.com/apppassword로 가서 2-step 인증을 통해 부여받아야한다.
smtp_gmail.login('이메일@gmail.com', 'AppPassword')

msg = EmailMessage()

msg['Subject'] = "안녕"  # 제목 입력

msg.set_content("이거 파이썬으로 보낸거야 (smtplib)")  # 내용 입력

msg['From'] = '보내는이@gmail.com'  # 보내는 사람

msg['To'] = '받는이@gmail.com'  # 받는 사람

smtp_gmail.send_message(msg)

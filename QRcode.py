import qrcode

# QR코드에 저장할 URL
url = "https://www.ecount.com/kr/"

# QR코드 생성
qr = qrcode.QRCode(
    version=1,  # QR코드 크기 (1~40, 숫자가 클수록 더 많은 데이터 저장 가능)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 복원 수준
    box_size=10,  # QR코드 내 박스 크기
    border=4,  # QR코드 테두리 두께
)
qr.add_data(url)  # URL 데이터를 추가
qr.make(fit=True)  # QR코드 크기 조정

# QR코드 이미지 생성
img = qr.make_image(fill_color="black", back_color="white")

# 이미지 저장
img.save("ecount.com.png")
print("QR코드가 저장되었습니다.")
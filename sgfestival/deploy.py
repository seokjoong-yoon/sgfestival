import os
import subprocess

HOME_DIR = os.path.expanduser('~')
AWS_DIR = os.path.join(HOME_DIR, '.aws')
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

EB_EXTENSION_DIR = os.path.join(BASE_DIR, '.ebextensions')

PROJECT_NAME = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

print('--------------------')
print('홈 폴더 (사용자 폴더) :')
print(HOME_DIR)
print()
print('AWS Config 폴더 :')
print(AWS_DIR)
print()
print('기본 폴더 :')
print(BASE_DIR)
print()
print('.ebextension 폴더 생성 위치 :')
print(EB_EXTENSION_DIR)
print()
print('프로젝트명(폴더명으로 판단) :')
print(PROJECT_NAME)
print()

try:
    os.mkdir(EB_EXTENSION_DIR)
except FileExistsError as e:
    pass

try:
    os.mkdir(AWS_DIR)
except FileExistsError as e:
    pass

print("django.config 생성 및 작성 중...")
with open(os.path.join(EB_EXTENSION_DIR, 'django.config'), 'w') as fp:
    fp.write('option_settings:')
    fp.write('\n')
    fp.write('  aws:elasticbeanstalk:container:python:')
    fp.write('\n')
    fp.write('    WSGIPath: %s/wsgi.py' % PROJECT_NAME)

print("django.config 작성 완료")
print()

if not os.path.exists(os.path.join(AWS_DIR, 'config')):
    print("AWS 계정 설정 중...")
    aws_id = input('aws-access-id : ')
    aws_secret = input('aws-secret-key : ')

    with open(os.path.join(AWS_DIR, 'config'), 'w') as fp:
        fp.write("[profile eb-cli]")
        fp.write("\n")
        fp.write("aws_access_key_id = %s" % aws_id)
        fp.write("\n")
        fp.write("aws_secret_access_key = %s" % aws_secret)
        fp.write("\n")

    print("AWS 계정 설정 완료")
    print()

print("Elastic Beanstalk Application 설정 중...")
print("Elastic Beanstalk Application 설정 완료, 결과 값 : ")
result = subprocess.run(['eb', 'init', '-p', 'python-3.6', PROJECT_NAME], cwd=BASE_DIR)
print(result.returncode, end=', ')
if result.returncode == 0:
    print("Elastic Beanstalk Application이 성공적으로 생성됐습니다.")
else:
    print("Elastic Beanstalk Application을 생성하던 도중 에러가 발생했습니다.")
print()

print("Django Project를 배포 중입니다...")
result = subprocess.run(['eb', 'create', '%s-env' % PROJECT_NAME.lower()], cwd=PROJECT_DIR)
print(result.returncode, end=', ')
if result.returncode == 0:
    print("%s이(가) 성공적으로 배포되었습니다." % PROJECT_NAME)
else:
    print("배포 중에 에러가 발생했습니다.")
print()
result = subprocess.run(['eb', 'console'])
print("프로세스 종료.")
print('--------------------')

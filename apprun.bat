@REM �~�[�e�B���OID
set MEETINGID=1234567890
@REM �~�[�e�B���O�p�X���[�h
set PASSWD=password
@REM ���Ǝ��ԁi���j
set RECTIME=90
@REM �`���b�g���b�Z�[�W�i�o�Ȋm�F�p�j
set MSG=99999IH99A999�R�c���Y

start zoommtg:"//zoom.us/join?action=join&confno=%MEETINGID%
python ./app.py %PASSWD% %RECTIME% %MSG%
timeout /t 5
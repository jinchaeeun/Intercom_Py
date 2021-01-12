import speech_recognition as sr
import logging

logger = logging.Logger('catch_all')

#pip install pyaudio(에러 시: pip install pipwin, pipwin install pyauidio 차례로 실행)

def STT():
    r = sr.Recognizer()

    # print(sr.Microphone.list_microphone_names()) #마이크 목록

    #마이크 목록에서 기기 선택
    mic = sr.Microphone(device_index=1)

    #마이크로부터 녹음
    with mic as source:
        audio = r.listen(source)

    try:
        return r.recognize_google(audio, language='ko-KR')

    #마이크에 녹음되지 않았을 때
    except Exception as ex:
        logger.error(ex)
        return "ERROR"

print(STT())
import requests

with open("test.wav", "wb") as f:
    f.write(b'dummy_wav_data')

url = "http://localhost:8000/voicebot"
files = {'file': ('test.wav', open('test.wav', 'rb'), 'audio/wav')}
try:
    response = requests.post(url, files=files)
    print(response.status_code)
    print(response.text)
except Exception as e:
    print("Exception:")
    print(e)

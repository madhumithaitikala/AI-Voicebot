import traceback
from app.whisper_asr import WhisperASR
from app.intent_model import IntentClassifier
from app.response_generator import ResponseGenerator
from app.tts_engine import TTSEngine

with open("test.wav", "wb") as f:
    f.write(b'dummy_wav_data')

print("Loading...")
asr = WhisperASR(model_size="tiny")
intent_model = IntentClassifier()
response_gen = ResponseGenerator()
tts_engine = TTSEngine()

print("Testing ASR...")
try:
    text = asr.transcribe("test.wav")
    print("ASR success:", text)
except Exception as e:
    print("ASR FAILED")
    traceback.print_exc()

print("Testing Intent...")
try:
    prediction = intent_model.predict("Hello")
    print("Intent success:", prediction)
except Exception as e:
    print("Intent FAILED")
    traceback.print_exc()

print("Testing Gen...")
resp = response_gen.generate("greeting")
print("Gen:", resp)

print("Testing TTS...")
try:
    audio = tts_engine.synthesize(resp)
    print("TTS success", audio)
except Exception as e:
    print("TTS FAILED")
    traceback.print_exc()

import traceback
import sys
from app.whisper_asr import WhisperASR
from app.intent_model import IntentClassifier
from app.response_generator import ResponseGenerator
from app.tts_engine import TTSEngine

print("Loading Models...")
try:
    asr = WhisperASR()
    print("ASR Loaded.")
    intent = IntentClassifier()
    print("Intent Loaded.")
    gen = ResponseGenerator()
    print("Gen Loaded.")
    tts = TTSEngine()
    print("TTS Loaded.")
except Exception as e:
    print("FAILED TO LOAD:")
    traceback.print_exc()
    sys.exit(1)

print("ALL GOOD.")
sys.exit(0)

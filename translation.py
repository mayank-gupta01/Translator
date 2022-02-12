from googletrans import Translator

translator=Translator()
# translation
ans = translator.translate("आप क्या कर रहे हो",dest="en")
# detection
lang= translator.detect("आप क्या कर रहे हो")

print(ans.text)
print(lang)

'''OUTPUT'''
# What are you doing
# Detected(lang=hi, confidence=1)
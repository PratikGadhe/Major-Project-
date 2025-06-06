from gtts import gTTS

# Text messages
welcome_text = "Welcome to Incentivised Plastic or Metallic Can Recycling Machine. Let's start recycling."
input_text = "Please enter how many number of plastic bottles or metal cans you want to recycle."

# Convert to speech
welcome_audio = gTTS(text=welcome_text, lang='en')
input_audio = gTTS(text=input_text, lang='en')

# Save as MP3
welcome_audio.save("static/audio/welcome_message.mp3")
input_audio.save("static/audio/input_prompt.mp3")

print("Audio files generated successfully!")

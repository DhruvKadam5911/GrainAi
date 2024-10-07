import pyttsx3

# Define the speak function
def speak(text, rate=150, volume=1.0, voice_index=1):
    """
    Convert the given text to speech.
    
    Parameters:
    - text (str): The text to be spoken.
    - rate (int): The speed of speech (default is 150 words per minute).
    - volume (float): The volume level (default is 1.0, range is 0.0 to 1.0).
    - voice_index (int): The index of the voice (default is 0 for male, 1 for female).
    """
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set the speech rate and volume
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    # Get the available voices
    voices = engine.getProperty('voices')

    # Set the voice by index (0 = male, 1 = female, depending on the system voices)
    engine.setProperty('voice', voices[voice_index].id)

    # Convert the text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()
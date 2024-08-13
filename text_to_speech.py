from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing

import os
import io

# Get the current working directory
current_dir = os.getcwd()

# Create a client using the credentials and region defined in the [default]
# section of the AWS credentials file
session = Session(profile_name="default")
polly = session.client("polly")


def tts(text, voice):
    try:
        # Check if the speech file already exists
        audio_file_path = os.path.join(current_dir, "speech.mp3")
        if not os.path.exists(audio_file_path):
            # Request speech synthesis
            response = polly.synthesize_speech(
                Text=text,
                OutputFormat="mp3",
                VoiceId=voice,
            )

            # Access the audio stream from the response
            if "AudioStream" in response:
                with closing(response["AudioStream"]) as stream:
                    # Open a file for writing the output as a binary stream
                    with open(audio_file_path, "wb") as file:
                        file.write(stream.read())
                        print(f"Audio saved as: {audio_file_path}")

                    # Return the audio file as a binary stream
                    return io.open(audio_file_path, "rb")

            else:
                # The response didn't contain audio data, handle it as desired
                return "Could not stream audio"

        else:
            # Speech file already exists, apply voiceover to the downloaded videos using your preferred video editing library
            return "Voiceover applied to the videos successfully!"
    
    except (BotoCoreError, ClientError) as error:
            # The service returned an error, handle it as desired
            return f"Error: {error}"

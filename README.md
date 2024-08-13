# Script2Screen

## Description:

Script2Screen is an innovative AI-powered platform designed to automate the video creation process. It transforms text scripts into fully edited videos by integrating various AI technologies, significantly reducing the time and effort required for manual video production. This platform is particularly useful for content creators, marketers, and educators who need to quickly generate high-quality videos from written content.

## How It Works:

1. Script Input: The user starts by inputting a text script into the Script2Screen platform. This script serves as the foundation for the video.

2. Text-to-Speech (TTS) Conversion: Using Amazon Polly AI, the platform converts the text script into natural-sounding speech. This voiceover serves as the narration for the video.

3. Keyword Extraction: The script is analyzed by the OpenAI API to extract key concepts and keywords. These keywords are essential for finding relevant visuals that align with the script’s content.

4. Visual Content Generation: Script2Screen utilizes the Pexels API to search for and retrieve video clips that match the extracted keywords. These clips are then assembled to form the visual content of the video.

5. Video Editing and Compilation: The platform leverages the MoviePy Python library to edit and compile the video. This includes trimming and combining clips, syncing the voiceover with the visuals, and adding subtitles to enhance accessibility.

6. Final Output: The result is a polished, fully edited video that aligns with the original script. The entire process, from script to screen, is streamlined to save time and increase content production efficiency.

## Technologies Used:

1. Amazon Polly AI: For converting text to speech.
2. OpenAI API: For extracting keywords from the script.
3. Pexels API: For sourcing video clips based on keywords.
4. MoviePy Python Library: For editing and compiling the final video.
5. Python Flask: Backend framework to manage the application's logic.
6. HTML5 and CSS3: For the user interface design.

## Benefits:

1. Efficiency: Reduces video creation time by 60% compared to manual processes.
2. Scalability: Allows for rapid content production, making it ideal for users who need to generate multiple videos quickly.
3. Customization: Users can easily adjust the generated content to fit their specific needs, offering flexibility in the final output.
4. Script2Screen is a powerful tool for anyone looking to streamline video production, making high-quality content creation accessible and efficient.

## Demo:
Check out the demo of Script2Screen in action here: [Script2Screen Demo](https://drive.google.com/file/d/1TYSljAlBn-T1Wnve0ENMv7zSo_YReRAQ/view?usp=sharing)

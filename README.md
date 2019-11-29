pdf to speech inspired from: https://github.com/Maegner/pdf-to-speech
Improvements:

- Can easily change language
- Gather all error messages at the same place
- Uses `pyttsx3` instead of `gTTS`, so works offline too

Speech recognition: https://pypi.org/project/SpeechRecognition/

Custom way to use the product:

- User switches on the Raspberry, which will start the program
- A vocal assistant notices when everything is ready with a welcome message
- Assistant gives the different possibilities (resume previous read, start new)
- If previous read, assistant says where the reader is (current chapter, current page) => user can change chapter or page before starting again
- If start new, can choose either with categories, title, author or random
- After having selected a book, can have info (author, summary, user review, ...)

To process books, do the following

- Get info about the source: pdf or ebook?
- If ebook, convert to pdf
- Then, parse the text to have indications: where are the chapters, the parts, ...
- Run process to improve the text: are there problems? If yes, can we solve them?
- Then, save this text as a mp3 => try to find the best reading voice possible
- If fast enough, compute on the run. If not, save a mp3 file
- Continue reading, until person says trigger word or switches off the device (save checkpoints, like every chapter)

To use espeak

- Remove bluealsa package
  `sudo apt-get remove --auto-remove bluealsa`
- Replace pcm.xxx.yyy by pcm.xxx.default whenever there is a mistake in the config file (`nano /usr/share/alsa/alsa.conf`)
- Install pulseaudio (`sudo apt-get install pulseaudio`)

Products to buy:

- Speakers: https://www.amazon.com/HONKYOB-Speaker-Computer-Multimedia-Notebook/dp/B075M7FHM1/ref=sr_1_2_sspa?crid=H45RHDYG2GZA&keywords=speaker+for+raspberry+pi&qid=1568586306&sprefix=speaker+for+rasp%2Caps%2C249&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE4M09FTUw3VllNTFgmZW5jcnlwdGVkSWQ9QTA4NTc5OTUxRVRBWFpCNzFHR1NYJmVuY3J5cHRlZEFkSWQ9QTAwODA1MDMzQVZTVVZGUTc2V0dHJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==
- Microphone: https://www.amazon.com/KISEER-Microphone-Desktop-Recording-YouTube/dp/B071WH7FC6/ref=sr_1_5?keywords=microphone+for+raspberry+pi&qid=1568586446&sr=8-5

## How to proceed:

- Use Python to read audio files
- Manage an ebook library: write the functions to do so
- Build a CLI command to interact with the library
- Build an ebook reader class, to deal with the reading
- Have a fully functional ebook library
- Add a vocal command to control the program, instead of the CLI (https://realpython.com/python-speech-recognition/)
- Add a voice to interact with the user
- Add a program to convert PDF files to ebooks
- Extend this program to other formats
- Add recommendation system

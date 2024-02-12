# YTS_Specific_Movies_Notifier

Sents a discord alert when a matching movie title in `movies_titles.txt` found in YTS.

1. Install Dependencies
```sh
$ pip install -r requirements.txt
```

2. Add your discord webhook URL to `webhook_url` variable.

3. Run Script
```sh
$ python YTS_Specific_Movies_Notifier.py
```

Discord Alert Structure
```
@everyone
 Latest movie: The Beekeeper
 Date: 02-02-2024
 URL: https://yts.mx/https://yts.mx/movies/the-beekeeper-2024
```

# YTS_Specific_Movies_Notifier

Sents a discord alert when a matching movie title in `movies_titles.txt` found in YTS.

1. Clone Repository

```sh
$ git clone https://github.com/nabzter/YTS_Specific_Movies_Notifier.git
```

2. Move into the directory

```sh
$ cd YTS_Specific_Movies_Notifier
```

3. Install Dependencies
```sh
$ pip install -r requirements.txt
```

4. Add your discord webhook URL to `webhook_url` variable.

5. Run Script
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

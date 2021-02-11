# Dodiom

Code for the Telegram bot [Dodiom](https://t.me/mwetest_bot).

## Setup

Create a new bot using [BotFather](https://t.me/botfather), get it's token and put it in `docker/docker-compose.yml` and then run

````shell script
docker-compose up -d
````

You can see the Database in [http://localhost:8080](http://localhost:8080) and logs in [http://localhost:5341](http://localhost:5341) after starting the bot.

## Publications

If you use Dodiom in a scientific publication, please kindly cite [Gamified Crowdsourcing for Idiom Corpora Construction](https://arxiv.org/abs/2102.00881) paper.

```bib
@misc{eryigit2021gamified,
      title={Gamified Crowdsourcing for Idiom Corpora Construction}, 
      author={Gülşen Eryiğit and Ali Şentaş and Johanna Monti},
      year={2021},
      eprint={2102.00881},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```


License
=======

GNU General Public License v3.0 or later

See `COPYING` to see the full text.

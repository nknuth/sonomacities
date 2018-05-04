import logging
import json
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")


logging.getLogger("flask_ask").setLevel(logging.INFO)
logger = logging.getLogger("flask_ask")


def random_choice(word_list):
    index = randint(0, len(word_list) - 1)
    return word_list[index]


@ask.launch
def new_game():
    citiesDictionary = {
        'Cloverdale': False,
        'Cotati': False,
        'Healdsburg': False,
        'Petaluma': False,
        'RohnertPark': False,
        'SantaRosa': False,
        'Sebastopol': False,
        'Sonoma': False,
        'Windsor': False
    }
    welcome_msg = render_template('welcome')

    people = json.load(open('people.json'))
    session.attributes['people'] = people
    session.attributes['cities'] = citiesDictionary

    return question(welcome_msg)


@ask.intent("YesIntent")
def next_round():
    msg = render_template('round')
    return question(msg)


@ask.intent("NoIntent")
def goodbye():
    firstname = session.attributes['firstname']
    msg = render_template('bye', firstname=firstname)
    return statement(msg)


@ask.intent("AMAZON.FallBackIntent")
def FallBackIntnet():
    msg = render_template('fallback')
    return statement(msg)


@ask.intent("NameIntent", convert={'firstname': str})
def name_answer(firstname):
    logger.info("NameIntent: firstname {}".format(firstname))

    session.attributes['firstname'] = firstname

    msg = render_template('name', firstname=firstname)

    return question(msg)


@ask.intent("StatusIntent")
def StatusIntent():
    logger.info("StatusIntent:")

    citiesDictionary = session.attributes['cities']

    numberFound = sum(citiesDictionary.values())

    msg = render_template('status', number=numberFound)
    return question(msg)


@ask.intent("CloverdaleIntent")
def CloverdaleIntent():
    logger.info("CloverdaleIntent:")

    session.attributes['cities']['Cloverdale'] = True

    good_words = session.attributes['people']['good_words']
    adjectives = session.attributes['people']['positive_people_adjectives']

    msg = render_template('city', city='Cloverdale',
                          good=random_choice(good_words),
                          adjective=random_choice(adjectives))

    return question(msg)


@ask.intent("CotatiIntent")
def CotatiIntent():
    logger.info("CotatiIntent:")

    session.attributes['cities']['Cotati'] = True

    good_words = session.attributes['people']['good_words']
    adjectives = session.attributes['people']['positive_people_adjectives']

    msg = render_template('city', city='Cotati',
                          good=random_choice(good_words),
                          adjective=random_choice(adjectives))
    return question(msg)


@ask.intent("HealdsburgIntent")
def HealdsburgIntent():
    logger.info("HealdsburgIntent:")

    session.attributes['cities']['Healdsburg'] = True

    good_words = session.attributes['people']['good_words']
    adjectives = session.attributes['people']['positive_people_adjectives']

    msg = render_template('city', city='Healdsburg',
                          good=random_choice(good_words),
                          adjective=random_choice(adjectives))
    return question(msg)


@ask.intent("PetalumaIntent")
def PetalumaIntent():
    logger.info("PetalumaIntent:")

    session.attributes['cities']['Petaluma'] = True

    good_words = session.attributes['people']['good_words']
    adjectives = session.attributes['people']['positive_people_adjectives']

    msg = render_template('city', city='Petaluma',
                          good=random_choice(good_words),
                          adjective=random_choice(adjectives))
    return question(msg)


@ask.intent("RohnertParkIntent")
def RohnertParkIntent():
    logger.info("RohnertParkIntent:")

    session.attributes['cities']['RohnertPark'] = True

    good_words = session.attributes['people']['good_words']
    adjectives = session.attributes['people']['positive_people_adjectives']

    msg = render_template('city', city='RohnertPark',
                          good=random_choice(good_words),
                          adjective=random_choice(adjectives))
    return question(msg)


@ask.intent("SantaRosaIntent")
def SantaRosaIntent():
    logger.info("SantaRosaIntent:")

    session.attributes['cities']['SantaRosa'] = True

    good_words = session.attributes['people']['good_words']
    adjectives = session.attributes['people']['positive_people_adjectives']

    msg = render_template('city', city='SantaRosa',
                          good=random_choice(good_words),
                          adjective=random_choice(adjectives))
    return question(msg)


@ask.intent("SebastopolIntent")
def SebastopolIntent():
    logger.info("SebastopolIntent:")

    session.attributes['cities']['Sebastopol'] = True

    good_words = session.attributes['people']['good_words']
    adjectives = session.attributes['people']['positive_people_adjectives']

    msg = render_template('city', city='Sebastopol',
                          good=random_choice(good_words),
                          adjective=random_choice(adjectives))
    return question(msg)


@ask.intent("SonomaIntent")
def SonomaIntent():
    logger.info("SonomaIntent:")

    session.attributes['cities']['Sonoma'] = True

    good_words = session.attributes['people']['good_words']
    adjectives = session.attributes['people']['positive_people_adjectives']

    msg = render_template('city', city='Sonoma',
                          good=random_choice(good_words),
                          adjective=random_choice(adjectives))
    return question(msg)


@ask.intent("WindsorIntent")
def WindsorIntent():
    logger.info("WindsorIntent:")

    session.attributes['cities']['Windsor'] = True

    good_words = session.attributes['people']['good_words']
    adjectives = session.attributes['people']['positive_people_adjectives']

    msg = render_template('city', city='Windsor',
                          good=random_choice(good_words),
                          adjective=random_choice(adjectives))
    return question(msg)


if __name__ == '__main__':
    app.run(debug=True)

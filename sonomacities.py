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


def city_message(city):
    citiesDictionary = session.attributes['cities']
    good_words = session.attributes['people']['good_words']
    adjectives = session.attributes['people']['positive_people_adjectives']

    if citiesDictionary[city] is True:
        msg1 = render_template('redo', city=city,
                               good=random_choice(good_words))
    else:
        msg1 = render_template('city', city=city,
                               good=random_choice(good_words),
                               adjective=random_choice(adjectives))
        citiesDictionary[city] = True

    found = sum(citiesDictionary.values())

    if found == 9:
        msg2 = render_template('finished',
                               good=random_choice(good_words))
        response = statement(msg1 + ' ' + msg2)
    else:
        msg2 = render_template('keepgoing')
        response = question(msg1 + ' ' + msg2)

    return response


def status_update():
    # report on the number found...
    citiesDictionary = session.attributes['cities']
    found = sum(citiesDictionary.values())

    if found == 0:
        msg = render_template('noneFound')
    else:
        ucities = [k for k, v in citiesDictionary.items() if v is True]
        if found > 1:
            ucities.insert(-1, 'and')
        cities = ', '.join([u.encode('utf-8') for u in ucities])
        msg = render_template('status', number=found, cities=cities)

    return msg


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


@ask.intent("AMAZON.FallbackIntent")
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
    msg = status_update()
    return question(msg)


@ask.intent("CloverdaleIntent")
def CloverdaleIntent():
    logger.info("CloverdaleIntent:")
    response = city_message('Cloverdale')
    return response


@ask.intent("CotatiIntent")
def CotatiIntent():
    logger.info("CotatiIntent:")
    response = city_message('Cotati')
    return response


@ask.intent("HealdsburgIntent")
def HealdsburgIntent():
    logger.info("HealdsburgIntent:")
    response = city_message('Healdsburg')
    return response


@ask.intent("PetalumaIntent")
def PetalumaIntent():
    logger.info("PetalumaIntent:")
    response = city_message('Petaluma')
    return response


@ask.intent("RohnertParkIntent")
def RohnertParkIntent():
    logger.info("RohnertParkIntent:")
    response = city_message('RohnertPark')
    return response


@ask.intent("SantaRosaIntent")
def SantaRosaIntent():
    logger.info("SantaRosaIntent:")
    response = city_message('SantaRosa')
    return response


@ask.intent("SebastopolIntent")
def SebastopolIntent():
    logger.info("SebastopolIntent:")
    response = city_message('Sebastopol')
    return response


@ask.intent("SonomaIntent")
def SonomaIntent():
    logger.info("SonomaIntent:")
    response = city_message('Sonoma')
    return response


@ask.intent("WindsorIntent")
def WindsorIntent():
    logger.info("WindsorIntent:")
    response = city_message('Windsor')
    return response


if __name__ == '__main__':
    app.run(debug=True)

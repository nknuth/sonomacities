import logging
import json
#from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")


logging.getLogger("flask_ask").setLevel(logging.INFO)
logger = logging.getLogger("flask_ask")


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
    logger.info("In name_answer: firstname {}"
                .format(firstname))
    session.attributes['firstname'] = firstname
    msg = render_template('name',
                          firstname=firstname)
    return question(msg)


@ask.intent("StatusIntent")
def StatusIntent():
    citiesDictionary = session.attributes['cities']
    logger.info("StatusIntent:")
    numberFound = sum(citiesDictionary.values())
    msg = render_template('status', number=numberFound)
    return question(msg)


@ask.intent("CloverdaleIntent")
def CloverdaleIntent():
    logger.info("CloverdaleIntent:")

    session.attributes['cities']['Cloverdale'] = True

    msg = render_template('city', city='Cloverdale')
    return question(msg)


@ask.intent("CotatiIntent")
def CotatiIntent():
    logger.info("CotatiIntent:")

    session.attributes['cities']['Cotati'] = True

    msg = render_template('city', city='Cotati')
    return question(msg)


@ask.intent("HealdsburgIntent")
def HealdsburgIntent():
    logger.info("HealdsburgIntent:")

    session.attributes['cities']['Healdsburg'] = True

    msg = render_template('city', city='Healdsburg')
    return question(msg)


@ask.intent("PetalumaIntent")
def PetalumaIntent():
    logger.info("PetalumaIntent:")

    session.attributes['cities']['Petaluma'] = True

    msg = render_template('city', city='Petaluma')
    return question(msg)


@ask.intent("RohnertParkIntent")
def RohnertParkIntent():
    logger.info("RohnertParkIntent:")

    session.attributes['cities']['RohnertPark'] = True

    msg = render_template('city', city='RohnertPark')
    return question(msg)


@ask.intent("SantaRosaIntent")
def SantaRosaIntent():
    logger.info("SantaRosaIntent:")

    session.attributes['cities']['SantaRosa'] = True

    msg = render_template('city', city='SantaRosa')
    return question(msg)


@ask.intent("SebastopolIntent")
def SebastopolIntent():
    logger.info("SebastopolIntent:")

    session.attributes['cities']['Sebastopol'] = True

    msg = render_template('city', city='Sebastopol')
    return question(msg)


@ask.intent("SonomaIntent")
def SonomaIntent():
    logger.info("SonomaIntent:")

    session.attributes['cities']['Sonoma'] = True

    msg = render_template('city', city='Sonoma')
    return question(msg)


@ask.intent("WindsorIntent")
def WindsorIntent():
    logger.info("WindsorIntent:")

    session.attributes['cities']['Windsor'] = True

    msg = render_template('city', city='Windsor')
    return question(msg)


if __name__ == '__main__':
    app.run(debug=True)

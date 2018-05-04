import logging
import json
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")


logging.getLogger("flask_ask").setLevel(logging.DEBUG)
logger = logging.getLogger("flask_ask")


globalFirstName = None
globalLastName = None
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


@ask.launch
def new_game():
    welcome_msg = render_template('welcome')
    people = json.load(open('people.json'))
    session.attributes['people'] = people
    return question(welcome_msg)


@ask.intent("YesIntent")
def next_round():
    numbers = [randint(0, 9) for _ in range(3)]
    round_msg = render_template('round', numbers=numbers)
    session.attributes['numbers'] = numbers[::-1]  # reverse
    return question(round_msg)


@ask.intent("NoIntent")
def goodbye():
    msg = render_template('bye', firstname=globalFirstName)
    return statement(msg)


@ask.intent("AMAZON.FallBackIntent")
def goodbye():
    msg = render_template('fallback')
    return statement(msg)


@ask.intent("AnswerIntent",
            convert={'first': int, 'second': int, 'third': int})
def answer(first, second, third):
    winning_numbers = session.attributes['numbers']
    if [first, second, third] == winning_numbers:
        msg = render_template('win')
    else:
        msg = render_template('lose')
    return statement(msg)


@ask.intent("NameIntent", convert={'firstname': str})
def name_answer(firstname):
    logger.info("In name_answer: firstname {}"
                .format(firstname))
    msg = render_template('name',
                          firstname=firstname)
    return question(msg)


@ask.intent("StatusIntent")
def StatusIntent():
    global citiesDictionary
    logger.info("StatusIntent:")
    numberFound = sum(citiesDictionary.values())
    msg = render_template('status', number=numberFound)
    return question(msg)


@ask.intent("CloverdaleIntent")
def CloverdaleIntent():
    global citiesDictionary
    logger.info("CloverdaleIntent:")
    citiesDictionary['Cloverdale'] = True

    msg = render_template('city', city='Cloverdale')
    return question(msg)


@ask.intent("CotatiIntent")
def CotatiIntent():
    global citiesDictionary
    logger.info("CotatiIntent:")
    citiesDictionary['Cotati'] = True

    msg = render_template('city', city='Cotati')
    return question(msg)


@ask.intent("HealdsburgIntent")
def HealdsburgIntent():
    global citiesDictionary
    logger.info("HealdsburgIntent:")
    citiesDictionary['Healdsburg'] = True

    msg = render_template('city', city='Healdsburg')
    return question(msg)


@ask.intent("PetalumaIntent")
def PetalumaIntent():
    global citiesDictionary
    logger.info("PetalumaIntent:")
    citiesDictionary['Petaluma'] = True

    msg = render_template('city', city='Petaluma')
    return question(msg)


@ask.intent("RohnertParkIntent")
def RohnertParkIntent():
    global citiesDictionary
    logger.info("RohnertParkIntent:")
    citiesDictionary['RohnertPark'] = True

    msg = render_template('city', city='RohnertPark')
    return question(msg)


@ask.intent("SantaRosaIntent")
def SantaRosaIntent():
    global citiesDictionary
    logger.info("SantaRosaIntent:")
    citiesDictionary['SantaRosa'] = True

    msg = render_template('city', city='SantaRosa')
    return question(msg)


@ask.intent("SebastopolIntent")
def SebastopolIntent():
    global citiesDictionary
    logger.info("SebastopolIntent:")
    citiesDictionary['Sebastopol'] = True

    msg = render_template('city', city='Sebastopol')
    return question(msg)


@ask.intent("SonomaIntent")
def SonomaIntent():
    global citiesDictionary
    logger.info("SonomaIntent:")
    citiesDictionary['Sonoma'] = True

    msg = render_template('city', city='Sonoma')
    return question(msg)


@ask.intent("WindsorIntent")
def WindsorIntent():
    global citiesDictionary
    logger.info("WindsorIntent:")
    citiesDictionary['Windsor'] = True

    msg = render_template('city', city='Windsor')
    return question(msg)


if __name__ == '__main__':
    globalFirstName = None
    globalLastName = None

    app.run(debug=True)

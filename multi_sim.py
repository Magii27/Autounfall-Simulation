import random
import math
from multiprocessing import Pool
import json


class settings():
    def const(self):
        ws_unfall = 0.0057 / 100
        durchschn_weglaenge = 16
        ws_anderes_getoetet = 0.0683 / 100
        ws_auto_gestorben = 0.0433 / 100
        ws_leicht_verletzt = 11.5942 / 100
        ws_schwer_verletzt = 2.3837 / 100

    start_alter = 21
    wege = 15 / 7
    weglaenge = 10

    end_alter = 90

    durchgaenge = 5000


def simulation(durchgang):
    global statistik
    alter = settings.const.start_alter
    tot = False

    temp_statistik = {"alter":setup.start_alter, "unfälle":0, "anderes_getötet":0, "auto_gestorben":0, "leicht_verletzt":0, "schwer_verletzt":0, "sachschaden":0}

    for day_sim in range((setup.end_alter - setup.start_alter)*365 + 1):
        if day_sim % 365 == 0:
            alter += 1

        schleife = int(math.ceil(setup.wege))
        temp_wege = setup.wege / round(setup.wege)

        for i_wege in range(schleife):
            if ws(temp_wege):
                if ws(setup.ws_unfall * (setup.weglaenge / setup.durchschn_weglaenge)):
                    temp_statistik["unfälle"] += 1
                    if ws(setup.ws_anderes_getoetet):
                        temp_statistik["anderes_getötet"] += 1

                    if ws(setup.ws_auto_gestorben):
                        temp_statistik["auto_gestorben"] += 1
                        tot = True
                    elif ws(setup.ws_leicht_verletzt):
                        temp_statistik["leicht_verletzt"] += 1
                    elif ws(setup.ws_schwer_verletzt):
                        temp_statistik["schwer_verletzt"] += 1
                    else:
                        temp_statistik["sachschaden"] += 1
                else:
                    pass

        if tot:
            break

    temp_statistik["alter"] = alter

    fin_temp_statistik = {}
    fin_temp_statistik["durchgang_" + str(durchgang)] = temp_statistik
    return fin_temp_statistik


def ws(prob):
    return random.random() < prob


if __name__ == '__main__':
    setup()

    statistik = {}

    with Pool(6) as p:
        temp_statistik = p.map(simulation, [x for x in range (0, setup.durchgaenge)])

    for i in range(len(temp_statistik)):
        statistik[list(temp_statistik[i].keys())[0]] = temp_statistik[i]["durchgang_" + str(i)]

    with open("stats.json", "w") as f:
        json.dump(statistik, f)
        f.close()
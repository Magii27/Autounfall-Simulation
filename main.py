import random
import math

ws_unfall = 0.0057 / 100
durchschn_weglänge = 16
ws_anderes_getötet = 0.0683 / 100
ws_auto_gestorben = 0.0433 / 100
ws_leicht_verletzt = 11.5942 / 100
ws_schwer_verletzt = 2.3837 / 100

start_alter = 22
wege = 18 / 7
weglänge = 70

end_alter = 90

alter = start_alter
tot = False

statistik = {"unfälle":0, "anderes_getötet":0, "auto_gestorben":0, "leicht_verletzt":0, "schwer_verletzt":0, "sachschaden":0}


def ws(prob):
    return random.random() < prob


for day_sim in range((end_alter - start_alter)*365 + 1):
    if day_sim % 365 == 0:
        alter += 1

    print(f"-- Jahr {day_sim // 365} Tag {day_sim % 365}" + " " * (4 - len(str(day_sim % 365))) + "-" * (
                20 - len(str(day_sim // 365)) + len(str(day_sim % 365)) + (4 - len(str(day_sim % 365)))))

    schleife = int(math.ceil(wege))
    temp_wege = wege / int(math.ceil(wege))

    for i_wege in range(schleife):
        if ws(temp_wege):
            #print("Fahrt")
            #print(ws_unfall * (weglänge / durchschn_weglänge))
            if ws(ws_unfall * (weglänge / durchschn_weglänge)):
                statistik["unfälle"] += 1
                if ws(ws_anderes_getötet):
                    statistik["anderes_getötet"] += 1

                if ws(ws_auto_gestorben):
                    statistik["auto_gestorben"] += 1
                    tot = True
                elif ws(ws_leicht_verletzt):
                    statistik["leicht_verletzt"] += 1
                elif ws(ws_schwer_verletzt):
                    statistik["schwer_verletzt"] += 1
                else:
                    statistik["sachschaden"] += 1
                print(" !> Unfall")
            else:
                #print("kein Unfall")
                pass

    print("Unfälle: {}, anderes getötet: {}, auto gestorben: {}".format(statistik["unfälle"], statistik["anderes_getötet"], statistik["auto_gestorben"]))
    print("leicht verletzt: {}, schwer verletzt: {}, nur sachschaden: {}".format(statistik["leicht_verletzt"], statistik["schwer_verletzt"], statistik["sachschaden"]))
    print("")

    if tot:
        print("Alter: ", alter)
        break





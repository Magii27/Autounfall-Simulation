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

print(settings.const(1))



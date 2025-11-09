# Otázka 1:
*Volba šířky okna klouzavého průměru*
- Jak volit šířku okna? Proč?
V naší řadě jsme ozkoušeli pro šířku klouzavého okna hodnoty 7, 14 a 30. Šířka sedm vyhlazuje data za týden, což by mělo eliminovat sezónnost v rámci týdne (více lidí chodí o víkendu), nicméně nevyhlatuzuje dostatečně a neukazuje správně trend. Šířka třicet vyhlazuje data za měsíc, nicméně toto opět má své chyby, specificky velké díry kvůli chybějícím hodnotám. Čtrnáct dní (dva týdny) se jeví jako ideální kompromis. Pěkně reprezentuje trend, a přitom nepřehlazuje.

- Doporučení jak šířku volit
Větší okno se používá pro vyhlazení pro zdůraznění dlouhodobého trendu a eliminace fluktuace. Taky se používá pro data braná v delším intervalu (víc jednotivých kusů dat).
Okno pro neperiodické řady by mělo být většinou liché, aby se nemuselo centrovat (hups).
Okno se také dá zvolit takové, aby vyhladilo sezónní složku.

# Otázka 2:
- Jak obecně vypadají grafy polynomiálních funkcí?
Něco s Taylorovým rozvojem?

- Nehodilo by se něco lepšího?
Potenciálním kandidátem by mohl být polynom stupně 6, poněvadž u polynomu stupně 5 hodnota za hranicemi grafu je rostoucí, což není sedí k vývoji křivky. Nicméně, poněvadž tento model je už tak komplikovaný, a v budoucnu by asi nesledoval vývoj řady, pravděpodobně lepší nebude. 
Dále bychom měli asi zvážit jako model součet sinusoidy a lineární funkce. Řada vzdáleně připomíná sínovou křivku, a jeví se jako cyklická, tudíž by se sínus mohl jevit jako potenciální volba.

# Otázka 3:
- Proč lineární trend vypadá lépe než kvadratický nebo kubický?
Dle kritéria BIC je nejlepší polynom stupně 5, a dle kritéria r^2 je kvintérní model je také nejlepší. Spletl jsem si to s RMSE, a čím blíže je skóre hodnotě 1, tím lepší. My bad.

# Otázka 4:
SARIMA pomocí rovnice

# Otázka 5:
Popsat ozkoušené dynamické modely

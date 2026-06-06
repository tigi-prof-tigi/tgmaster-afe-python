"""Signal momentum anti look-ahead (fiche section 7.4)."""
import pandas as pd


def signal_momentum(prix, fenetre=63, n_titres=2):
    perf = prix.pct_change(fenetre)
    rang = perf.rank(axis=1, ascending=False)
    poids = (rang <= n_titres).astype(float)
    poids = poids.div(poids.sum(axis=1), axis=0)
    poids = poids.shift(1).fillna(0.0)
    return poids

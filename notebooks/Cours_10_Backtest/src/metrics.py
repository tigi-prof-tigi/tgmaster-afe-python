"""Metriques de performance : Sharpe et max drawdown (fiche section 7.6)."""
import numpy as np


def sharpe_annualise(rendements, taux_sans_risque=0.035, periodes=252):
    rf = taux_sans_risque / periodes
    exces = rendements - rf
    if exces.std() == 0:
        return 0.0
    return np.sqrt(periodes) * exces.mean() / exces.std()


def max_drawdown(equity):
    sommet = equity.cummax()
    return (equity / sommet - 1.0).min()

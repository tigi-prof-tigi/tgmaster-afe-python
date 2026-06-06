"""Moteur de backtest avec frais de rotation (fiche section 7.5)."""
import pandas as pd


def backtester(prix, poids, frais=0.005):
    rend = prix.pct_change().fillna(0.0)
    rend_strat = (poids * rend).sum(axis=1)
    rotation = poids.diff().abs().sum(axis=1).fillna(0.0)
    rend_strat = rend_strat - rotation * frais
    equity_strat = (1 + rend_strat).cumprod()
    equity_bh = (1 + rend.mean(axis=1)).cumprod()
    return pd.DataFrame({'Strategie': equity_strat, 'BuyAndHold': equity_bh}), rend_strat

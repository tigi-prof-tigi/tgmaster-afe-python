"""Chargement et nettoyage des cours BRVM (fiche section 7.3)."""
import pandas as pd
import numpy as np


def charger_cours_brvm(chemin_csv):
    df = pd.read_csv(chemin_csv)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
    df = df.dropna(subset=['Date'])
    prix = df.pivot_table(index='Date', columns='Ticker', values='Cloture')
    return prix.sort_index().ffill().dropna(how='all')


def rendements_quotidiens(prix):
    return prix.pct_change().dropna(how='all')

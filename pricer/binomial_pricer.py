import numpy as np
import math

# Modèle Binomial
# Utilisé pour évaluer les options en construisant un arbre binomial où le prix du sous-jacent évolue de manière discrète.
# Particulièrement utile pour les options américaines ou européennes, car il permet de modéliser l'exercice anticipé (pour les options américaines).
# La précision augmente avec le nombre d'étapes dans l'arbre.

class BinomialPricer:
    def __init__(self, S, K, T, r, sigma, N):
        self.S = S           # Prix de l'actif sous-jacent
        self.K = K           # Prix d'exercice
        self.T = T           # Maturité
        self.r = r           # Taux sans risque
        self.sigma = sigma   # Volatilité
        self.N = N   # Nombre d'étapes dans l'arbre binomial
        self._dt = T / N  # Taille d'un intervalle de temps
        self._u = np.exp(sigma * np.sqrt(self._dt))  # Facteur de hausse
        self._d = 1 / self._u  # Facteur de baisse
        self._q = (np.exp(r * self._dt) - self._d) / self._u - self._d


    def get_european_option(self):
        option_prices = {
            'call': np.array(
                        math.comb(self.N, i) * (self._q ** i) * ((1 - self._q) ** (self.N - i))
                        * np.max(self.S * self._u ** i * self._d ** (self.N - i) - self.K, 0)
                    for i in range(self.N + 1)
            ),
            'put': np.array(
                       math.comb(self.N, i) * (self._q ** i) * ((1 - self._q) ** (self.N - i))
                       * np.max(self.K - self.S * self._u ** i * self._d ** (self.N - i),0)
                       for i in range(self.N + 1)
            )
        }
        call_price = np.sum(option_prices['call'] * np.exp(-self.r * self._dt))
        put_price = np.sum(option_prices['put'] * np.exp(-self.r * self._dt))
        return call_price, put_price


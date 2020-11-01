def f (x,mu,sig) :
    return np.exp(-(x-mu)**2/(2*sig**2)) / np.sqrt(2*np.pi) / sig
# Next up, the derivative with respect to μ.
# If you wish, you may want to express this as f(x, mu, sig) multiplied by chain rule terms.
# === COMPLETE THIS FUNCTION ===
def dfdmu (x,mu,sig) :
    return f(x, mu, sig) * (-x + mu)/(sig**2)*(-1)

# Finally in this cell, the derivative with respect to σ.
# === COMPLETE THIS FUNCTION ===
def dfdsig (x,mu,sig) :
    return (-1/np.sqrt(2*np.pi) / sig**2) 
    * np.exp(-(x-mu)**2/(2*sig**2)) 
    + (1/ np.sqrt(2*np.pi) 
    / sig)*((x-mu)**2 * sig**(-3) 
    *np.exp(-(x-mu)**2/(2*sig**2)))

def steepest_step (x, y, mu, sig, aggression) :
    J = np.array([
        -2*(y - f(x,mu,sig)) @ dfdmu(x,mu,sig),
        -2*(y - f(x,mu,sig)) @ dfdsig(x,mu,sig)
    ])
    step = -J * aggression
    return step
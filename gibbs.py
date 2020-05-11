from pprint import pprint
import tqdm
import numpy as np

def energy_of_state(G,H,state):
    return state.T @ G @ state + state.T @ H

def make_prob(energy,beta):
    return np.exp(energy*beta)

def sample_state(G,H,betas,num_iter):
    number_of_states = G.shape[0]

    states = np.random.binomial(1,0.5,size=(G.shape[0],betas.shape[0]))

    for i in range(num_iter):

        sampling_point = num_iter % number_of_states
        pos,neg = state.copy(),state.copy()

        pos[sampling_point] = 1
        neg[sampling_point] = -1

        pos_energy = energy_of_state(G,H,pos).flatten()
        neg_energy = energy_of_state(G,H,neg).flatten()

        pos_prob = make_prob(pos_energy,beta)
        neg_prob = make_prob(neg_energy,beta)

        normalizer = pos_prob + neg_prob
        pos_prob = pos_prob/normalizer
        neg_prob = neg_prob/normalizer

        selection = np.random.uniform()

        state = pos.copy() if selection < pos_energy else neg.copy()

    return state

def energy_estimation(G,H,beta,num_iter,sample_size=100):
    states = [ sample_state(G,H ,beta, num_iter) for i in range(sample_size)]
    energies = [ energy_of_state(G,H,state).flatten() for state in states]
    return sum(energies)/len(energies)




G = [[0,1,1,0],[0,0,0,0],[0,0,0,0],[0,1,1,0]]
G = np.array(G)
H = np.zeros((4,))


betas = np.linspace(0.5,10,num=20)
energies = []
for beta in tqdm.tqdm(betas):
    energies.append(energy_estimation(G,H,beta,1000).flatten())

print(energies)

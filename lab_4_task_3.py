g = 10
def energy(m, h, v):
  energy_pot = m * g * h
  energy_kin = (m * v**2)/2
  meh_energy = energy_pot + energy_kin
  return meh_energy
print(energy(10, 100, 60))
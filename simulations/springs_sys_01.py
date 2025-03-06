import numpy as np
import pdb
import matplotlib.pyplot as plt

node_qty = 15
area = 100
k = 2.0
min_distance = 3
num_iteraciones = 100

positions = np.random.uniform(0, np.sqrt(area), (node_qty, 2))
#positions = np.array([[3., 3.], [3., 7.], [7., 3.], [7., 7.], [7, 5]])
offsets = np.zeros_like(positions)
interactions = np.zeros((node_qty, 2))

# force_magnitude computes a scalar value based on the given distance.
# If the distance is less than or equal to min_distance, the result will be
# negative. If the distance is greater than min_distance, the result will be
# positive.
def force_magnitude (distance, min_distance):
  #k = 2
  return k * (min_distance - distance) if distance <= min_distance else -k * (distance - min_distance)

# force_B_on_A computes a vector representing the force exerted by object B on object A.
# The force is calculated based on the distance between A and B and is directed
# along the vector B - A.
def force_B_on_A(a, b):
  distance_a_b = np.linalg.norm(a - b)
  direction_a_b = np.divide(a - b, distance_a_b, where=(distance_a_b != 0))
  force_module = force_magnitude(distance_a_b, min_distance)
  f = force_module * direction_a_b

  return f

# resultant_force takes an array of force vectors and returns a single vector representing
# the combined effect of all the forces in the array.
def resultant_force(forces):
  return np.sum(forces, axis=0)

def compute_interactions(positions):
  interactions = np.zeros((node_qty, 2))

  for i in range(node_qty):
    aux_forces = np.zeros((node_qty - 1, 2))
    aux_forces_index = 0
    for j in range(node_qty):
      if i != j:
        aux_forces[aux_forces_index] = force_B_on_A(positions[i], positions[j])
        aux_forces_index += 1
    interactions[i] = resultant_force(aux_forces)
  return interactions

# compute_offsets takes an array of vectors representing the initial positions of nodes
# and calculates their positional offsets based on an array of interaction
# forces.
def compute_offsets(positions, interactions, step_size):
  offsets = np.zeros_like(positions)
  for i in range(node_qty):
    #print("compute_offsets i: ", i)
    offsets[i] = positions[i] + interactions[i] * step_size
    #print("i: ", i, " positions[i]: ", positions[i], " offsets[i]: ", offsets[i])
  return offsets

plt.figure(figsize=(8, 8))
plt.scatter(positions[:, 0], positions[:, 1], color="blue", s=200, zorder=2)

for i in range(num_iteraciones-1):
  #print("positions: ", positions)
  offsets = compute_offsets(positions, compute_interactions(positions), 0.05)
  positions = offsets
  plt.scatter(positions[:, 0], positions[:, 1], color="skyblue", s=200, zorder=2)

offsets = compute_offsets(positions, compute_interactions(positions), 0.05)
positions = offsets
plt.scatter(positions[:, 0], positions[:, 1], color="red", s=200, zorder=2)

plt.xlim(0, np.sqrt(area))
plt.ylim(0, np.sqrt(area))
plt.gca().set_aspect("equal", adjustable="box")
plt.title("Simulación de sistema masas unidas por resortes")
plt.show()

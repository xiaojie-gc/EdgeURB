import numpy as np

# Interval = 6s , segment length = 12,  640 * 640

info= {'static': {'time': [4.308279037475586, 4.4063496589660645, 4.373910903930664, 4.420788049697876, 4.319616794586182, 4.332087516784668, 4.485997438430786, 4.222504615783691, 4.309391260147095, 4.243631839752197, 4.155680894851685, 4.117675065994263, 4.207131385803223, 4.263052701950073, 4.244883298873901, 4.044734001159668, 4.10221529006958, 4.032358646392822, 4.180273056030273, 4.249496698379517, 4.20308256149292, 4.308971881866455], 'energy': [6.41, 6.15, 5.9, 5.69, 5.4, 5.58, 5.67, 5.26, 5.48, 5.34, 4.88, 4.65, 4.67, 4.86, 4.18, 4.46, 4.61, 5.06, 4.63, 4.77, 4.73, 4.79]}, 'network': {'time': [0.491, 0.514, 0.48, 0.479, 0.516, 0.544, 0.461, 0.569, 0.602, 0.632, 0.567, 0.665, 0.545, 0.601, 0.644, 0.668, 0.762, 0.638, 0.599, 0.596, 0.536, 0.519], 'energy': [1.23, 1.12, 1.08, 1.01, 1.07, 1.25, 0.96, 1.19, 1.26, 1.31, 1.21, 1.28, 1.06, 1.14, 1.1, 1.28, 1.45, 1.25, 1.16, 1.13, 1.04, 1.01]}, 'encoding': {'time': [1.254, 1.11, 1.08, 1.136, 1.101, 1.159, 1.085, 1.135, 1.124, 1.161, 1.209, 1.254, 1.183, 1.168, 1.141, 1.216, 1.174, 1.257, 1.248, 1.193, 1.19, 1.207], 'energy': [2.75, 2.16, 2.11, 2.1, 1.97, 2.02, 1.96, 2.02, 2.0, 2.06, 2.1, 1.97, 1.91, 1.86, 1.68, 1.85, 1.94, 2.44, 1.93, 1.93, 1.99, 1.97]}}

print("###############################################")
x = np.array([np.average(info["static"]["energy"]), np.average(info["encoding"]["energy"]), np.average(info["network"]["energy"])])
x = np.round(x, 4)
print("e=", list(x))
t = np.array([np.average(info["static"]["time"]), np.average(info["encoding"]["time"]), np.average(info["network"]["time"])])
t = np.round(t, 4)
print("t=", list(t))

info= {'static': {'time': [4.290174961090088, 4.228397607803345, 4.408887624740601, 4.16761326789856, 4.186583042144775, 4.021570444107056, 4.441059350967407, 4.246670961380005, 4.268811225891113, 4.219405651092529, 4.211141109466553, 4.38088583946228, 4.183485269546509, 4.130857229232788, 4.159926414489746, 4.121172189712524, 4.507521390914917, 4.247762680053711, 4.134053945541382, 4.25612211227417, 4.351793050765991, 4.405084133148193], 'energy': [6.64, 6.3, 6.36, 6.07, 6.01, 5.73, 6.34, 5.97, 6.04, 6.09, 6.06, 6.23, 6.11, 5.89, 5.92, 5.87, 6.47, 6.07, 5.83, 6.04, 6.21, 6.18]}, 'network': {'time': [0.52, 0.56, 0.485, 0.654, 0.57, 0.648, 0.492, 0.642, 0.533, 0.634, 0.592, 0.511, 0.636, 0.651, 0.727, 0.605, 0.457, 0.567, 0.657, 0.556, 0.552, 0.515], 'energy': [1.35, 1.3, 1.13, 1.45, 1.27, 1.46, 1.15, 1.44, 1.21, 1.43, 1.37, 1.18, 1.46, 1.49, 1.64, 1.41, 1.01, 1.3, 1.51, 1.3, 1.22, 1.15]}, 'encoding': {'time': [1.324, 1.112, 1.142, 1.105, 1.276, 1.26, 1.1, 1.139, 1.13, 1.177, 1.16, 1.11, 1.21, 1.152, 1.144, 1.212, 1.064, 1.215, 1.142, 1.137, 1.115, 1.111], 'energy': [2.89, 2.26, 2.33, 2.21, 2.41, 2.33, 2.19, 2.27, 2.22, 2.3, 2.3, 2.26, 2.36, 2.27, 2.3, 2.39, 2.16, 2.37, 2.28, 2.31, 2.2, 2.2]}}

print("###############################################")
x = np.array([np.average(info["static"]["energy"]), np.average(info["encoding"]["energy"]), np.average(info["network"]["energy"])])
x = np.round(x, 4)
print("e=", list(x))
t = np.array([np.average(info["static"]["time"]), np.average(info["encoding"]["time"]), np.average(info["network"]["time"])])
t = np.round(t, 4)
print("t=", list(t))

### 9fd3b96565dbebe8####################
e = [6.1105, 2.3095, 1.3286]
t = [4.2531, 1.1608, 0.5802]

### 204dfa87f106ca64####################
e = [5.1441, 2.0327, 1.1632]
t = [4.2515, 1.172, 0.574]

import matplotlib.pyplot as plt
import numpy as np
from fit_model import *

# Interval = 6s , segment length = 12,  384 * 384
info= {'static': {'time': [4.788750648498535, 5.034250259399414, 5.084988355636597, 4.9478912353515625, 5.013004302978516, 4.947625398635864, 5.066121339797974, 5.059707880020142, 4.965874433517456, 5.043835401535034, 5.060317039489746, 5.0969953536987305, 5.036155939102173, 5.004553318023682], 'energy': [7.69, 7.42, 7.31, 6.94, 7.12, 6.97, 7.19, 7.04, 6.9, 7.03, 7.15, 7.08, 6.91, 7.02]}, 'network': {'time': [0.222, 0.247, 0.186, 0.211, 0.2, 0.204, 0.209, 0.213, 0.187, 0.213, 0.214, 0.183, 0.24, 0.186], 'energy': [0.58, 0.59, 0.42, 0.46, 0.44, 0.47, 0.46, 0.52, 0.41, 0.46, 0.49, 0.4, 0.52, 0.4]}, 'encoding': {'time': [1.005, 0.752, 0.762, 0.769, 0.818, 0.777, 0.76, 0.757, 0.731, 0.74, 0.737, 0.753, 0.755, 0.744], 'energy': [2.39, 1.5, 1.47, 1.47, 1.56, 1.46, 1.45, 1.46, 1.42, 1.4, 1.36, 1.39, 1.44, 1.4]}}
# Interval = 6s , segment length = 12,  192 * 192
info= {'static': {'time': [5.144951820373535, 5.343831300735474, 5.336036443710327, 5.220470905303955, 5.255597114562988, 5.223854303359985, 5.321363687515259, 5.323211193084717, 5.242335319519043, 5.343380689620972, 5.200533628463745, 5.3543078899383545, 5.209167957305908, 5.3383238315582275, 5.307269811630249, 5.209068775177002, 5.383795499801636, 5.208843946456909, 5.310437202453613, 5.30463981628418, 5.197141885757446, 5.295122861862183, 5.145842790603638], 'energy': [7.95, 7.8, 7.57, 7.29, 7.37, 7.23, 7.47, 7.47, 7.44, 7.56, 7.32, 7.47, 7.35, 7.52, 7.58, 7.34, 7.57, 7.29, 7.45, 7.59, 7.48, 7.55, 7.33]}, 'network': {'time': [0.083, 0.067, 0.06, 0.075, 0.085, 0.07, 0.071, 0.066, 0.066, 0.072, 0.071, 0.069, 0.074, 0.063, 0.073, 0.065, 0.057, 0.075, 0.073, 0.067, 0.088, 0.072, 0.067], 'energy': [0.22, 0.15, 0.13, 0.17, 0.18, 0.16, 0.17, 0.14, 0.15, 0.15, 0.16, 0.16, 0.16, 0.15, 0.16, 0.15, 0.13, 0.17, 0.17, 0.15, 0.2, 0.16, 0.15]}, 'encoding': {'time': [0.793, 0.625, 0.641, 0.639, 0.697, 0.637, 0.644, 0.645, 0.626, 0.626, 0.626, 0.645, 0.65, 0.637, 0.657, 0.662, 0.594, 0.654, 0.65, 0.665, 0.647, 0.669, 0.722], 'energy': [1.65, 1.18, 1.22, 1.2, 1.29, 1.18, 1.2, 1.21, 1.24, 1.17, 1.18, 1.18, 1.24, 1.21, 1.23, 1.25, 1.11, 1.24, 1.27, 1.28, 1.2, 1.23, 1.45]}}
# Interval = 6s , segment length = 12,  576 * 576
info= {'static': {'time': [4.395095586776733, 4.643601894378662, 4.59761905670166, 4.572222948074341, 4.6001505851745605, 4.584743976593018, 4.693969488143921, 4.427224636077881, 4.699794769287109, 4.698573589324951, 4.522579669952393, 4.694524049758911, 4.407015800476074, 4.565258026123047, 4.530092716217041, 4.480322599411011, 4.7878172397613525, 4.423928260803223], 'energy': [7.17, 6.94, 6.7, 6.65, 6.55, 6.63, 6.87, 6.6, 6.79, 7.56, 6.64, 6.84, 6.36, 6.63, 6.43, 6.46, 6.86, 6.35]}, 'network': {'time': [0.424, 0.406, 0.359, 0.485, 0.403, 0.377, 0.369, 0.43, 0.384, 0.384, 0.447, 0.389, 0.49, 0.454, 0.504, 0.441, 0.333, 0.451], 'energy': [1.12, 0.93, 0.8, 1.07, 0.93, 0.86, 0.82, 1.17, 0.84, 0.87, 1.06, 0.84, 1.09, 1.03, 1.14, 1.0, 0.77, 1.03]}, 'encoding': {'time': [1.216, 0.982, 0.976, 0.973, 1.042, 0.966, 0.973, 1.075, 0.952, 0.95, 0.964, 0.95, 1.031, 1.014, 0.996, 1.014, 0.917, 1.048], 'energy': [2.81, 1.91, 1.86, 1.84, 1.97, 1.79, 1.79, 1.91, 1.76, 1.79, 1.8, 1.83, 1.84, 1.8, 1.86, 1.86, 1.71, 1.9]}}
# Interval = 6s , segment length = 12,  320 * 320
info= {'static': {'time': [5.073009490966797, 5.0881054401397705, 5.070800542831421, 5.201466083526611, 5.079344272613525, 5.201092720031738, 5.202361822128296, 5.079505681991577, 5.187166690826416, 5.077932119369507, 5.165701389312744, 5.229408264160156, 5.0298566818237305, 5.235132694244385], 'energy': [8.05, 7.68, 7.19, 7.35, 7.05, 7.31, 7.25, 7.16, 7.25, 7.08, 7.22, 7.42, 7.13, 7.34]}, 'network': {'time': [0.155, 0.183, 0.135, 0.154, 0.154, 0.148, 0.151, 0.17, 0.152, 0.185, 0.175, 0.143, 0.185, 0.134], 'energy': [0.38, 0.41, 0.3, 0.35, 0.35, 0.33, 0.33, 0.38, 0.34, 0.38, 0.37, 0.32, 0.42, 0.31]}, 'encoding': {'time': [0.848, 0.729, 0.723, 0.675, 0.695, 0.682, 0.678, 0.678, 0.697, 0.671, 0.692, 0.665, 0.713, 0.667], 'energy': [1.75, 1.37, 1.41, 1.31, 1.31, 1.27, 1.29, 1.3, 1.3, 1.3, 1.32, 1.32, 1.34, 1.27]}}
# Interval = 6s , segment length = 12,  448 * 448
info= {'static': {'time': [4.699442148208618, 4.908058404922485, 4.781190633773804, 4.902903318405151, 4.695846080780029, 4.904622316360474, 4.8898937702178955, 4.78260064125061, 4.947208881378174, 4.8861565589904785, 4.912625551223755, 4.944926023483276, 4.804270029067993, 4.979692697525024, 4.801940441131592, 4.923316717147827, 5.0079121589660645, 4.7664594650268555, 4.913748264312744], 'energy': [7.46, 7.36, 6.85, 6.91, 6.51, 6.86, 6.77, 6.65, 6.8, 6.77, 6.73, 6.93, 6.58, 6.93, 6.65, 6.77, 6.91, 6.59, 6.88]}, 'network': {'time': [0.264, 0.284, 0.262, 0.3, 0.284, 0.245, 0.233, 0.275, 0.275, 0.255, 0.264, 0.234, 0.28, 0.243, 0.305, 0.268, 0.215, 0.278, 0.265], 'energy': [0.68, 0.64, 0.58, 0.66, 0.64, 0.55, 0.54, 0.62, 0.59, 0.56, 0.59, 0.52, 0.6, 0.54, 0.67, 0.6, 0.48, 0.62, 0.59]}, 'encoding': {'time': [1.086, 0.834, 0.882, 0.825, 0.945, 0.885, 0.902, 0.873, 0.803, 0.794, 0.856, 0.857, 0.846, 0.811, 0.826, 0.842, 0.813, 0.89, 0.851], 'energy': [2.23, 1.6, 1.67, 1.55, 1.75, 1.61, 1.61, 1.58, 1.51, 1.44, 1.52, 1.53, 1.57, 1.5, 1.53, 1.53, 1.5, 1.57, 1.58]}}
# Interval = 6s , segment length = 12,  640 * 640
info= {'static': {'time': [4.201647996902466, 4.4222493171691895, 4.406054258346558, 4.456302165985107, 4.268808126449585, 4.412967681884766, 4.438122510910034, 4.2535905838012695, 4.39648175239563, 4.301746606826782, 4.345511436462402, 4.450211763381958, 4.135083436965942, 4.449106454849243, 4.151639223098755, 4.386431932449341, 4.553714752197266, 4.3294758796691895, 4.331989526748657], 'energy': [6.73, 6.49, 6.47, 6.47, 6.06, 6.29, 6.26, 6.01, 6.21, 6.12, 6.11, 6.29, 5.92, 6.3, 5.88, 6.19, 6.58, 6.18, 6.1]}, 'network': {'time': [0.586, 0.565, 0.457, 0.516, 0.551, 0.528, 0.522, 0.523, 0.563, 0.531, 0.587, 0.494, 0.604, 0.464, 0.664, 0.527, 0.453, 0.523, 0.555], 'energy': [1.47, 1.27, 1.04, 1.17, 1.22, 1.18, 1.14, 1.17, 1.24, 1.18, 1.34, 1.1, 1.34, 1.03, 1.43, 1.16, 1.01, 1.15, 1.25]}, 'encoding': {'time': [1.256, 1.05, 1.071, 1.058, 1.107, 1.095, 1.07, 1.166, 1.06, 1.095, 1.102, 1.087, 1.189, 1.118, 1.115, 1.119, 1.029, 1.076, 1.149], 'energy': [2.54, 2.01, 1.99, 2.0, 2.03, 2.07, 1.94, 2.03, 2.01, 1.96, 2.03, 1.95, 2.1, 1.99, 2.02, 2.01, 1.87, 2.01, 2.14]}}
# Interval = 6s , segment length = 9,  640 * 640
info= {'static': {'time': [4.7546916007995605, 4.79768705368042, 4.714487075805664, 4.9446635246276855, 4.86253023147583, 4.702573537826538, 4.748329162597656, 4.8026909828186035, 4.922759771347046, 4.820086717605591, 4.7251434326171875, 4.896772623062134, 4.726824760437012, 4.784497022628784, 4.692569017410278], 'energy': [7.81, 7.2, 6.84, 7.07, 6.87, 6.72, 6.7, 6.77, 7.07, 6.82, 6.73, 6.79, 6.7, 6.73, 6.55]}, 'network': {'time': [0.354, 0.415, 0.4, 0.291, 0.374, 0.389, 0.398, 0.329, 0.335, 0.376, 0.373, 0.354, 0.426, 0.422, 0.426], 'energy': [0.86, 0.92, 0.88, 0.64, 0.82, 0.9, 0.88, 0.79, 0.74, 0.85, 0.82, 0.76, 0.93, 0.97, 0.94]}, 'encoding': {'time': [0.928, 0.816, 0.812, 0.792, 0.792, 0.842, 0.886, 0.798, 0.777, 0.832, 0.833, 0.779, 0.773, 0.816, 0.8], 'energy': [2.11, 1.58, 1.54, 1.47, 1.47, 1.53, 1.57, 1.49, 1.44, 1.55, 1.54, 1.42, 1.43, 1.5, 1.47]}}
# Interval = 6s , segment length = 15,  640 * 640
info= {'static': {'time': [3.7180888652801514, 3.9095189571380615, 4.115858316421509, 3.990866184234619, 3.8926329612731934, 3.9956493377685547, 3.9089348316192627, 4.111874341964722, 4.000958681106567, 3.8972060680389404, 4.018531799316406, 3.862248182296753, 3.918370485305786, 4.1610236167907715, 3.915107488632202, 3.974520444869995], 'energy': [5.74, 5.71, 5.83, 5.71, 5.53, 5.56, 5.46, 5.77, 5.59, 5.42, 5.59, 5.35, 5.58, 5.87, 5.53, 5.57]}, 'network': {'time': [0.712, 0.583, 0.575, 0.745, 0.647, 0.65, 0.676, 0.622, 0.693, 0.661, 0.64, 0.711, 0.669, 0.606, 0.677, 0.66], 'energy': [1.75, 1.3, 1.26, 1.64, 1.44, 1.45, 1.47, 1.36, 1.58, 1.42, 1.42, 1.56, 1.46, 1.32, 1.51, 1.48]}, 'encoding': {'time': [1.644, 1.437, 1.34, 1.364, 1.325, 1.393, 1.341, 1.294, 1.343, 1.376, 1.374, 1.355, 1.383, 1.322, 1.335, 1.4], 'energy': [3.29, 2.59, 2.5, 2.5, 2.48, 2.48, 2.41, 2.35, 2.43, 2.46, 2.45, 2.45, 2.41, 2.36, 2.48, 2.49]}}


info= {'static': {'time': [4.146805286407471, 3.7977423667907715, 3.999742269515991, 4.338484525680542, 3.8848674297332764, 4.092969179153442, 3.7733123302459717, 4.378485202789307, 3.7768077850341797, 4.225445985794067, 3.748302459716797, 4.021557569503784, 3.9407074451446533, 4.270493507385254, 4.096147298812866, 3.9630799293518066, 4.105583429336548, 3.9398815631866455, 4.241340637207031, 3.9020955562591553, 4.32915472984314, 3.495743989944458, 4.374557971954346, 3.5857818126678467, 4.424665927886963], 'energy': [7.02, 5.89, 6.09, 6.6, 6.07, 5.68, 6.4, 5.46, 5.52, 5.29, 5.69, 5.47, 5.93, 5.71, 5.55, 5.79, 5.59, 5.89, 5.46, 6.01, 4.86, 6.02, 5.12, 6.31]}, 'network': {'time': [0.724, 0.882, 0.868, 0.51, 0.956, 0.547, 1.068, 0.531, 1.12, 0.569, 1.284, 0.627, 0.971, 0.517, 0.809, 0.808, 0.648, 0.931, 0.543, 1.042, 0.485, 1.107, 0.561, 1.265, 0.421], 'energy': [1.64, 1.9, 1.69, 1.06, 1.21, 1.97, 1.17, 2.01, 1.07, 2.26, 1.34, 1.75, 0.99, 1.61, 1.6, 1.39, 1.75, 1.14, 1.88, 1.01, 2.03, 1.17, 2.3, 0.9]}, 'encoding': {'time': [1.211, 1.35, 1.076, 1.179, 1.196, 1.293, 1.086, 1.154, 1.109, 1.131, 1.106, 1.183, 1.125, 1.142, 1.227, 1.159, 1.183, 1.157, 1.144, 1.196, 1.112, 1.332, 1.122, 1.156, 1.088], 'energy': [2.57, 3.12, 2.2, 2.2,  2.54, 2.26, 2.21, 2.12, 1.97, 2.08, 2.24, 2.13, 2.13, 2.28, 2.23, 2.19, 2.12, 2.17, 2.25, 2.05, 2.99, 2.12, 2.15, 2.02]}}


print("###############################################")
x = np.array([np.average(info["static"]["energy"]), np.average(info["encoding"]["energy"]), np.average(info["network"]["energy"])])
x = np.round(x, 4)
print("e=", list(x))
t = np.array([np.average(info["static"]["time"]), np.average(info["encoding"]["time"]), np.average(info["network"]["time"])])
t = np.round(t, 4)
print("t=", list(t))


###############################################################################################
# Interval = 2s , segment length = 6,  640 * 640
e = [1.689, 1.039, 0.6688]
t = [1.144, 0.549, 0.301]

# Interval = 6s , segment length = 9,  640 * 640
e = [6.8913, 1.5407, 0.8467]
t = [4.7931, 0.8184, 0.3775]

# Interval = 6s , segment length = 12,  640 * 640
e = [6.2453, 2.0368, 1.2047]
t = [4.3522, 1.1059, 0.5375]

# Interval = 6s , segment length = 15,  640 * 640
e = [5.6131, 2.5081, 1.4638]
t = [3.962, 1.3766, 0.6579]

###############################################################################################
# Interval = 6s , segment length = 12 ,  640 * 640
e= [6.2453, 2.0368, 1.2047]
t= [4.3522, 1.1059, 0.5375]

# Interval = 6s , segment length = 12,  576 * 576
e= [6.7239, 1.8906, 0.965]
t= [4.5736, 1.0022, 0.4183]

# Interval = 6s , segment length = 12,  512 * 512
e= [6.7707, 1.702, 0.7933]
t= [4.7477, 0.8987, 0.3496]

# Interval = 6s , segment length = 12,  448 * 448
e= [6.8374, 1.5989, 0.5932]
t= [4.8659, 0.8643, 0.2647]

# Interval = 6s , segment length = 12,  384 * 384
e= [7.1264, 1.5121, 0.4729]
t= [5.0107, 0.7757, 0.2082]

# Interval = 6s , segment length = 12,  320 * 320
e= [7.32, 1.3471, 0.355]
t= [5.1372, 0.7009, 0.1589]

# Interval = 6s , segment length = 12,  192 * 192
e= [7.4778, 1.2439, 0.1604]
t= [5.2704, 0.6544, 0.0708]

r = [192 * 192, 320 * 320, 384 * 384, 448 * 448, 512 * 512, 576 * 576, 640 * 640]

e_coding = np.array([1.2439, 1.3471, 1.5121, 1.5989, 1.702, 1.8906, 2.0964]) / 12
e_network = np.array([0.1604, 0.355, 0.4729, 0.5932, 0.7933, 0.965, 1.3136] ) / 12

t_coding = np.array([0.6544, 0.7009, 0.7757, 0.8643, 0.8987,1.0022, 1.1151]  ) / 12
t_network =np.array( [0.0708, 0.1589, 0.2082, 0.2647, 0.3496, 0.4183, 0.5642]) / 12

fit3(t_network, x=r, eva=r, gt=t_network)

plt.show()

"""
0.095306224196092 + 0.000000189213298 * x
e_coding = [1.2439, 1.3471, 1.5121, 1.5989, 1.702, 1.8906, 2.0368] / 12
e_coding_p = [0.10228138319655002, 0.11468166586403028, 0.12320686019792298, 0.1332820898652507, 0.14490735486601347, 0.15808265520021125, 0.17280799086784407]

0.002588334342357 + 0.000000247940226 * x
e_network = [0.1604, 0.355, 0.4729, 0.5932, 0.7933, 0.965, 1.2047] / 12
e_network_p = [0.01172840284721491, 0.027977413522518292, 0.03914860836178937, 0.05235092953547337, 0.06758437704357029, 0.08484895088608013, 0.1041446510630029]

0.049440340280028 + 0.000000103866600 * x
t_coding = [0.6544, 0.7009, 0.7757, 0.8643, 0.8987,1.0022, 1.1059] / 12
t_coding_p = [0.053269278638155296, 0.06007628016371434, 0.0647560937125362, 0.07028678245205291, 0.07666834638226452, 0.08390078550317101, 0.09198409981477239]

0.001646107905526 + 0.000000105996991 * x
t_network = [0.0708, 0.1589, 0.2082, 0.2647, 0.3496, 0.4183, 0.5375] / 12
t_network_p = [0.005553580989710533, 0.012500199806038911, 0.017276000242264673, 0.022920128030531478, 0.029432583170839334, 0.036813365663188234, 0.045062475507578185]
"""
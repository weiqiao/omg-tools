import sys
sys.path.append("/home/ruben/Documents/Work/Programs/motionplanningtoolbox/")
from motionplanning import *


# create vehicle
vehicle = Holonomic()

# at start only constraints up to 1st derivative
vehicle.options['boundary_smoothness']['initial'] = 1
vehicle.set_options({'safety_distance': 0.1})

vehicle.set_initial_pose([-1.5, -1.5])
vehicle.set_terminal_pose([2., 2.])

# create environment
environment = Environment(room={'shape': Square(2.5)}, vehicles=vehicle)
rectangle = Rectangle(width=3., height=0.2)
environment.add_obstacle(Obstacle({'position': [-2.1, -0.5]}, shape=rectangle))
environment.add_obstacle(Obstacle({'position': [1.7, -0.5]}, shape=rectangle))
trajectory = {'velocity': np.vstack([[3., -0.15, 0.0], [4., 0., 0.15]])}
environment.add_obstacle(Obstacle({'position': [1.5, 0.5]}, shape=Circle(0.4),
                                  trajectory=trajectory))

# create a point-to-point problem
codegen = {'compileme': False, 'codegen': True, 'buildname': 'quadrotor'}
problem = Point2point(environment, options={'codegen': codegen})

# create simulator
simulator = Simulator(problem)
simulator.plot.set_options({'knots': True})
simulator.plot.create('2d')
simulator.plot.create('input')

# run it!
simulator.run()

# show/save some results
problem.plot.show_movie('2d', number_of_frames=100, repeat=False)
# problem.plot.save_movie('input', 5, 'holonomic')
# problem.plot.show('input')

plt.show(block=True)

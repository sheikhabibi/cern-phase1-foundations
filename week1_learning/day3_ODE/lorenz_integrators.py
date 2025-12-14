import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
import time



def lorenz(t, state, sigma, rho, beta):
    x,y,z = state

    dx_dt = sigma*(y-x)
    dy_dt = x*(rho-z)-y
    dz_dt = x*y - beta*z

    return(dx_dt, dy_dt, dz_dt)

initial_state = [1.0, 1.0, 1.0]
t_span = (0, 40)    # solve_ivp only wants the starting and ending time

methods = ['RK45', 'BDF', 'DOP853']

for i, method in enumerate(methods):
    start = time.time()
    solution = sci.solve_ivp( 
                lorenz,
                t_span,
                initial_state,
                t_eval=np.linspace(0, 40, 5000),
                method=method,
                args=(10, 28, 8/3)
            )
    duration = time.time() - start
    print(f"Done {method}: ({duration}s)")

    # print(f"Time taken to solve {method}: {(time.time()-start_time):.4f} sec")
    # print(np.size(solution.y))

    x_values = solution.y[0]
    y_values = solution.y[1]
    z_values = solution.y[2]

    # setup the 3d plot
    # fig = plt.figure(figsize=(10,7))            # blank canvas
    # ax = fig.add_subplot(projection='3d')       # turn it into a 3D box
    ax = plt.subplot(1, 3, i+1, projection='3d')


    # draw the trajectory
    ax.plot(x_values, y_values, z_values, lw=0.5, color='purple')

    # make it pretty (labels)
    # ax.set_title("The Lorenz Attractor")
    ax.set_title(f"{method}\nTime: {duration:.4f}s")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")

plt.tight_layout()
plt.show()
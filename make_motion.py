import math

lat0_deg = 60.0
lon0_deg = 25.0
height = 100.0

R = 100.0
T = 60.0  # period of one revolution
dt = 1.0    # time step in seconds
duration = 60.0   # total simulation time in seconds

lat0 = math.radians(lat0_deg)
lon0 = math.radians(lon0_deg)

Re = 6378137.0    # WGS-84 earth equatorial radius (meters)
omega = 2 * math.pi / T   # angular velocity in rad/s

def timestamp(t):
    t = int(t)
    hh = t // 3600
    mm = (t % 3600) // 60
    ss = t % 60
    return f"{hh:02d}:{mm:02d}:{ss:02d}"

with open("circular_motion.txt", "w") as f:

    t = 0
    while t <= duration:
        
       # Circular motion in local NED frame
        north = R * math.cos(omega * t)
        east  = R * math.sin(omega * t)

        lat = lat0 + (north / Re)
        lon = lon0 + (east / (Re * math.cos(lat0)))

       # Velocity components
        vel_n = -R * omega * math.sin(omega * t)
        vel_e =  R * omega * math.cos(omega * t)
        vel_d = 0.0

       # Centripetal acceleration components
        acc_n = -R * omega * omega * math.cos(omega * t)
        acc_e = -R * omega * omega * math.sin(omega * t)
        acc_d = 0.0

        line = (
            f"{timestamp(t)},MOTB,v1_m1,"
            f"{lat:.12f},{lon:.12f},{height:.2f},"
            f"{vel_n:.6f},{vel_e:.6f},{vel_d:.6f},"
            f"{acc_n:.6f},{acc_e:.6f},{acc_d:.6f}\n"
        )

        f.write(line)
        t += dt

print("Motion file created successfully!")

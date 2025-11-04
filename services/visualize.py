import matplotlib.pyplot as plt
import time

def visualize_live(polygon, results, delay=0.5):
    plt.ion()  
    fig, ax = plt.subplots()

   
    poly_x, poly_y = zip(*polygon)
    ax.plot(poly_x + (poly_x[0],), poly_y + (poly_y[0],), "b--", label="Geofence")

    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title("Aegis Real-Time Geofence Monitor")
    ax.legend()


    for point, status in results:
        color = "green" if status == "Safe" else "red"
        ax.plot(point[0], point[1], "o", color=color, markersize=8)
        ax.annotate(status, (point[0], point[1]), textcoords="offset points", xytext=(5,5), fontsize=8)
        
        plt.draw()          
        plt.pause(delay)     
        fig.canvas.flush_events()  
        time.sleep(delay)    
    plt.ioff()
    plt.show()

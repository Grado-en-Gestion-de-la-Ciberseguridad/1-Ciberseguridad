import numpy as np # Importar la librería de álgebra lineal
import matplotlib.pyplot as plt # Importar la librería de visualización de graficos
from matplotlib.animation import FuncAnimation # Importar la clase FuncAnimation para la animación

# ------------------ Variables de la red ------------------
# Parámetros para la generación de la red
n_switches = 11  # Número de nodos que representan switches en la red
n_endpoints = 500  # Número de nodos que representan endpoints (dispositivos finales)
n_nodes = n_switches + n_endpoints  # Número total de nodos en la red
prob_connection_switches = 1  # Probabilidad de conexión entre switches
# ------------------ Simulación de la propagación de malware ------------------
# Parámetros del modelo SIR (Susceptibles, Infectados, Recuperados)
beta = 0.2 # Tasa de infección: probabilidad de que un nodo susceptible se infecte al estar conectado a un nodo infectado
gamma = 0.1 # Tasa de recuperación: probabilidad de que un nodo infectado se recupere en cada paso
time_steps = 100  # Número de pasos temporales para la simulación (tiempo discreto)

# ------------------ Creación de la red ------------------
# Crear una matriz de adyacencia para representar la red
np.random.seed(42)  # Semilla para reproducibilidad (garantiza los mismos resultados aleatorios)
adj_matrix = np.zeros((n_nodes, n_nodes), dtype=int)  # Inicializa una matriz de adyacencia vacía


# Conectar switches entre sí
for i in range(n_switches):  # Iterar sobre cada switch
    for j in range(i + 1, n_switches):  # Conectar solo con los switches posteriores
        if np.random.rand() < prob_connection_switches:  # 30% de probabilidad de conexión entre switches
            adj_matrix[i, j] = adj_matrix[j, i] = 1  # Representa una conexión bidireccional

# Conectar endpoints a switches
for endpoint in range(n_switches, n_nodes):  # Iterar sobre los nodos que representan endpoints
    connected_switch = np.random.randint(0, n_switches)  # Seleccionar un switch al azar
    adj_matrix[endpoint, connected_switch] = adj_matrix[connected_switch, endpoint] = 1  # Crear conexión bidireccional

# ------------------ Inicialización de los estados de los nodos ------------------
# Inicializar los estados de los nodos (0: Susceptible, 1: Infectado, 2: Recuperado)
states = np.zeros(n_nodes, dtype=int)  # Todos los nodos comienzan como susceptibles
states[n_switches] = 1  # Infectar inicialmente un endpoint

# ------------------ Visualización de la propagación ------------------
# Configuración para la visualización
positions = np.random.rand(n_nodes, 2)  # Generar posiciones aleatorias para los nodos en un espacio 2D
colors = {0: "blue", 1: "red", 2: "green"}  # Colores para cada estado: azul (susceptible), rojo (infectado), verde (recuperado)

# Configuración del gráfico
fig, ax = plt.subplots(figsize=(12, 8))  # Crear una figura y un eje con dimensiones específicas
scat = ax.scatter(positions[:, 0], positions[:, 1], c=[colors[s] for s in states], s=100, edgecolors="black")  # Dibujar nodos

# Dibujar conexiones (aristas) entre los nodos
for i in range(n_nodes):
    for j in range(i + 1, n_nodes):
        if adj_matrix[i, j] == 1:  # Si hay una conexión en la matriz de adyacencia
            ax.plot([positions[i, 0], positions[j, 0]], [positions[i, 1], positions[j, 1]], "gray", alpha=0.3)  # Dibujar línea

# ------------------ Función de actualización para la animación ------------------
# Función de actualización para la animación
def update(frame):
    global states  # Usar la variable global de estados
    new_states = states.copy()  # Crear una copia de los estados actuales para actualizarla
    for node in range(n_nodes):  # Iterar sobre cada nodo
        if states[node] == 0:  # Nodo susceptible
            neighbors = np.where(adj_matrix[node] > 0)[0]  # Encontrar los vecinos conectados
            for neighbor in neighbors:  # Revisar cada vecino
                if states[neighbor] == 1 and np.random.rand() < beta:  # Si un vecino está infectado y ocurre infección
                    new_states[node] = 1  # Nodo se infecta
                    break
        elif states[node] == 1:  # Nodo infectado
            if np.random.rand() < gamma:  # Si ocurre recuperación
                new_states[node] = 2  # Nodo se recupera
    states = new_states  # Actualizar los estados
    # Actualizar los colores de los nodos
    scat.set_color([colors[s] for s in states])
    return scat,

# Animación
ani = FuncAnimation(fig, update, frames=time_steps, interval=500, blit=True)  # Reiniciar la animación cada 500 ms, con los valores nuevos de la función update
# Mostrar la visualización
# plt.title("Propagación de Malware en una Red Grande (Modelo SIR)")  # Título del gráfico
plt.axis("off")  # Ocultar los ejes
# ani.save("malware_spread.gif", writer="imagemagick")  # Guardar la animación como un archivo GIF
plt.show()  # Mostrar la visualización
import tkinter as tk
from tkinter import ttk
import numpy as np
import pygad
import random



def calcular_capacidad(probabilidades: np.ndarray, prob_entradas: np.ndarray):
    cant_b = probabilidades.shape[1]
    aux = np.tile(prob_entradas, [cant_b, 1]).transpose()
    prioriB = np.sum(probabilidades * aux, 0)
    inv_priori_B = np.zeros_like(prioriB)
    inv_priori_B[prioriB != 0] = 1 / prioriB[prioriB != 0]
    logaritmos_B = np.zeros_like(inv_priori_B)
    logaritmos_B[inv_priori_B != 0] = np.log2(inv_priori_B[inv_priori_B != 0])
    HB = np.sum(prioriB * logaritmos_B)
    inversas = np.zeros_like(probabilidades)
    inversas[probabilidades != 0] = 1 / probabilidades[probabilidades != 0]
    logaritmos = np.zeros_like(inversas)
    logaritmos[inversas != 0] = np.log2(inversas[inversas != 0])
    HBA = np.sum(prob_entradas * np.sum(probabilidades * logaritmos, 1))
    return HB - HBA

def fitness_func(probabilidades:np.ndarray, solution:np.ndarray):
    negativo = 0
    for i in range(solution.shape[0]):
        if solution[i] < 0:
            negativo -= 10
    if negativo < 0:
        return negativo
    if not 0.9999 <= sum(solution) <= 1.0001:
        return -np.abs(solution.sum() - 1)
    return calcular_capacidad(probabilidades, solution)

def generar_probabilidades_aleatorias(n):
    probabilidades = [random.random() for _ in range(n)]
    suma_total = sum(probabilidades)
    probabilidades_normalizadas = [p / suma_total for p in probabilidades]
    return probabilidades_normalizadas

def calculate_capacity(probabilidades:np.ndarray, result_label: tk.Label, labels: list[str]):
    fitness_function = lambda ga_instance, solution, solution_idx : fitness_func(probabilidades, solution)

    num_generations = 50000
    num_parents_mating = 4
    parent_selection_type = "sss"
    keep_parents = 1
    crossover_type = "single_point"
    mutation_type = "random"
    mutation_percent_genes = 10

    initial_population = []
    for _ in range(5):
        initial_population.append(generar_probabilidades_aleatorias(probabilidades.shape[0]))
    initial_population.append([1/probabilidades.shape[0] for _ in range(probabilidades.shape[0])])

    ga_instance = pygad.GA(num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes,
                           initial_population=initial_population)
    
    ga_instance.run()

    solucion = ga_instance.best_solution()
    
    result_text = f"Resultados: {solucion[1]:.4f}\n"
    for label, value in zip(labels, solucion[0]):
        result_text += f"{label}: {value:.4f}\n"

    result_label.config(text=result_text)

root = tk.Tk()
root.title("Capacidad de Canal")
root.geometry("500x600")

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame_binario = ttk.Frame(notebook)
frame_ternario = ttk.Frame(notebook)
frame_cuaternario = ttk.Frame(notebook)

notebook.add(frame_binario, text="Canal Binario")
notebook.add(frame_ternario, text="Canal Ternario")
notebook.add(frame_cuaternario, text="Canal Cuaternario")

# Canal Binario
lbl_binario = tk.Label(frame_binario, text="Ingrese las Probabilidades")
lbl_binario.grid(row=0, column=0, columnspan=2, pady=10)

entries_binario = {}
labels_binario = ["p(A/A)", "p(B/A)", "p(A/B)", "p(B/B)"]
for i in range(2):
    for j in range(2):
        lbl = tk.Label(frame_binario, text=labels_binario[i*2 + j])
        lbl.grid(row=i+1, column=j*2, padx=10, pady=5)
        entry = tk.Entry(frame_binario)
        entry.grid(row=i+1, column=j*2+1, padx=10, pady=5)
        entries_binario[labels_binario[i*2 + j]] = entry

btn_calculate_binario = tk.Button(frame_binario, text="Calcular", command=lambda: calculate_capacity(
    np.array([[float(entries_binario["p(A/A)"].get()), float(entries_binario["p(B/A)"].get())], 
              [float(entries_binario["p(A/B)"].get()), float(entries_binario["p(B/B)"].get())]]), 
    lbl_result_binario, ["p(A)", "p(B)"]))
btn_calculate_binario.grid(row=4, column=0, columnspan=4, pady=20)

lbl_result_binario = tk.Label(frame_binario, text="Resultados:")
lbl_result_binario.grid(row=5, column=0, columnspan=4, pady=10)

# Canal Ternario
lbl_ternario = tk.Label(frame_ternario, text="Ingrese las Probabilidades")
lbl_ternario.grid(row=0, column=0, columnspan=3, pady=10)

entries_ternario = {}
labels_ternario = ["p(A/A)", "p(B/A)", "p(C/A)", "p(A/B)", "p(B/B)", "p(C/B)", "p(A/C)", "p(B/C)", "p(C/C)"]
for i in range(3):
    for j in range(3):
        lbl = tk.Label(frame_ternario, text=labels_ternario[i*3 + j])
        lbl.grid(row=i+1, column=j*2, padx=10, pady=5)
        entry = tk.Entry(frame_ternario)
        entry.grid(row=i+1, column=j*2+1, padx=10, pady=5)
        entries_ternario[labels_ternario[i*3 + j]] = entry

btn_calculate_ternario = tk.Button(frame_ternario, text="Calcular", command=lambda: calculate_capacity(
    np.array([
        [float(entries_ternario[labels_ternario[0]].get()), float(entries_ternario[labels_ternario[1]].get()), float(entries_ternario[labels_ternario[2]].get())],
        [float(entries_ternario[labels_ternario[3]].get()), float(entries_ternario[labels_ternario[4]].get()), float(entries_ternario[labels_ternario[5]].get())],
        [float(entries_ternario[labels_ternario[6]].get()), float(entries_ternario[labels_ternario[7]].get()), float(entries_ternario[labels_ternario[8]].get())]
    ]),
    lbl_result_ternario, ["p(A)", "p(B)", "p(C)"]))
btn_calculate_ternario.grid(row=4, column=0, columnspan=6, pady=20)

lbl_result_ternario = tk.Label(frame_ternario, text="Resultados:")
lbl_result_ternario.grid(row=5, column=0, columnspan=6, pady=10)

# Canal Cuaternario
lbl_cuaternario = tk.Label(frame_cuaternario, text="Ingrese las Probabilidades")
lbl_cuaternario.grid(row=0, column=0, columnspan=4, pady=10)

entries_cuaternario = {}
labels_cuaternario = [
    "p(A/A)", "p(B/A)", "p(C/A)", "p(D/A)", 
    "p(A/B)", "p(B/B)", "p(C/B)", "p(D/B)", 
    "p(A/C)", "p(B/C)", "p(C/C)", "p(D/C)", 
    "p(A/D)", "p(B/D)", "p(C/D)", "p(D/D)"
]
for i in range(4):
    for j in range(4):
        lbl = tk.Label(frame_cuaternario, text=labels_cuaternario[i*4 + j])
        lbl.grid(row=i+1, column=j*2, padx=10, pady=5)
        entry = tk.Entry(frame_cuaternario)
        entry.grid(row=i+1, column=j*2+1, padx=10, pady=5)
        entries_cuaternario[labels_cuaternario[i*4 + j]] = entry

btn_calculate_cuaternario = tk.Button(frame_cuaternario, text="Calcular", command=lambda: calculate_capacity(
    np.array([
        [float(entries_cuaternario[labels_cuaternario[0]].get()), float(entries_cuaternario[labels_cuaternario[1]].get()), float(entries_cuaternario[labels_cuaternario[2]].get()), float(entries_cuaternario[labels_cuaternario[3]].get())],
        [float(entries_cuaternario[labels_cuaternario[4]].get()), float(entries_cuaternario[labels_cuaternario[5]].get()), float(entries_cuaternario[labels_cuaternario[6]].get()), float(entries_cuaternario[labels_cuaternario[7]].get())],
        [float(entries_cuaternario[labels_cuaternario[8]].get()), float(entries_cuaternario[labels_cuaternario[9]].get()), float(entries_cuaternario[labels_cuaternario[10]].get()), float(entries_cuaternario[labels_cuaternario[11]].get())],
        [float(entries_cuaternario[labels_cuaternario[12]].get()), float(entries_cuaternario[labels_cuaternario[13]].get()), float(entries_cuaternario[labels_cuaternario[14]].get()), float(entries_cuaternario[labels_cuaternario[15]].get())]
    ]),
    lbl_result_cuaternario, ["p(A)", "p(B)", "p(C)", "p(D)"]))
btn_calculate_cuaternario.grid(row=5, column=0, columnspan=8, pady=20)

lbl_result_cuaternario = tk.Label(frame_cuaternario, text="Resultados:")
lbl_result_cuaternario.grid(row=6, column=0, columnspan=8, pady=10)

root.mainloop()
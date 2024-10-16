# app.py
import tkinter as tk
from tkinter import messagebox
import sqlite3
import random
import matplotlib.pyplot as plt

def criar_banco():
    conexao = sqlite3.connect("diario_emagrecimento.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            refeicoes TEXT,
            exercicios TEXT,
            sentimentos TEXT,
            data TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conexao.commit()
    conexao.close()

def criar_tabela_dietas():
    conexao = sqlite3.connect("diario_emagrecimento.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dietas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            descricao TEXT
        )
    """)
    conexao.commit()
    conexao.close()

def criar_tabela_frases():
    conexao = sqlite3.connect("diario_emagrecimento.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS frases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT
        )
    """)
    conexao.commit()
    conexao.close()

def criar_tabela_peso():
    conexao = sqlite3.connect("diario_emagrecimento.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS peso (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            peso REAL,
            data TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conexao.commit()
    conexao.close()

def criar_tabela_objetivos():
    conexao = sqlite3.connect("diario_emagrecimento.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS objetivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            objetivo REAL,
            data TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conexao.commit()
    conexao.close()

def adicionar_dietas():
    dietas = [
        ("Dieta da Sopa", "Uma dieta de baixo carboidrato que envolve sopas e vegetais."),
        ("Dieta Mediterrânea", "Foca em frutas, legumes, nozes e azeite de oliva."),
        ("Dieta Low Carb", "Reduz a ingestão de carboidratos e aumenta as proteínas."),
    ]
    
    conexao = sqlite3.connect("diario_emagrecimento.db")
    cursor = conexao.cursor()
    
    for dieta in dietas:
        cursor.execute("INSERT INTO dietas (nome, descricao) VALUES (?, ?)", dieta)
    
    conexao.commit()
    conexao.close()

def adicionar_frases():
    frases = [
        ("Você é mais forte do que pensa!"),
        ("Cada passo conta na sua jornada!"),
        ("O sucesso é a soma de pequenos esforços!"),
    ]

    conexao = sqlite3.connect("diario_emagrecimento.db")
    cursor = conexao.cursor()
    
    for frase in frases:
        cursor.execute(f"INSERT INTO frases (texto) VALUES ('{frase}')")
    
    conexao.commit()
    conexao.close()

def iniciar_app():
    criar_banco()
    criar_tabela_dietas()
    criar_tabela_frases()
    criar_tabela_peso()
    criar_tabela_objetivos()
    adicionar_dietas()  # Adiciona dietas iniciais
    adicionar_frases()  # Adiciona frases iniciais

    janela = tk.Tk()
    janela.title("Diário de Emagrecimento")
    janela.geometry("400x500")

    label_bem_vindo = tk.Label(janela, text="Bem-vindo ao Diário de Emagrecimento!", font=("Arial", 16))
    label_bem_vindo.pack(pady=20)

    botao_registrar = tk.Button(janela, text="Registrar um Dia", command=registrar_dia)
    botao_registrar.pack(pady=10)

    botao_dieta = tk.Button(janela, text="Sugestões de Dietas", command=sugerir_dieta)
    botao_dieta.pack(pady=10)

    botao_frase = tk.Button(janela, text="Frase Motivacional", command=mostrar_frase_motivacional)
    botao_frase.pack(pady=10)

    botao_registrar_peso = tk.Button(janela, text="Registrar Peso", command=registrar_peso)
    botao_registrar_peso.pack(pady=10)

    botao_visualizar_evolucao = tk.Button(janela, text="Visualizar Evolução", command=visualizar_evolucao)
    botao_visualizar_evolucao.pack(pady=10)

    botao_analisar_humor = tk.Button(janela, text="Analisar Humor", command=analisar_humor)
    botao_analisar_humor.pack(pady=10)

    botao_definir_objetivo = tk.Button(janela, text="Definir Objetivo de Peso", command=definir_objetivo)
    botao_definir_objetivo.pack(pady=10)

    botao_feedback = tk.Button(janela, text="Enviar Feedback", command=coletar_feedback)
    botao_feedback.pack(pady=10)

    botao_suporte = tk.Button(janela, text="Suporte e Atualizações", command=mostrar_suporte)
    botao_suporte.pack(pady=10)

    janela.mainloop()

def registrar_dia():
    janela_registro = tk.Toplevel()
    janela_registro.title("Registrar um Dia")
    janela_registro.geometry("300x250")

    tk.Label(janela_registro, text="Refeições:").pack(pady=5)
    entrada_refeicoes = tk.Entry(janela_registro)
    entrada_refeicoes.pack(pady=5)

    tk.Label(janela_registro, text="Exercícios:").pack(pady=5)
    entrada_exercicios = tk.Entry(janela_registro)
    entrada_exercicios.pack(pady=5)

    tk.Label(janela_registro, text="Sentimentos:").pack(pady=5)
    entrada_sentimentos = tk.Entry(janela_registro)
    entrada_sentimentos.pack(pady=5)

    botao_salvar = tk.Button(janela_registro, text="Salvar", command=lambda: salvar_registro(entrada_refeicoes.get(), entrada_exercicios.get(), entrada_sentimentos.get()))
    botao_salvar.pack(pady=20)

def salvar_registro(refeicoes, exercicios, sentimentos):
    conexao = sqlite3.connect("diario_emagrecimento.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO registros (refeicoes, exercicios, sentimentos) VALUES (?, ?, ?)", (refeicoes, exercicios, sentimentos))
    conexao.commit()
    conexao.close()
    messagebox.showinfo("Registro Salvo", "Seu registro foi salvo com sucesso!")

def sugerir_dieta():
    conexao = sqlite3.connect("diario_emagrecimento.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, descricao FROM dietas")
    dietas = cursor.fetchall()
    conexao.close()

    if dietas:
        dieta_sugerida = random.choice(dietas)
        messagebox.showinfo("Dieta Sugerida", f"{dieta_sugerida[0]}: {dieta_sugerida[1]}")
    else:
        messagebox.showwarning("Dieta Sugerida", "Nenhuma dieta disponível.")

def mostrar_frase_motivacional():
    conexao = sqlite3.connect("diario_emagrecimento.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT texto FROM frases")
    frases = cursor.fetchall()
    conexao.close()

    if frases:
        frase_sugerida = random.choice(frases)
        messagebox.showinfo("Frase Motivacional", frase_sugerida[0])
    else:
        messagebox.showwarning("Frase Motivacional", "Nenhuma frase disponível.")

def registrar_peso():
    janela_peso = tk.Toplevel()
    janela_peso.title("Registrar Peso")
    janela_peso.geometry("300x150")

    tk.Label(janela_peso, text="Peso (kg):").pack(pady=5)
    entrada_peso = tk.Entry(janela_peso)
    entrada_peso.pack(pady=5)

    botao_salvar_peso = tk.Button(janela_peso, text="Salvar", command=lambda: salvar_peso(entrada_peso.get()))
    botao_salvar_peso.pack(pady=20)

def salvar_peso(peso):
    conexao = sqlite3.connect("diario_emagrecimento.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO peso (peso) VALUES (?)", (peso,))
    conexao.commit()
    conexao.close()
    messagebox.showinfo("Peso Salvo", "Seu peso foi salvo com sucesso!")

def visualizar_evolucao():
    conexao = sqlite3.connect("diario_emagrecimento.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT data, peso FROM peso")
    registros = cursor.fetchall()
    conexao.close()

    if registros:
        datas = [registro[0] for registro in registros]
        pesos = [registro[1] for registro in registros]
        
        plt.plot(datas, pesos, marker='o')
        plt.title("Evolução do Peso")
        plt.xlabel("Data")
        plt.ylabel("Peso (kg)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        messagebox.showwarning("Evolução", "Nenhum registro de peso encontrado.")

def analisar_humor():
    conexao = sqlite3.connect("diario_emagrecimento.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT sentimentos FROM registros")
    registros = cursor.fetchall()
    conexao.close()

    if registros:
        sentimentos = [registro[0] for registro in registros]
        # Simples análise: contar palavras positivas/negativas
        positivos = sum("feliz" in s for s in sentimentos)
        negativos = sum("triste" in s for s in sentimentos)
        
        resultado = f"Sentimentos positivos: {positivos}, Sentimentos negativos: {negativos}"
        messagebox.showinfo("Análise de Humor", resultado)
    else:
        messagebox.showwarning("Análise de Humor", "Nenhum registro encontrado.")

def definir_objetivo():
    janela_objetivo = tk.Toplevel()
    janela_objetivo.title("Definir Objetivo de Peso")
    janela_objetivo.geometry("300x150")

    tk.Label(janela_objetivo, text="Objetivo de Peso (kg):").pack(pady=5)
    entrada_objetivo = tk.Entry(janela_objetivo)
    entrada_objetivo.pack(pady=5)

    botao_salvar_objetivo = tk.Button(janela_objetivo, text="Salvar", command=lambda: salvar_objetivo(entrada_objetivo.get()))
    botao_salvar_objetivo.pack(pady=20)

def salvar_objetivo(objetivo):
    conexao = sqlite3.connect("diario_emagrecimento.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO objetivos (objetivo) VALUES (?)", (objetivo,))
    conexao.commit()
    conexao.close()
    messagebox.showinfo("Objetivo Salvo", "Seu objetivo foi salvo com sucesso!")

def coletar_feedback():
    janela_feedback = tk.Toplevel()
    janela_feedback.title("Coletar Feedback")
    janela_feedback.geometry("300x250")

    tk.Label(janela_feedback, text="Por favor, deixe seu feedback:", font=("Arial", 12)).pack(pady=10)

    entrada_feedback = tk.Text(janela_feedback, height=5, width=30)
    entrada_feedback.pack(pady=10)

    botao_enviar = tk.Button(janela_feedback, text="Enviar", command=lambda: enviar_feedback(entrada_feedback.get("1.0", tk.END)))
    botao_enviar.pack(pady=10)

def enviar_feedback(feedback):
    if feedback.strip():
        with open("feedback.txt", "a") as f:
            f.write(feedback + "\n")
        messagebox.showinfo("Feedback Enviado", "Seu feedback foi enviado com sucesso!")
    else:
        messagebox.showwarning("Feedback Vazio", "Por favor, insira seu feedback antes de enviar.")

def mostrar_suporte():
    suporte_info = """
    Suporte e Atualizações:

    Para suporte, entre em contato conosco pelo email: suporte@diarioemagrecimento.com
    Verifique sempre se está usando a versão mais recente do aplicativo.
    """
    messagebox.showinfo("Suporte e Atualizações", suporte_info)

if __name__ == "__main__":
    iniciar_app()


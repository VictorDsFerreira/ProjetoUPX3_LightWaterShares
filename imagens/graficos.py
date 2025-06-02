import matplotlib.pyplot as plt # type: ignore

# Gráfico 1 - Consumo Mundial: Renovável vs Fóssil
labels1 = ['Energias Renováveis', 'Energias Fósseis']
sizes1 = [28, 72]  # Dados fictícios representativos
colors1 = ['#00A86B', '#0B2545']

plt.figure(figsize=(6,6))
plt.pie(sizes1, labels=labels1, colors=colors1, autopct='%1.1f%%', startangle=90)
plt.title('Consumo Mundial: Renovável vs Fóssil')
plt.savefig('imagens/grafico1.png')
plt.close()

# Gráfico 2 - Fontes de Energia mais Utilizadas no Brasil
labels2 = ['Hídrica', 'Solar', 'Eólica', 'Biomassa', 'Outras']
sizes2 = [60, 12, 10, 8, 10]
colors2 = ['#3498db', '#f1c40f', '#95a5a6', '#27ae60', '#8e44ad']

plt.figure(figsize=(6,6))
plt.pie(sizes2, labels=labels2, colors=colors2, autopct='%1.1f%%', startangle=90)
plt.title('Fontes de Energia no Brasil')
plt.savefig('imagens/grafico2.png')
plt.close()

# Gráfico 3 - Crescimento da Energia Solar nos Últimos Anos
labels3 = ['2018', '2019', '2020', '2021', '2022', '2023']
sizes3 = [5, 10, 15, 25, 30, 40]  # Crescimento representativo em porcentagem
colors3 = plt.cm.Greens(range(50, 250, 30))

plt.figure(figsize=(6,6))
plt.pie(sizes3, labels=labels3, colors=colors3, autopct='%1.1f%%', startangle=90)
plt.title('Crescimento Energia Solar')
plt.savefig('imagens/grafico3.png')
plt.close()

print('Gráficos gerados com sucesso!')

tecnologias = ['Python', 'JavaScript', 'HTML', 'CSS', 'Git', 'PHP']
tecnologias[2] = 'Kotlin'
tecnologias.append('C#')
tecnologias.sort()
print(f'Por ordem alfabética {tecnologias}')
tecnologias.sort(reverse=True)
print(f'Por ordem de Z a A: {tecnologias}')
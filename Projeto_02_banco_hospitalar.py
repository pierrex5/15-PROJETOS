import sqlite3

# Conectar ao banco de dados (cria automaticamente se não existir)
conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()

print("Criando banco de dados hospitalar...")

# Criar tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS medicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        especialidade TEXT NOT NULL,
        crm TEXT UNIQUE NOT NULL,
        telefone TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_nascimento TEXT,
        cpf TEXT UNIQUE NOT NULL,
        telefone TEXT,
        endereco TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medico_id INTEGER,
        paciente_id INTEGER,
        data_consulta TEXT,
        diagnostico TEXT,
        valor_consulta REAL,
        FOREIGN KEY (medico_id) REFERENCES medicos(id),
        FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
    )
''')

print("Tabelas criadas com sucesso!")

# Inserir médicos
medicos = [
    ('Dr. João Silva', 'Cardiologia', 'CRM/SP 12345', '(11) 9999-1111'),
    ('Dra. Maria Santos', 'Pediatria', 'CRM/SP 67890', '(11) 9999-2222'),
    ('Dr. Carlos Oliveira', 'Ortopedia', 'CRM/SP 54321', '(11) 9999-3333'),
    ('Dra. Ana Costa', 'Dermatologia', 'CRM/SP 98765', '(11) 9999-4444')
]

cursor.executemany('''
    INSERT OR IGNORE INTO medicos (nome, especialidade, crm, telefone)
    VALUES (?, ?, ?, ?)
''', medicos)

# Inserir pacientes
pacientes = [
    ('Pedro Almeida', '1985-03-15', '123.456.789-00', '(11) 8888-1111', 'Rua A, 123 - São Paulo'),
    ('Mariana Lima', '1990-07-22', '987.654.321-00', '(11) 8888-2222', 'Av. B, 456 - São Paulo'),
    ('Lucas Souza', '1978-11-30', '456.123.789-00', '(11) 8888-3333', 'Rua C, 789 - São Paulo'),
    ('Julia Rodrigues', '2000-05-10', '321.654.987-00', '(11) 8888-4444', 'Av. D, 321 - São Paulo')
]

cursor.executemany('''
    INSERT OR IGNORE INTO pacientes (nome, data_nascimento, cpf, telefone, endereco)
    VALUES (?, ?, ?, ?, ?)
''', pacientes)

# Inserir consultas
consultas = [
    (1, 1, '2024-01-15 09:00:00', 'Pressão arterial elevada', 250.00),
    (2, 2, '2024-01-15 10:30:00', 'Check-up infantil', 180.00),
    (3, 3, '2024-01-16 14:00:00', 'Fratura no braço', 300.00),
    (1, 4, '2024-01-17 11:00:00', 'Arritmia cardíaca', 280.00),
    (4, 1, '2024-01-18 16:00:00', 'Dermatite', 200.00),
    (2, 3, '2024-01-19 08:30:00', 'Gripe comum', 150.00)
]

cursor.executemany('''
    INSERT INTO consultas (medico_id, paciente_id, data_consulta, diagnostico, valor_consulta)
    VALUES (?, ?, ?, ?, ?)
''', consultas)

conn.commit()
print("Dados inseridos com sucesso!")

print("\n" + "="*60)
print("CONSULTAS COM JOIN, GROUP BY E WHERE")
print("="*60)

# CONSULTA 1: JOIN - Todas as consultas com dados completos
print("\n1. JOIN - Todas as consultas:")
cursor.execute('''
    SELECT 
        c.data_consulta,
        m.nome as medico,
        m.especialidade,
        p.nome as paciente,
        c.diagnostico,
        c.valor_consulta
    FROM consultas c
    JOIN medicos m ON c.medico_id = m.id
    JOIN pacientes p ON c.paciente_id = p.id
    ORDER BY c.data_consulta
''')

print("Data         | Médico           | Paciente        | Diagnóstico")
print("-" * 70)
for linha in cursor.fetchall():
    print(f"{linha[0][:10]} | {linha[1]:15} | {linha[3]:15} | {linha[4]}")

# CONSULTA 2: WHERE - Consultas de um médico específico
print("\n2. WHERE - Consultas do Dr. João Silva (Cardiologia):")
cursor.execute('''
    SELECT 
        p.nome as paciente,
        c.data_consulta,
        c.diagnostico,
        c.valor_consulta
    FROM consultas c
    JOIN pacientes p ON c.paciente_id = p.id
    WHERE c.medico_id = 1
    ORDER BY c.data_consulta
''')

for linha in cursor.fetchall():
    print(f"  {linha[0]} - {linha[1][:10]} - R$ {linha[3]} - {linha[2]}")

# CONSULTA 3: GROUP BY - Total de consultas por médico
print("\n3. GROUP BY - Consultas por médico:")
cursor.execute('''
    SELECT 
        m.nome as medico,
        m.especialidade,
        COUNT(c.id) as total_consultas,
        SUM(c.valor_consulta) as faturamento_total
    FROM medicos m
    LEFT JOIN consultas c ON m.id = c.medico_id
    GROUP BY m.id, m.nome, m.especialidade
    ORDER BY total_consultas DESC
''')

print("Médico              | Especialidade | Consultas | Faturamento")
print("-" * 65)
for linha in cursor.fetchall():
    print(f"{linha[0]:18} | {linha[1]:12} | {linha[2]:9} | R$ {linha[3]:.2f}")

# CONSULTA 4: WHERE + GROUP BY - Consultas com valor acima de R$ 200
print("\n4. WHERE + GROUP BY - Faturamento por especialidade (acima de R$ 200):")
cursor.execute('''
    SELECT 
        m.especialidade,
        COUNT(c.id) as total_consultas,
        SUM(c.valor_consulta) as faturamento_total
    FROM medicos m
    JOIN consultas c ON m.id = c.medico_id
    WHERE c.valor_consulta > 200
    GROUP BY m.especialidade
    ORDER BY faturamento_total DESC
''')

for linha in cursor.fetchall():
    print(f"  {linha[0]}: {linha[1]} consultas - R$ {linha[2]:.2f}")

# CONSULTA 5: GROUP BY - Pacientes e quantas consultas fizeram
print("\n5. GROUP BY - Consultas por paciente:")
cursor.execute('''
    SELECT 
        p.nome as paciente,
        COUNT(c.id) as total_consultas,
        SUM(c.valor_consulta) as total_gasto
    FROM pacientes p
    LEFT JOIN consultas c ON p.id = c.paciente_id
    GROUP BY p.id, p.nome
    HAVING total_consultas > 0
    ORDER BY total_consultas DESC
''')

for linha in cursor.fetchall():
    print(f"  {linha[0]}: {linha[1]} consultas - R$ {linha[2]:.2f}")

# CONSULTA 6: WHERE + JOIN - Pacientes com mais de 30 anos
print("\n6. WHERE - Pacientes com mais de 30 anos:")
cursor.execute('''
    SELECT 
        nome,
        data_nascimento,
        telefone
    FROM pacientes
    WHERE CAST(strftime('%Y', 'now') AS INTEGER) - CAST(strftime('%Y', data_nascimento) AS INTEGER) > 30
    ORDER BY data_nascimento
''')

for linha in cursor.fetchall():
    idade = 2024 - int(linha[1][:4])  # cálculo simplificado da idade
    print(f"  {linha[0]} - {idade} anos - {linha[2]}")

# CONSULTA 7: GROUP BY + HAVING - Especialidades com mais de 1 consulta
print("\n7. GROUP BY + HAVING - Especialidades com alta demanda:")
cursor.execute('''
    SELECT 
        m.especialidade,
        COUNT(c.id) as total_consultas,
        AVG(c.valor_consulta) as valor_medio
    FROM medicos m
    JOIN consultas c ON m.id = c.medico_id
    GROUP BY m.especialidade
    HAVING total_consultas >= 2
    ORDER BY total_consultas DESC
''')

for linha in cursor.fetchall():
    print(f"  {linha[0]}: {linha[1]} consultas - R$ {linha[2]:.2f} em média")

# Fechar conexão
conn.close()
print("\n" + "="*60)
print("Banco de dados fechado. Arquivo: hospital.db")
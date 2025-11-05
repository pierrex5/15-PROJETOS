from flask import Flask, jsonify, request

app = Flask(__name__)

# Banco de dados em memória (lista de dicionários)
tarefas = []
contador_id = 1


@app.route('/')
def home():
    return jsonify({"mensagem": "✅ API ToDo Flask está rodando!"})


# === [CREATE] Criar nova tarefa ===
@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    global contador_id

    dados = request.get_json()
    if not dados or "titulo" not in dados:
        return jsonify({"erro": "Campo 'titulo' é obrigatório!"}), 400

    nova_tarefa = {
        "id": contador_id,
        "titulo": dados["titulo"],
        "descricao": dados.get("descricao", ""),
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    contador_id += 1

    return jsonify(nova_tarefa), 201


# === [READ] Listar todas as tarefas ===
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas), 200


# === [READ] Obter tarefa específica ===
@app.route('/tarefas/<int:id_tarefa>', methods=['GET'])
def obter_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada!"}), 404


# === [UPDATE] Atualizar tarefa ===
@app.route('/tarefas/<int:id_tarefa>', methods=['PUT'])
def atualizar_tarefa(id_tarefa):
    dados = request.get_json()

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["titulo"] = dados.get("titulo", tarefa["titulo"])
            tarefa["descricao"] = dados.get("descricao", tarefa["descricao"])
            tarefa["concluida"] = dados.get("concluida", tarefa["concluida"])
            return jsonify(tarefa)

    return jsonify({"erro": "Tarefa não encontrada!"}), 404


# === [DELETE] Excluir tarefa ===
@app.route('/tarefas/<int:id_tarefa>', methods=['DELETE'])
def deletar_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefas.remove(tarefa)
            return jsonify({"mensagem": f"Tarefa {id_tarefa} removida com sucesso!"})
    return jsonify({"erro": "Tarefa não encontrada!"}), 404


if __name__ == '__main__':
    app.run(debug=True)
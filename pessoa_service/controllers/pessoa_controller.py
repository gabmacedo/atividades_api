from flask import Blueprint, jsonify, request
from database.db import get_connection

pessoa_bp = Blueprint("pessoa_bp", __name__)

@pessoa_bp.route("/pessoas/professores", methods=["GET"])
def get_professores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, materia FROM professores")
    rows = cursor.fetchall()
    conn.close()

    professores = []
    for row in rows:
        professores.append({
            "id": row[0],
            "nome": row[1],
            "materia": row[2]
        })

    return jsonify(professores), 200

@pessoa_bp.route("/pessoas/professores/<int:professor_id>", methods=["GET"])
def get_professor_id(professor_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM professores WHERE id = ?", (professor_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify({
            "id": row[0],
            "nome": row[1],
            "disciplina": row[2]
        }), 200
    else:
        return jsonify({"erro": "Professor não encontrado"}), 404

@pessoa_bp.route("/pessoas/professores", methods=["POST"])
def create_professor():
    data = request.get_json()
    nome = data.get("nome")
    materia = data.get("materia")

    if not nome or not materia:
        return jsonify({"erro": "Campos 'nome' e 'materia' são obrigatórios."}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO professores (nome, materia) VALUES (?, ?)", (nome, materia))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Professor criado com sucesso"}), 201

@pessoa_bp.route("/pessoas/professores/<int:professor_id>", methods=["DELETE"])
def delete_professor(professor_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM professores WHERE id = ?", (professor_id,))
    professor = cursor.fetchone()

    if not professor:
        conn.close()
        return jsonify({"erro": "Professor não encontrado"}), 404

    cursor.execute("DELETE FROM professores WHERE id = ?", (professor_id,))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": f"Professor com ID {professor_id} foi removido com sucesso"}), 200
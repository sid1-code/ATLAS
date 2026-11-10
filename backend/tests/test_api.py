def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_conversation_and_chat_flow(client):
    conversation = client.post("/api/v1/conversations", json={"user_id": 1, "title": "First chat"})
    assert conversation.status_code == 201
    conversation_id = conversation.json()["id"]

    reply = client.post(
        "/api/v1/chat",
        json={"conversation_id": conversation_id, "user_id": 1, "message": "Hello ATLAS"},
    )
    assert reply.status_code == 200
    assert reply.json()["conversation_id"] == conversation_id
    assert "Hello ATLAS" in reply.json()["message"]

    detail = client.get(f"/api/v1/conversations/{conversation_id}")
    assert detail.status_code == 200
    assert [message["role"] for message in detail.json()["messages"]] == ["user", "assistant"]



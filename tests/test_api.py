from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "AI Research Agent API is running"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_research_validation():
    response = client.post("/research", json={})
    assert response.status_code == 422


def test_research(monkeypatch):
    def mock_graph_invoke(state):
        return {
            "topic": state["topic"],
            "status": "test_success"
        }

    monkeypatch.setattr("api.main.graph.invoke", mock_graph_invoke)

    response = client.post(
        "/research",
        json={"topic": "Artificial Intelligence"}
    )

    assert response.status_code == 200
    assert response.json()["topic"] == "Artificial Intelligence"
    assert response.json()["status"] == "test_success"

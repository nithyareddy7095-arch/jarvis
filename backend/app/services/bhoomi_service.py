from app.schemas.chat import ChatRequest, ChatResponse


class BhoomiService:
    """LLM wrapper with deterministic fallback for local/dev environments."""

    async def ask(self, payload: ChatRequest) -> ChatResponse:
        prompt = payload.question.lower()
        tips = [
            "Use soil testing every season for better nutrient planning.",
            "Prefer drip irrigation for water efficiency.",
        ]
        if "tomato" in prompt:
            answer = "Tomatoes prefer warm weather, loamy soil, and regular pruning. Start with disease-resistant seedlings."
        elif "sandy" in prompt:
            answer = "For sandy soil, try groundnut, watermelon, and millets with compost and mulching to retain moisture."
        elif "pest" in prompt or "organic" in prompt:
            answer = "Use neem oil spray, pheromone traps, and companion planting for organic pest control."
        else:
            answer = "I recommend starting with climate-suitable crops, healthy seedlings, and weekly field scouting."

        return ChatResponse(answer=answer, tips=tips, stage="Plant")

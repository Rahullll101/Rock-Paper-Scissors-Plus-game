from tools import validate_move, resolve_round
from state import GameState


class GameAgent:
    def explain_rules(self):
        return (
            "Rock–Paper–Scissors–Plus rules:\n"
            "• Best of 3 rounds\n"
            "• Moves: rock, paper, scissors, bomb\n"
            "• Bomb beats all but usable once\n"
            "• Invalid input wastes the round"
        )

    def process_turn(self, user_input: str, state: GameState):
        current_round = state.round_number
        validation = validate_move(user_input, state.user_bomb_used)

        # Invalid input → round wasted
        if not validation["valid"]:
            state.round_number += 1
            response = (
                f"Round {current_round}\n"
                f"{validation['reason']}\n"
                f"Score → You: {state.user_score}, Bot: {state.bot_score}"
            )
            return response, state

        # Valid input → resolve round via tool
        result = resolve_round(validation["move"], state)

        response = (
            f"Round {current_round}\n"
            f"You played: {validation['move']}\n"
            f"Bot played: {result['bot_move']}\n"
            f"Round winner: {result['winner']}\n"
            f"Score → You: {state.user_score}, Bot: {state.bot_score}"
        )

        return response, state

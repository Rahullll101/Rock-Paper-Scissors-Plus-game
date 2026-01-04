# ADK agent
from tools import validate_move, resolve_round

class GameAgent:

    def explain_rules(self):
        return (
            "Rock–Paper–Scissors–Plus rules:\n"
            "• Best of 3 rounds\n"
            "• Moves: rock, paper, scissors, bomb\n"
            "• Bomb beats all but usable once\n"
            "• Invalid input wastes the round"
        )

    def process_turn(self, user_input, state):
        validation = validate_move(user_input, state.user_bomb_used)

        if not validation["valid"]:
            state.round_number += 1
            return validation["reason"], state

        result = resolve_round(validation["move"], state)

        response = (
            f"Round {state.round_number - 1}\n"
            f"You played: {validation['move']}\n"
            f"Bot played: {result['bot_move']}\n"
            f"Winner: {result['winner']}\n"
            f"Score → You: {state.user_score}, Bot: {state.bot_score}"
        )

        return response, state

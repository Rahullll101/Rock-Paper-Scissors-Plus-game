# ADK tools (logic + mutation)
import random

VALID_MOVES = {"rock", "paper", "scissors", "bomb"}

def validate_move(move: str, bomb_used: bool):
    move = move.lower().strip()

    if move not in VALID_MOVES:
        return {
            "valid": False,
            "reason": "Invalid move. Round wasted."
        }

    if move == "bomb" and bomb_used:
        return {
            "valid": False,
            "reason": "Bomb already used. Round wasted."
        }

    return {
        "valid": True,
        "move": move
    }

# import random

def resolve_round(user_move, state):
    bot_moves = ["rock", "paper", "scissors"]
    if not state.bot_bomb_used:
        bot_moves.append("bomb")

    bot_move = random.choice(bot_moves)

    # Track bomb usage
    if user_move == "bomb":
        state.user_bomb_used = True
    if bot_move == "bomb":
        state.bot_bomb_used = True

    # Determine winner
    winner = "draw"

    if user_move == bot_move:
        winner = "draw"
    elif user_move == "bomb" and bot_move != "bomb":
        winner = "user"
        state.user_score += 1
    elif bot_move == "bomb" and user_move != "bomb":
        winner = "bot"
        state.bot_score += 1
    elif (
        (user_move == "rock" and bot_move == "scissors") or
        (user_move == "scissors" and bot_move == "paper") or
        (user_move == "paper" and bot_move == "rock")
    ):
        winner = "user"
        state.user_score += 1
    else:
        winner = "bot"
        state.bot_score += 1

    state.round_number += 1

    return {
        "bot_move": bot_move,
        "winner": winner,
        "state": state
    }

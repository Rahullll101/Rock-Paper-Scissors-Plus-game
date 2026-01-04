import random

VALID_MOVES = {"rock", "paper", "scissors", "bomb"}

COMMON_MISTAKES = {
    "scissor": "scissors",
    "papers": "paper",
    "rocks": "rock"
}


def validate_move(move: str, bomb_used: bool) -> dict:
    """Validate user move and bomb usage."""
    if not move:
        return {"valid": False, "reason": "No move provided. Round wasted."}

    move = move.lower().strip()

    # Fix common spelling mistakes (safe normalization)
    if move in COMMON_MISTAKES:
        move = COMMON_MISTAKES[move]

    if move not in VALID_MOVES:
        return {"valid": False, "reason": "Invalid move. Round wasted."}

    if move == "bomb" and bomb_used:
        return {"valid": False, "reason": "Bomb already used. Round wasted."}

    return {"valid": True, "move": move}


def resolve_round(user_move: str, state) -> dict:
    """Resolve one round and mutate game state."""
    bot_moves = ["rock", "paper", "scissors"]
    if not state.bot_bomb_used:
        bot_moves.append("bomb")

    bot_move = random.choice(bot_moves)

    # Track bomb usage
    if user_move == "bomb":
        state.user_bomb_used = True
    if bot_move == "bomb":
        state.bot_bomb_used = True

    winner = "draw"

    if user_move == bot_move:
        pass
    elif user_move == "bomb":
        winner = "user"
        state.user_score += 1
    elif bot_move == "bomb":
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
        "winner": winner
    }

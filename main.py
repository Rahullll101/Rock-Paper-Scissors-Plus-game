# conversation loop
from state import GameState
from game_agent import GameAgent


def main():
    agent = GameAgent()
    state = GameState()

    print("\n=== Welcome to Rock–Paper–Scissors–Plus ===\n")
    print(agent.explain_rules())

    # Game loop (max 3 rounds)
    while state.round_number <= state.max_rounds:
        user_input = input("\nEnter your move: ")
        response, state = agent.process_turn(user_input, state)
        print(response)

    # Game over
    print("\n=== GAME OVER ===")

    if state.user_score > state.bot_score:
        print("🏆 Final Result: You win!")
    elif state.bot_score > state.user_score:
        print("🤖 Final Result: Bot wins!")
    else:
        print("🤝 Final Result: It's a draw!")


if __name__ == "__main__":
    main()


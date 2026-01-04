# conversation loop
from state import GameState
from agent import GameAgent

def main():
    agent = GameAgent()
    state = GameState()

    print(agent.explain_rules())

    while state.round_number <= state.max_rounds:
        user_input = input("\nEnter your move: ")
        response, state = agent.process_turn(user_input, state)
        print(response)

    print("\n=== GAME OVER ===")
    if state.user_score > state.bot_score:
        print("🏆 You win!")
    elif state.bot_score > state.user_score:
        print("🤖 Bot wins!")
    else:
        print("🤝 It's a draw!")

if __name__ == "__main__":
    main()

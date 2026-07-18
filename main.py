"def near game():"
'secret number' =random.randit(1,100)
attempts=0
max_attenpts=10

print("===========================")
print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    print(f"Can you guess it within {max_attempts} attempts?")
    print("=========================================\n")
    print("Welcome to the Number Guessing Game!")
        print("I am thinking of a number between 1 and 100.")
        print(f"Can you guess it within {max_attempts} attempts?")
        print("=========================================\n")
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
                except ValueError:
                    print("❌ Invalid input! Please enter a whole number.\n")
                    continue

                attempts += 1
                if guess < secret_number:
                            print("📈 Too low! Try a higher number.\n")
                        elif guess > secret_number:
                            print("📉 Too high! Try a lower number.\n")
                        else:
                            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
                            return
                            print(f"😢 Game over! You've run out of turns. The correct number was {secret_number}.")
                            if __name__ == "__main__":
                                play_game()

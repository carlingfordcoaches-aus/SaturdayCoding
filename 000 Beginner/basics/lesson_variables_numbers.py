"""Variables & Numbers

Focus: Manage integers and floats to track classroom progress."""

def exercise_1():
    done = int(input("How many lessons out of 10 have you completed? "))
    percent = (done/10) * 100
    print(f"Progress: {done}/10 ({percent}%)")
    """Track completed and remaining lessons, then print a friendly progress bar."""
    # TODO: Track completed and remaining lessons, then print a friendly progress bar
    pass

def exercise_2():
    min = int(input('how long did you study for in min: '))
    hour = (min/60)
    print(f"Time: {min} minutes = {hour} hours ")
    """Convert study minutes to hours with a formatted sentence."""
    # TODO: Convert study minutes to hours with a formatted sentence.
    pass


def main():
    """Uncomment the exercises you want to run."""
    # exercise_1()
    exercise_2()
    pass

if __name__ == '__main__':
    main()

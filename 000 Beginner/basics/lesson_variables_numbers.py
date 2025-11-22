"""Variables & Numbers

Focus: Manage integers and floats to track classroom progress."""

def exercise_1():
    done = int(input("how many lessons out of 10 have you done? "))
    w = done*10
    print(f"progress: {done}/10 ({w}%)") 
    
    
    """Track completed and remaining lessons, then print a friendly progress bar."""
    # TODO: Track completed and remaining lessons, then print a friendly progress bar.2
    pass


def exercise_2():
    study=int(input("how long have you studyed for in minutes ?"))
    three=study/60 
    print(f"study time: {study} minutes = {three} hours")
    """Convert study minutes to hours with a formatted sentence."""
    # TODO: Convert study minutes to hours with a formatted sentence.
    pass


def main():
    """Uncomment the exercises you want to run."""
    exercise_1()
    exercise_2()
    pass

if __name__ == '__main__':
    main()

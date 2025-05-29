def main_welcome(func):
    def child_welcome():
        print("The Great Hitesh Solanki")
        func()
        print("The Great Great Great Hitesh Solanki")
    return child_welcome()

@main_welcome
def print_welcome():
    print("The Great Great Hitesh Solanki")

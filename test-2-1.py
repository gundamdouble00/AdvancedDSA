from core.base import Base


class Test(Base):

    def initialize(self):
        print("Initializing program...")

    def update(self):
        pass


def main():
    # instantiate this class and run the program
    Test().run()


if __name__ == "__main__":
    main()

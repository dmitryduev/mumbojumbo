import time

import wandb


def main():
    run = wandb.init(
        entity="dimaduev",
        project="lunch",
    )
    run.finish()


if __name__ == "__main__":
    main()

import time

import wandb


def main():
    run = wandb.init(
        entity="dimaduev",
        project="lunch",
    )
    run.config["a"] = 1
    assert run.config["a"] == 1
    run.finish()


if __name__ == "__main__":
    main()

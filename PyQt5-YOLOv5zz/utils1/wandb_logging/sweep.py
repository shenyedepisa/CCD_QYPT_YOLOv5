import sys
from pathlib import Path

import wandb

FILE = Path(__file__).absolute()
sys.path.append(FILE.parents[2].as_posix())  # add utils1/ to path

from train import train, parse_opt
from utils1.general import increment_path
from utils1.torch_utils import select_device


def sweep():
    wandb.init()
    # Get hyp dict from sweep agent
    hyp_dict = vars(wandb.config).get("_items")

    # Workaround: get necessary opt args
    opt = parse_opt(known=True)
    opt.batch_size = hyp_dict.get("batch_size")
    opt.save_dir = str(increment_path(Path(opt.project) / opt.name, exist_ok=opt.exist_ok or opt.evolve))
    opt.epochs = hyp_dict.get("epochs")
    opt.nosave = True
    opt.data = hyp_dict.get("data")
    device = select_device(opt.device, batch_size=opt.batch_size)

    # train
    train(hyp_dict, opt, device)


if __name__ == "__main__":
    sweep()

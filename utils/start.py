# =========================================================================== #
# 
# =========================================================================== #

# 参数设定
import argparse
parser = argparse.ArgumentParser(description="AI Auto Runner")
parser.add_argument("--epoch_max", type=int, default=2000,
                    help="Set the maximum of training epoch")
parser.add_argument("--epoch_stop", type=int, default=200,
                    help="Set the early stop of training epoch")
parser.add_argument("--batch_size", type=int, default=4,
                    help="Set batch size")
parser.add_argument("--classes", type=int, default=4,
                    help="Set classes")
parser.add_argument("--dataset", type=str, default="TwT",
                    help="Set dataset name")
parser.add_argument("--device", type=str, default="cuda:0",
                    help="Set device")
parser.add_argument("--device_ids", type=int, default=[0,1], nargs="+",
                    help="Set device indexes")
parser.add_argument("--depths", type=int, default=[4,4,4,4], nargs="+",
                    help="Set depths")
parser.add_argument("--dim", type=int, default=32,
                    help="Set embedding dims")
parser.add_argument("--figure_size", type=int, default=256,
                    help="Set figure size")
parser.add_argument("--in_channels", type=int, default=1,
                    help="Set input channel number")
parser.add_argument("--learning_rate", type=float, default=0.001,
                    help="Set learning rate")
parser.add_argument("--loss_function", type=str, default="Lovasz_Multical",
                    choices=["Lovasz_Multical","Logit_Adjustment",
                             "Dice","Weight_Dice","Generalized_Dice"],
                    help="Set loss function")
parser.add_argument("--model", type=str, default="Unet",
                    choices=["Unet", "ST-Unet", "ACC-Unet"],
                    help="Choose the model name: Unet, ST-Unet, ACC-Unet")
parser.add_argument("--num_gpu", type=int, default=1,
                    help="Set the number of gpus to be used")
parser.add_argument("--num_heads", type=int, default=[2,4,8,16], nargs="+",
                    help="Set the number of heads")
parser.add_argument("--seed", type=int, default=42,
                    help="Set training seed")
parser.add_argument("--wandb", type=str, default="CHOL-Classifier",
                    choices=["CHOL-Classifier","Loss_Function_Test"],
                    help="Set wandb space name")
args = parser.parse_args()

# 
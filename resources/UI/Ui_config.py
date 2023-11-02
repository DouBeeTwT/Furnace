########################
### Information Page ###
########################

# QComBox AddItems
Nodes_Items = ["ALL", "GPU01", "GPU02", "GPU03", "GPU04", "GPU05", "GPU06"]


####################
### Trainer Page ###
####################

# QComBox AddItems

MaxEpoch_Items = ["100", "500", "1000", "2000", "5000"]
EarlyStop_Items = ["200", "500"]
BatchSize_Items = ["1", "2", "4", "8", "16", "32", "64"]
LearningRate_Items = ["0.001", "0.003", "0.01", "0.03", "0.1"]
CudaDevice_Items = ["0", "1"]
Model_Items = ["Unet", "ST-Unet", "ACC-Unet"]
LossFunction_Items = ["MDR", "Lov-Multi", "ACC-Unet"]
DimChannels_Items = ["16", "32", "64"]
OutputChannels_Items = ["1", "4", "6", "100"]
InputChannels_Items = ["1", "3"]
FigureSize_Items = ["128", "256", "512", "1024"]
TransDepth_Items = ["[4,4,4,4]", "[4,8,8,4]", "[8,8,8,8]"]
TransHead_Items = ["[4,4,4,4]", "[2,4,8,16]", "[4,8,8,16]"]

"""
from resources.UI.Ui_config import *

self.MaxEpochBox.addItems(MaxEpoch_Items)
self.EarlyStopBox.addItems(EarlyStop_Items)
self.BatchSizeBox.addItems(BatchSize_Items)
self.LearningRateBox.addItems(LearningRate_Items)
self.CudaDeviceBox.addItems(CudaDevice_Items)
self.ModelBox.addItems(Model_Items)
self.LossFunctionBox.addItems(LossFunction_Items)
self.DimChannelsBox.addItems(DimChannels_Items)
self.OutputChannelsBox.addItems(OutputChannels_Items)
self.InputChannelsBox.addItems(InputChannels_Items)
self.FigureSizeBox.addItems(FigureSize_Items)
self.TransDepthBox.addItems(TransDepth_Items)
self.TransHeadBox.addItems(TransHead_Items)
"""
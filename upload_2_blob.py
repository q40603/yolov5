
import numpy as np
import os
from azureml.core import Workspace, Datastore, Experiment
from azureml.core.compute import AmlCompute, ComputeTarget
from azureml.core.runconfig import MpiConfiguration
import os
import sys
import argparse



ws = Workspace.from_config()
print('Workspace name: ' + ws.name, 
      'Azure region: ' + ws.location, 
      'Subscription id: ' + ws.subscription_id, 
      'Resource group: ' + ws.resource_group, sep='\n')


datastore = ws.get_default_datastore()
datastore.upload(
    src_dir = "E:Waymo\\1_Training_done_extracted_1\\training_0001",
    target_path = "./waymo/train",
    overwrite = True,
    show_progress = True
)


datastore.upload(
    src_dir = "E:Waymo\\1_Training_done_extracted_1\\training_0002",
    target_path = "./waymo/val",
    overwrite = True,
    show_progress = True
)
This repository consists of all the code developed and/or used as part of the course F21MP. The purpose of this code is to evaluate Simulated to Real Domain Adaptation for Lane Detection.
The GitHub link to this repo is https://github.com/bushra021897/synth2realanalysis

## Dataset Preparation
Create new folders TuSimple and Simulanes
Download training and test set for TuSimple Dataset from https://github.com/TuSimple/tusimple-benchmark/issues/3 and place it in TuSimple folder. 
Download the Simulation dataset from https://drive.google.com/drive/folders/19kydbyO17dtieTar_5AS0hnXHDMHE4lk and place it in Simulanes folder.

Run ```python3 transform_wato.py```. The dataset is ready to be trained.

## Experimental Setup
This repository assumes that you have a GPU and Anaconda3 is installed. Create two separate Anaconda3 environments for PINet and UFLD. 
### PINet
```
cd PINet_New/TuSimple/
pip3 install -r requirements.txt
```
Install PyTorch for your system from https://pytorch.org/

### UFLD
```
cd Ultra-Fast-Lane-Detection/TuSimple/
pip3 install -r requirements.txt
```

## Training
### PINet
```cd PINet_New/TuSimple/```
In parameters.py, change the split_perc to a value between 0 and 1. This will be the ratio for the real dataset. 1 - split_perc will be taken as the ratio for the simulation dataset.
Change the save_path to the path where the models should be saved. 
Change train_root_url and test_root_url to the path where your dataset is saved.

Follow steps on https://github.com/koyeongmin/PINet_new for detailed instructions.

```
python3 fix_dataset_split.py
python3 -m visdom.server
python3 train.py
```

For evaluation,
``` python3 evaluation.py```

### UFLD
```cd Ultra-Fast-Lane-Detection/TuSimple/```
In scripts/convert_tusimple.py, change the split_perc to a value between 0 and 1. This will be the ratio for the real dataset. 1 - split_perc will be taken as the ratio for the simulation dataset.
Change the train_root and test root to the path where your dataset is saved. 
In configs/tusimple.py, change the data root to the path where your dataset is saved. 
Change the log_path to where the logs should be saved. These logs can be viewed using tensorboard.

Follow steps on https://github.com/cfzd/Ultra-Fast-Lane-Detection for detailed instructions.

```
python3 scripts/convert_tusimple.py
python3 train.py
```

For evaluation,
```
python test.py configs/tusimple.py --test_model model_path --test_work_dir save_path
```


## References
```
@misc{hu2022simtoreal,
      title={Sim-to-Real Domain Adaptation for Lane Detection and Classification in Autonomous Driving}, 
      author={Chuqing Hu and Sinclair Hudson and Martin Ethier and Mohammad Al-Sharman and Derek Rayside and William Melek},
      year={2022},
      eprint={2202.07133},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@article{DBLP:journals/corr/abs-2004-11757,
  author    = {Zequn Qin and
               Huanyu Wang and
               Xi Li},
  title     = {Ultra Fast Structure-aware Deep Lane Detection},
  journal   = {CoRR},
  volume    = {abs/2004.11757},
  year      = {2020},
  url       = {https://arxiv.org/abs/2004.11757},
  eprinttype = {arXiv},
  eprint    = {2004.11757},
  timestamp = {Tue, 19 Jul 2022 15:32:45 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2004-11757.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}

@article{DBLP:journals/corr/abs-2002-06604,
  author    = {YeongMin Ko and
               Jiwon Jun and
               Donghwuy Ko and
               Moongu Jeon},
  title     = {Key Points Estimation and Point Instance Segmentation Approach for
               Lane Detection},
  journal   = {CoRR},
  volume    = {abs/2002.06604},
  year      = {2020},
  url       = {https://arxiv.org/abs/2002.06604},
  eprinttype = {arXiv},
  eprint    = {2002.06604},
  timestamp = {Mon, 02 Mar 2020 16:46:06 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2002-06604.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}```


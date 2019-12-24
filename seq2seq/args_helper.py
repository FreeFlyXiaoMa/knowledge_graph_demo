# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/23 10:19 上午
# @Author: wuchenglong





import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--task", type=str, default="predict", help="epoch")
parser.add_argument("--epoch", type=int, default=0, help="epoch")
parser.add_argument("--vocab_file", type=str, default="data/vocab.txt", help="vocab_file")
parser.add_argument("--size_layer", type=int, default=256, help="size_layer")
parser.add_argument("--num_layers", type=int, default=2, help="num_layers")
parser.add_argument("--embedded_size", type=int, default=128, help="num_layers")
parser.add_argument("--learning_rate", type=float, default=0.001, help="learning_rate")
parser.add_argument("--batch_size", type=int, default=16, help="batch_size")
parser.add_argument("--checkpoint_dir", type=str, default="result", help="checkpoint_dir")
args = parser.parse_args()

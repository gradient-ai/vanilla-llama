import gradio as gr
from typing import Tuple
import os
import sys
import torch
import time
import json
import argparse
import subprocess
from pathlib import Path
from inference import LLaMAInference

from datetime import datetime
from llama import ModelArgs, Transformer, Tokenizer, LLaMA
import torch

llama_path = 'models'
llama = LLaMAInference(llama_path, "7B")


def seedTorch(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
import string
nonprint = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
def run(prompts, seed):
    seedTorch(seed)
    return llama.generate([f'{prompts}'])

def remove_non_printable(s):
    lst = []
    for i in s:
        if i in nonprint:
            lst.append(i)
    return "".join(lst)

with gr.Blocks(css="#margin-top {margin-top: 15px} #center {text-align: center;} #description {text-align: center}") as demo:
    with gr.Row(elem_id="center"):
        gr.Markdown("# LLaMa Inference with Gradient")
    with gr.Row(elem_id = 'description'):
        gr.Markdown(""" To run LLaMA, be sure to select a model size that works for your machine. Single GPUs should always use '7B'.\n Start typing below and then click **Run to generate text** to see the output.""")
    with gr.Row():
        ckpt = gr.Radio(["7B"], label="Checkpoint directory", value = "7B", interactive = False)
        seed = gr.Slider(label = 'Seed', value = 8019, minimum = 1, maximum = 10000, step =1, interactive = True)
        prompts = gr.Textbox(label = 'Prompt input', placeholder="What is your prompt?", value = 'my new invention is the', interactive = True)
        
    btn = gr.Button("Run to generate text")
    with gr.Row():
        out = gr.Markdown()
    with gr.Row():
        gr.Image('assets/logo.png').style(height = 53, width = 125, interactive = False)

    btn.click(fn=run, inputs=[prompts, seed, ckpt], outputs=out)


demo.launch(share = True)


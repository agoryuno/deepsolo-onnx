# DeepSolo-ONNX

This is a slimmed down version of the code for the scene text recognition
model DeepSolo. See the original codebase here: https://github.com/ViTAE-Transformer/DeepSolo

DeepSolo-ONNX is a simple way to export a checkpoint of the DeepSolo model to ONNX for
inference on any of the supported platforms.

## Installing

There is no need to install DeepSolo-ONNX or any of its dependencies locally, see the
next section for what you should do instead.

## Using

You can use this [Google Colab notebook](https://colab.research.google.com/drive/1oANvLQekE_6Equ_ld5W4lTR0Kpav09_Q?usp=sharing) to convert a checkpoint of your choosing
to ONNX in 4 easy steps.

## Original checkpoint

You will need to supply the original model's checkpoint for conversion. You can get these
at the main DeepSolo repository: https://github.com/ViTAE-Transformer/DeepSolo

I save my checkpoints in Google Drive for easy and repeatable access from Colab. But simply uploading to the instance's `/content` folder also works fine.

## Output format

TBD
 
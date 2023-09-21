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

## Custom character maps

This is only relevant for models trained for different character sets.

If you are trying to convert a model you've trained yourself for some language other than English, which is supported by default by the base model, you'll need to adjust the vocabulary settings.

### Create an alphabet

You'll need to create a file named "lang-chars-#.txt" in directory './char-dicts' where "lang" is the name of the language and "#" is the total number of characters in the language's alphabet. The file should contain a literal string, comprised of the langauge's characters. 

You can refer to the files 'heb-chars-29.txt' and 'heb-chars-71.txt' for examples of such files.

Once the text file with the alphabet is ready, run the `make_dicts.py` script in the projects root:

`python make_dicts.py`

This will rebuild all alphabet files and create corresponding '.cmap' files, which are simply pickled lists of characters.

### Adjust `VOC_SIZE`

You will also need to adjust the `MODEL.TRANSFORMER.VOC_SIZE` setting. 

The best way to do that is to create a new config file, by copying the file 
'./configs/Base_det_export.yaml' under a descriptive name and adding a line in the 
`MODEL.TRANSFORMER` block (between the lines 11 and 33):

```
VOC_SIZE = 37
```

setting it to whatever number of characters is in your language's alphabet.

### Add the alphabet file to config

TBD

### Specify the new config

Replace the base config in the Google Colab notebook with your version (uploading the
new config or saving it to Drive). 

Done.

## Output format

TBD

## Running inference

TBD
 
# Installing

**NOTE:** Meta's detectron2 has to be built from source. 

## Installing in Google Colab

```
!git clone https://github.com/agoryuno/deepsolo-onnx

import os
os.chdir('deepsolo-onnx')

!pip install -r requirements.txt
!pip install git+https://github.com/agoryuno/deepsolo-onnx
```
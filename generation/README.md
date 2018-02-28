Once a fingerprint image is generated with the Anguli software, the corresponding ground-truth and degraded fingerprint images can be obtained with the provided scripts as follwed:

```
from glob import glob
from helpers import generate

background = glob('background/*.jpg')
fingerprint = '1.jpg'

ground_truth, input = generate(background, fingerprint)
```

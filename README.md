# AudioClassifier

Software under construction ...




## 4 Main programs:
### 1. slice.py
Convert audio mp3 to png images of a chopped spectrogram.

### 2. train.py
### 3. test.py
### 4. classify.py

---
## Lib directory
Where all the important functions for data processing would be:
### audio2image.py
##### convert_to_spectrogram
Take mp3 files directory and using __sox__ convert them into spectrogram maps.

##### convert_to_slices
Take a spectrogram files directory and chop it on a desired pixel size.
# AI Attendance System

An AI-powered attendance system using YOLOv5 for face detection and recognition. This project is designed to automate attendance tracking efficiently with high accuracy.

---

## How to Run the Project

### 1. Install Python
Ensure Python 3.10.* is installed on your system. You can download it from [python.org](https://www.python.org/).

### 2. Install Dependencies
Install the required libraries using the provided `requirements.txt`:
```bash
pip install -r requirements.txt
``` 

### 3. Prepare the Dataset

Organize your dataset in the `dataset/` folder with the following structure:
```bash
dataset/
├── images/          # Extract all images here
├── labels/          # Already prepared
├── test/            # Optional test data
└── data.yaml        # Configuration file for YOLOv5
``` 

### 4. Testing the Model

**Model Location**:  
The model is pre-trained and located in `runs/train/exp15/weights/`:
- `best.pt`: The best weights achieved during training (optimal performance on validation data).
- `last.pt`: The weights from the last training epoch (useful for continued training or testing).

#### For Live Video Feed (e.g., webcam):
Run the following command to use the webcam as the input source:
```bash
python detect.py --weights runs/train/exp15/weights/last.pt --img 640 --source 0
``` 
- `--source 0`: Indicates live video feed from your webcam.

#### For Specific Images:
To test the model on a folder of images, run the following command:
```bash
python detect.py --weights runs/train/exp15/weights/last.pt --img 640 --source dataset/images/
``` 

- `--source 0 dataset/images/`: Specifies the folder containing images for testing.

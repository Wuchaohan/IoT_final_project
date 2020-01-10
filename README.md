# IoT final project: Face Detection on taking attendance

Taking attendance in class by manual is a conventional way to know the students' attendance level. It may be time-consuming to take attendance. Also, teacher may make mistake to write down an inaccurate data. Nowadays, face detection becomes the trend and is applied to many applications. For me, I wanna to use this 
technology on taking attendance by ueing python API OpenCV-OpenVINO in Raspberry pi.

## Required items
* Raspberry pi 3 (Model B)
* Raspberry pi Power supply
* Raspberry Pi 3.5 Inch LCD with HDMI
* Raspberry pi camera NoIR/w CS   
 

## Component Make-Up

k

## Raspberry Pi Environment Setting

* If you start with a new raspberry pi, you need to set the basic environment before going on.
(Please refer to the attached file: RaspberryPi_setting.pdf)

* Then we set the OpenVINO. All of the steps are clearly written down in the OpenVINO official document. Just follow it step-by-step.

[Install OpenVINO™ toolkit for Raspbian* OS](https://docs.openvinotoolkit.org/latest/_docs_install_guides_installing_openvino_raspbian.html)

[Getting Started with the Intel® Neural Compute Stick 2 on Raspbian](https://www.youtube.com/watch?v=34KN-UJsd58)

*  Now everything are deployed. Let's start coding.

## Programming

In my project, there are two python files and three xml files in FaceRecognition folder. Let's analysis how to code works.

### Step1: Import the packages

`import cv2

from lineNotifyMessage import lineNotifyMessage`


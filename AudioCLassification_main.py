import PySimpleGUI as sg
import pygame
import pickle

sg.ChangeLookAndFeel('NeutralBlue')

#The window layout of the interface using PySimpleGUI library
layout = [
        [sg.Text('Welcome to the Audio Classification Program!')],
        [sg.Text('Select your Audio:'), sg.Input(),
         sg.FileBrowse(key="-IN-")],
        [sg.Button('Play Audio', key='play')],
        [sg.Button('Check Audio - Music or Speech', key='modelbulding')]
    ]
window = sg.Window('Music and Speech Audio Classification', layout, keep_on_top=True)
    
while True:
        event, values = window.read()

        #to play the selected audio
        if event in ('play'):
            import simpleaudio as sa
            #print(values["-IN-"])
            wave_obj = sa.WaveObject.from_wave_file(values["-IN-"])
            play_obj = wave_obj.play()
            play_obj.wait_done()
         #to build a model from train_data with both music and speech files using feature extraction with pyAudioAnalysis library     
        if event in ('modelbulding'):
            from pyAudioAnalysis import audioTrainTest as aT
            def featandmodelcreation():
                aT.extract_features_and_train([".\\train_data\\music",".\\train_data\\speech"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
            featandmodelcreation()
            c, p, p_nam = aT.file_classification(values["-IN-"], "svmSMtemp","svm")
            #0.0 --> music class
            if c == 0.0:
                sg.Popup('The audio is music', keep_on_top=True)
            #1.0 --> speech class    
            elif c == 1.0:
                sg.Popup('The audio is speech', keep_on_top=True)
window.close()
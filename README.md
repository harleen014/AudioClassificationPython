This project is to implement an audio classification system that involves audio signal processing and machine learning model.
The graphic user interface allows users to browse given test audio files from the given database, select the query audio, and to classify if it belongs to music or speech class. User can also listen the audio by playing the selected audio from the database. 

Technical Details:

The project is implemented in Python using different libraries for audio classification and analysis.
For the GUI, “PySimpleGUI” library is used to build the interface of the Audio Classification System in this assignment.
Next to play the audio in the system, “simpleaudio” library is used. WaveObject.from_wave_file of simpleaudio is used to read the selected audio file and play() method helps to play the read audio file.

For extracting the features and building a machine learning model from the training data, “pyAudioAnalysis” library is used for machine learning process. So, lets see briefly what happens using this library, what steps are taken for building a machine learning process.
pyAudioAnalysis implements the following functionalities:
• Feature extraction: several audio features both from the time and frequency domain are
implemented in the library.
• Classification: supervised knowledge (i.e. annotated recordings) is used to train classifiers. A
cross-validation procedure is also implemented in order to estimate the optimal classifie
pyAudioAnalysis implements the following functionalities:
• Feature extraction: several audio features both from the time and frequency domain are
implemented in the library.
• Classification: supervised knowledge (i.e. annotated recordings) is used to train classifiers. A
cross-validation procedure is also implemented in order to estimate the optimal classifie
pyAudioAnalysis implements the following functionalities:
• Feature extraction: several audio features both from the time and frequency domain are
implemented in the library.
• Classification: supervised knowledge (i.e. annotated recordings) is used to train classifiers. A
cross-validation procedure is also implemented in order to estimate the optimal classifie
pyAudioAnalysis implements the following functionalities:
• Feature extraction: several audio features both from the time and frequency domain are
implemented in the library.
• Classification: supervised knowledge (i.e. annotated recordings) is used to train classifiers. A
cross-validation procedure is also implemented in order to estimate the optimal classifie
pyAudioAnalysis implements the following functionalities:
• Feature extraction: several audio features both from the time and frequency domain are
implemented in the library.
• Classification: supervised knowledge (i.e. annotated recordings) is used to train classifiers. A
cross-validation procedure is also implemented in order to estimate the optimal classifie
pyAudioAnalysis implements the following functionalities:
• Feature extraction: several audio features both from the time and frequency domain are
implemented in the library.
• Classification: supervised knowledge (i.e. annotated recordings) is used to train classifiers. A
cross-validation procedure is also implemented in order to estimate the optimal classifie
pyAudioAnalysis implements the following functionalities:
• Feature extraction: several audio features both from the time and frequency domain are
implemented in the library.
• Classification: supervised knowledge (i.e. annotated recordings) is used to train classifiers. A
cross-validation procedure is also implemented in order to estimate the optimal classifie
pyAudioAnalysis implements the following functionalities:
• Feature extraction: several audio features both from the time and frequency domain are
implemented in the library.
• Classification: supervised knowledge (i.e. annotated recordings) is used to train classifiers. A
cross-validation procedure is also implemented in order to estimate the optimal classifie
pyAudioAnalysis implements the following functionalities:
• Feature extraction: several audio features both from the time and frequency domain are
implemented in the library.
• Classification: supervised knowledge (i.e. annotated recordings) is used to train classifiers. A
cross-validation procedure is also implemented in order to estimate the optimal classifie

pyAudioAnalysis implements the following functionalities:
• Feature extraction: several audio features both from the time and frequency domain are
implemented in the library.
• Classification: supervised knowledge (i.e., annotated recordings) is used to train classifiers. A
cross-validation procedure is also implemented to estimate the optimal classifier parameter (e.g., the cost parameter in Support Vector Machines or the number of nearest neighbors used in the kNN classifier). The output of this functionality is a classifier model which can be stored in a file. In addition, wrappers that classify an unknown audio file (or a set of audio files) are also provided in that context. In this system, we have used SVM model.
• Segmentation: the following supervised or unsupervised segmentation tasks are implemented
in the library: fix-sized segmentation and classification, silence removal, speaker diarization
and audio thumbnailing. When required, trained models are used to classify audio segments
to predefined classes, or to estimate one or more learned variables (regression).

Feature Extraction: 
he aforementioned list of features can be extracted in a short-term basis: the audio signal is
first divided into short-term windows (frames) and for each frame all 34 features are calculated.
This results in a sequence of short-term feature vectors of 34 elements each. Widely accepted
The list of features can be extracted in a short-term basis: the audio signal is first divided into short-term windows (frames) and for each frame all 34 features are calculated. This results in a sequence of short-term feature vectors of 34 elements each. Widely accepted short-term window sizes are 20 to 100 ms. In pyAudioAnalysis, the short-term process can be conducted either using overlapping (frame step is shorter than the frame length) or non-over-lapping (frame step is equal to the frame length) framing. 
In mid-term basis, according to which the audio signal is first divided into mid-term windows(segments), which can be either overlapping or non-overlapping. For each segment, the short-term processing stage is carried out and the feature sequence from each mid-term segment, is used for computing feature statistics (e.g., the average value of the ZCR). Therefore, each mid-term segment is represented by a set of statistics. Typical values of the mid-term segment size can be 1 to 10 seconds. In cases of long recordings (e.g., music tracks) a long-term averaging of the mid-term features can be applied so that the whole signal is represented by an average vec-tor of mid-term statistics.
Some of the important features listed below:
Index Name Description
•	Zero Crossing Rate: The rate of sign-changes of the signal during the duration of a particular frame.
•	Energy: The sum of squares of the signal values, normalized by the respective frame length.
•	Entropy of Energy: The entropy of sub-frames’ normalized energies. It can be interpreted as a measure of abrupt changes.
•	Spectral Centroid: The center of gravity of the spectrum.
•	Spectral Spread: The second central moment of the spectrum.
•	Spectral Entropy: Entropy of the normalized spectral energies for a set of sub-frames.


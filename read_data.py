from imagehash import  hex_to_hash
from PyQt5.QtWidgets import QFileDialog
import pydub
import  json
import numpy as np
import  librosa
from PIL import Image
import imagehash
import librosa.display
from  error_msg import error
class song_import():
    frame_size = 2048
    hop_size = 512
    def imp_song(self):
        path_image = QFileDialog.getOpenFileName(None, 'Open MP3 ', '/home', "MP3 (*.mp3)")[0]
        return path_image

    def get_song(self):
        try:
            path = self.imp_song() 
            error().error_if_not_equal(len(path))
            song = pydub.AudioSegment.from_mp3(path)[:60000]
            song.export("file.wav", format="wav")
            data,sr = librosa.load("file.wav")
            return data
        except Exception:
            return 0

    def extract_features(self,data):
        S_signal = librosa.stft(data, n_fft=2048, hop_length=512)  # STFT of y
        y_scale = np.abs(S_signal) ** 2
        y_log_scale = librosa.power_to_db(y_scale)
        mel_spectrogram     = librosa.feature.melspectrogram(data, 22050, n_fft=2048, hop_length=512, n_mels=10)
        log_mel_spectrogram = librosa.power_to_db(mel_spectrogram)
        mfcc                = librosa.feature.mfcc(data, 22050)
        return self.get_hash(y_log_scale,log_mel_spectrogram, mfcc  )

    def createPerceptualHash(self,arrayData: "np.ndarray") -> str:
        dataInstance = Image.fromarray(arrayData)
        return imagehash.phash(dataInstance, hash_size=16).__str__()

    def get_hash (self,spec,feature1,feature2):
        features=[spec,feature1,feature2]
        features_hashes=[]
        for i in range (3):
            features_hashes.append(self.createPerceptualHash(features[i]))
        return features_hashes
    def Similarity_index(self,hash1,hash2):
        return ((hex_to_hash(hash1)-hex_to_hash(hash2)))

    def mapRanges(self,inputValue: float, inMin: float, inMax: float, outMin: float, outMax: float):
        slope = (outMax - outMin) / (inMax - inMin)
        return outMin + slope * (inputValue - inMin)

    def similarity_iteration(self,song_data):
        song_hashes=self.extract_features(song_data)
        with  open(r'songs3.json')as f:
            data_base = json.loads(f.read())
        similarity_Indexes=[]
        for i in range(0, 168):
            avg=(self.Similarity_index(song_hashes[0], data_base['Spec_Hash'][i]) + self.Similarity_index(song_hashes[1], data_base['HashFeature1'][i]) + self.Similarity_index(song_hashes[2], data_base['HashFeature2'][i])) / 3
            avgMap = self.mapRanges(avg, 0, 255, 0, 1)
            result = (1 - avgMap) * 100
            similarity_Indexes.append(result)
            Arr_OfMaxes = np.array(similarity_Indexes)
            Arr2 = Arr_OfMaxes.argsort()[-10:][::-1]
        top_10_song_list=[]
        top_10_similarity_list=[]
        for i in Arr2:
            top_10_song_list.append(data_base['songs'][i])
            top_10_similarity_list.append(similarity_Indexes[i])
        return top_10_song_list,top_10_similarity_list

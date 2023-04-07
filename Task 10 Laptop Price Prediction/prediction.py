import os
import math
import numpy as np
import pandas as pd
import pickle

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "Resources")
encode_os_path = os.path.join(dir_of_interest, 'encode_os.sav')
scaler_path = os.path.join(dir_of_interest, 'scaler.sav')
y_scaler_path = os.path.join(dir_of_interest, 'y_scaler.sav')
model_path = os.path.join(dir_of_interest, 'finalized_model.sav')
HD_type_endict = {'HDD': 1,
                  'EMMC': 1.5,
                  'SSD': 2,
                  'Hybrid': 3}
RAM_type_endict = {'LPDDR3': 1,
                   'DDR4': 2, 'LPDDR4': 2, 'LPDDR4X': 2,
                   'DDR5': 3, 'LPDDR5': 3,
                   'Unified': 4
                   }
processor_endict = {'Qualcomm Snapdragon 7c Gen 2': 1, 'Intel Pentium': 1, 'Intel Celeron': 1, 'AMD': 1, 'AMD Athlon': 1,
                   'Intel Core i3': 2, 'AMD Ryzen 3': 2,
                   'Intel Core i5': 3, 'AMD Ryzen 5': 3,
                   'Intel Core i7': 4, 'AMD Ryzen 7': 4,
                   'Intel Core i9': 5, 'AMD Ryzen 9': 5,
                   'Apple M1': 6, 'Apple M1 Max': 6, 'Apple M1 Pro': 6,
                   'Apple M2': 7}
product_endict = {'Ultimus': 1, 'Infinix': 1,
                 'Lenovo': 2, 'ASUS': 2, 'realme': 2,'acer': 2,'RedmiBook': 2, 'Vaio': 2, 'Nokia': 2,
                 'GIGABYTE': 2, 'MSI': 2, 'HP': 2, 'DELL': 2, 'SAMSUNG': 2,
                 'ALIENWARE': 3, 'APPLE': 3
                 }


def data_transform(data):
    df_sample = pd.DataFrame(data, columns=['Product', 'Processor', 'OS', 'Display', 'RAM_size', 'RAM_type', 'HD_type', 'HD_size'])
    df_sample['Product'] = df_sample.Product.map(product_endict)
    df_sample['Processor'] = df_sample.Processor.map(processor_endict)
    encode_os = pickle.load(open(encode_os_path, 'rb'))
    df_sample['OS'] = encode_os.transform(df_sample['OS'])
    df_sample['RAM_type'] = df_sample.RAM_type.map(RAM_type_endict)
    df_sample['HD_type'] = df_sample.HD_type.map(HD_type_endict)
    scaler = pickle.load(open(scaler_path, 'rb'))
    scaled_features = df_sample.columns
    print(scaled_features)
    df_sample[scaled_features] = scaler.transform(df_sample[scaled_features].values)
    print(df_sample)
    return df_sample


def predict(df_sample):
    model = pickle.load(open(model_path, 'rb'))
    y_scaler = pickle.load(open(y_scaler_path, 'rb'))
    result = model.predict(df_sample)
    result = y_scaler.inverse_transform(result)
    print(result)
    return round(math.exp(result), 2)

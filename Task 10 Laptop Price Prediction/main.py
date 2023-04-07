import streamlit as st
import prediction
import time
if __name__ == '__main__':

    # st.set_page_config(layout='wide')
    st.title("Laptop Price Prediction by Mohammad Wasiq")
    processor_options = tuple(())
    os_options = tuple(())
    ram_options = tuple(())
    brand = st.selectbox('Select any brand:',
        ('Lenovo', 'ASUS', 'HP', 'DELL', 'RedmiBook', 'realme', 'acer',
       'MSI', 'APPLE', 'Infinix', 'SAMSUNG', 'Ultimus', 'Vaio',
       'GIGABYTE', 'Nokia', 'ALIENWARE'))

    if brand == 'APPLE':
        processor_options = ('Apple M1', 'Apple M2', 'Apple M1 Pro', 'Apple M1 Max')
        os_options = ('Mac',)
        ram_options = ('LPDDR3', 'DDR4', 'LPDDR4', 'LPDDR4X', 'DDR5', 'LPDDR5', 'Unified')
    else:
        processor_options = ('Intel Core i3', 'AMD Ryzen 5', 'Intel Core i5', 'AMD Ryzen 7',
       'AMD Ryzen 9', 'Intel Celeron', 'AMD Ryzen 3', 'AMD Athlon', 'Intel Core i7',
        'Qualcomm Snapdragon 7c Gen 2', 'Intel Pentium', 'Intel Core i9', 'AMD')
        os_options = ('Windows', 'DOS', 'Chrome')
        ram_options = ('LPDDR3', 'DDR4', 'LPDDR4', 'LPDDR4X', 'DDR5', 'LPDDR5')
        
    processor = st.selectbox('Select any Processor:',
                             processor_options)
    operating_system = st.selectbox('Select any OS:',
                                    os_options)
    display = st.select_slider('Choose any display (in inches):',
                               (11.6, 13., 13.3, 13.4, 13.5, 13.6, 14., 14.1, 14.2, 14.96, 15., 15.6, 16., 16.1, 16.2, 16.6, 17.3))
    ram_size = st.selectbox('Choose RAM size',
                            (4, 8, 16, 32))
    ram_type = st.selectbox('Select RAM type (in GB):',
                            ram_options)
    hd_size = st.selectbox('Choose HD size (in GB):',
                           (32, 64, 128, 256, 512, 1000, 1128, 1256, 1512, 2000))
    hd_type = st.selectbox('Select any HD type',
                           ('HDD', 'EMMC', 'SSD', 'Hybrid'))

    data = [[brand, processor, operating_system, display, ram_size, ram_type, hd_type, hd_size]]
    if st.button('Predict'):
        data = prediction.data_transform(data)
        data = prediction.predict(data)
        st.subheader(u'\u20B9' + str(data))


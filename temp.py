import cv2
import av
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import streamlit as st
import base64

st.set_page_config(page_title='IEEE CS PESU', page_icon='🏆')
'''
# IEEE CS PESU Summer Project
# Project Title Here
## Team Members -

1. Vaibhav Vemula (PES1UG19CS***)
2. Vaibhav Vemula (PES1UG19CS***)
3. Vaibhav Vemula (PES1UG19CS***)
'''

def predict(image):
    
    
    return cv2.flip(image, 1)


class VideoCapture:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = predict(img)
        return av.VideoFrame.from_ndarray(img, format="bgr24")
    
webrtc_streamer(
    key="TEST",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}),
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoCapture,
    async_processing=True,
)


'''### NOTE:'''
st.markdown(f'''
        <h6>
            When using this application on a MOBILE BROWSER, click the "PLAY" button
            <img width=130 src="data:image/png;base64,
            {base64.b64encode(open('images/playimg.png', "rb").read()).decode()}">
            and wait 1-2 minutes.
        </h6>
    ''', unsafe_allow_html=True)


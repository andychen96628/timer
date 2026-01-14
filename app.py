import streamlit as st
import time

st.set_page_config(page_title="Streamlit 計時器", page_icon="⏱️")

st.title("⏱️ 極簡計時器")

# 使用 Session State 來儲存計時狀態
if 'running' not in st.session_state:
    st.session_state.running = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
if 'elapsed_time' not in st.session_state:
    st.session_state.elapsed_time = 0

placeholder = st.empty()

# 按鈕排版
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("開始 / 繼續", use_container_width=True):
        st.session_state.running = True
        st.session_state.start_time = time.time() - st.session_state.elapsed_time

with col2:
    if st.button("暫停", use_container_width=True):
        st.session_state.running = False

with col3:
    if st.button("重設", use_container_width=True):
        st.session_state.running = False
        st.session_state.elapsed_time = 0

# 計時邏輯與顯示
while st.session_state.running:
    st.session_state.elapsed_time = time.time() - st.session_state.start_time
    
    # 格式化時間
    mins, secs = divmod(int(st.session_state.elapsed_time), 60)
    hrs, mins = divmod(mins, 60)
    time_str = f"{hrs:02d}:{mins:02d}:{secs:02d}"
    
    placeholder.metric("經過時間", time_str)
    time.sleep(0.1)
    st.rerun()

# 非執行狀態下的顯示
mins, secs = divmod(int(st.session_state.elapsed_time), 60)
hrs, mins = divmod(mins, 60)
placeholder.metric("經過時間", f"{hrs:02d}:{mins:02d}:{secs:02d}")
